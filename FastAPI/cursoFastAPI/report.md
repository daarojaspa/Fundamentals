# Code Quality Report — `app/` (FastAPI + SQLModel course project)

Scope: everything under `app/` (`main.py`, `models.py`, `DB.py`, `security.py`, `routers/*.py`).
Every bug listed below was **reproduced** by booting the app with `TestClient` and calling the
endpoint, not just read off the page — see the "how I verified it" note on each one.

---

## 1. What's already good — keep doing this

- **One router per resource** (`users`, `transactions`, `invoices`, `plans`), included from
  `main.py`. This is the right way to keep a FastAPI app navigable past a handful of endpoints.
- **Separate Pydantic/SQLModel classes per use-case** (`UserCreate` / `UserRead` / `UserUpdate` /
  `UserTable`). This is the pattern that keeps `password` out of API responses while still
  letting the table model carry it — you clearly understood *why* this split exists, not just
  copied it. Same shape repeated for `Invoice` and `Transaction`. Keep this discipline for the
  payment fields on your next project (never let the table model double as the response model).
- **`SessionDep = Annotated[Session, Depends(get_session)]`** in `DB.py` — correct use of FastAPI
  dependency injection for a per-request session with guaranteed close via the `with` block.
- **`security.py`** truncates the password to 72 bytes before handing it to bcrypt
  (`password.encode("utf-8")[:72]`). That's the actual bcrypt limit and most beginner code gets
  this wrong or ignores it — good instinct to handle it explicitly.
- **`PositiveInt` on `Transaction.amount`** — validating "money must be positive" at the schema
  level instead of with an `if` in the route is the right altitude for that rule.

---

## 2. Confirmed bugs (reproduced, not guessed)

### 2.1 Creating a user always crashes on the response — `models.py:24-37`, `routers/users.py:40-49`
`User.email_validator` is a `field_validator` that queries the DB for an existing row with that
email and raises if found. It's defined on the shared base class `User`, which `UserRead` also
inherits from. FastAPI re-validates the **outgoing** response against `response_model=UserRead`.
So the sequence on `POST /users` is: insert the row → commit → serialize `UserRead` → the
validator queries the DB again → **finds the row it just inserted** → raises
`"that email is already registered"` → FastAPI turns that into a 500
`ResponseValidationError`.

```
fastapi.exceptions.ResponseValidationError: 1 validation error:
  {'type': 'value_error', 'loc': ('response', 'email'), 'msg': 'Value error, that email is already registered', ...}
  File ".../app/routers/users.py", line 40, in create_user
```

The user *is* persisted (you'd see it in the DB), but the client gets a 500 on every single
signup. This is the single most important bug in the project: a DB-querying rule was put on a
Pydantic validator that gets reused for both write-time and read-time models.

**Fix direction:** uniqueness must be a **database constraint** (`Field(unique=True, index=True)`
on `email`), enforced by catching `IntegrityError` in the router — not re-derived by querying on
every model instantiation, and never on a class shared with the read/output model.

### 2.2 `GET /{user_id}/invoices` — `NameError` on every call — `routers/invoices.py:10-14`
```python
@router.get("/{user_id}/invoices", response_model=list[InvoiceRead], tags=["invoices"])
async def get_list_invoices(session: SessionDep):
    return session.exec(select(InvoiceTable).where(InvoiceTable.user_id==user_id))
```
`user_id` is in the path but never declared as a function parameter, so the `where` clause
references a name that doesn't exist. Reproduced: `NameError: name 'user_id' is not defined`.

### 2.3 `POST /invoice` is an unimplemented stub — `routers/invoices.py:17-19`
```python
async def create_invoice(session: SessionDep):
    pass
```
Takes no body, does nothing, returns `None` against `response_model=InvoiceRead` — would itself
fail response validation if reached. There is currently no way to create an invoice through the
API at all, which also means `POST /transactions` (which requires a real `invoice_id`) has no
legitimate way to get one.

### 2.4 `GET /plans` — wrong model passed to `select()` — `routers/plans.py:17-19`
```python
plans = session.exec(select(Plans)).all()
```
`Plans` is the plain schema (no `table=True`); the table model is `PlansTable`. Reproduced:
`sqlalchemy.exc.ArgumentError: Column expression, FROM clause, or other columns clause element
expected, got <class 'app.models.Plans'>`. `GET /plans` cannot return `200` as written.

Also note `response_model=Plans` / `list[Plans]` on both plan endpoints — `Plans` has no `id`
field, so even once the query is fixed, clients can never learn a plan's id from the API. There's
already a correct `PlanRead(Plans)` model in `models.py:118` with `id: int` that isn't used
anywhere.

### 2.5 `HTTPException(..., details=...)` — wrong keyword — `routers/users.py:73-76`
```python
raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    details="user or plan do not exist",
)
```
`HTTPException` takes `detail`, not `details`. Reproduced:
`TypeError: HTTPException.__init__() got an unexpected keyword argument 'details'`. Instead of a
clean 404, the client gets an unhandled 500 — worse than not checking at all, because it masks
the real "not found" case.

### 2.6 `status.HTTP_404_not_found` — wrong attribute name — `routers/users.py:87`
```python
raise HTTPException(status_code=status.HTTP_404_not_found)
```
Reproduced: `AttributeError: module 'starlette.status' has no attribute 'HTTP_404_not_found'`
(the real constant is `HTTP_404_NOT_FOUND`, all caps). Same failure mode as 2.5: a guard clause
meant to produce a clean 404 instead produces an unhandled 500.

### 2.7 `GET /user/{id}/plans` response model doesn't match what's returned — `routers/users.py:83-95`
`response_model=list[Plans]` but the query selects `UserPlans` rows (`user_id`, `plan_id`,
`subscription`, `id` — none of which are `Plans` fields: `name`, `price`, `description`).
Reproduced: `ResponseValidationError` as soon as a matching row exists. This endpoint's name says
"list a user's plans" but it would need to join through to `PlansTable` to actually return plans.

---

## 3. Design issues (not crashes, but the wrong shape for what you're describing building next)

You said the next project integrates a **payment platform with an already-built external
service** — that's a materially different reliability bar than a CRUD course project, so these
are the gaps I'd treat as blocking, not "nice to have":

- **No auth on any endpoint.** `hash_password` / `verify_password` exist in `security.py` but
  there is no login route, no token issuance, no `Depends` that checks *who* is calling. Every
  route — including deleting users and creating transactions — is open to anyone who can reach
  the server. A payment integration talks to money; this has to exist before anything else.
- **No idempotency on `POST /transactions`.** Payment gateways retry webhooks and clients retry
  timed-out requests. Without an idempotency key (client-supplied or derived from the gateway's
  event id) a retried request creates a second, duplicate transaction — a real double-charge risk
  once this touches an actual payment platform.
- **No status/state field on `Invoice` or `Transaction`.** Right now a transaction just *exists*;
  real payment flows are a state machine (`pending → authorized → captured → failed/refunded`).
  You'll want an explicit `status` enum plus a place to record the external provider's reference
  id (`provider_transaction_id`) so you can reconcile your DB against the gateway's records.
- **No webhook receiver modeled.** "Integrates with an already-built external service" almost
  always means that service calls *you* back asynchronously (payment succeeded/failed, days
  later for refunds). That's a distinct endpoint with its own concerns (verifying the request
  signature, being safely re-callable, not trusting the payload blindly) — worth designing as its
  own router from day one rather than bolting it on later.
- **No pagination anywhere**, including on `list_of_users` and (once fixed) `read_all` plans —
  every list endpoint does `select(...).all()` and returns the entire table. This is what the
  seed script below is for: generate enough rows that "just return everything" visibly becomes
  the wrong choice.
- **Existence-check boilerplate is copy-pasted in every router** (`get(...)`, `if not X: raise
  HTTPException(404, ...)`). Worth promoting to a shared dependency
  (e.g. `def get_user_or_404(user_id: int, session: SessionDep) -> UserTable`) once you have three
  or more copies of it — several of today's bugs (2.5, 2.6) are typos inside that exact
  boilerplate, which is itself an argument for writing it once.
- **Config is hardcoded**, not environment-driven: `DB.py` hardcodes `name="ProjectDB"` /
  `sqlite:///{name}.db`. `pydantic-settings` is already in `requirements.txt` but unused. A
  payment integration needs at least an API key/secret for the external service — those cannot be
  hardcoded, and reaching for `pydantic-settings`'s `BaseSettings` (env-var driven) now will save
  you from having to retrofit it under time pressure later.
- **No tests.** For CRUD-of-notes, that's a style choice. For money-moving code, an untested
  "does creating a transaction actually debit the right invoice" is a liability. Even a handful of
  `TestClient`-based tests (the same tool used to verify this report) covering the happy path and
  the "external service says payment failed" path pays for itself immediately.
- **Inconsistent REST paths**: `/users/{id}` (plural) in `users.py` vs `/user/{id}/plans`
  (singular) two lines later in the same file, and `/{user_id}/invoices` with no `/users` prefix
  at all in `invoices.py`. Small, but worth a five-minute pass — inconsistent paths are the kind
  of thing that turns into copy-pasted client bugs.

---

## 4. What I'd change about *how* the code was written, for next time

1. **Don't put DB queries inside a Pydantic `field_validator`.** Validators run on *every* model
   instantiation, including ones that were never meant to touch the DB (like building a response).
   If a rule needs the database, it belongs in the router (or a dedicated service function) that
   knows whether it's on the write path or the read path — not in the shared schema.
2. **Treat "returns 404 cleanly" as a code path worth testing**, not just an `if` you write once.
   Two of the seven bugs above (2.5, 2.6) are typos *inside* a not-found guard clause, which means
   they were never exercised — the happy path was tested, the error path wasn't. A one-line test
   per "does this raise 404 when the id is missing" would have caught both instantly.
3. **`response_model` is a contract, not a formality** — three of the bugs above (2.1, 2.4/2.7)
   are places where the model returned by the function doesn't actually match what the DB query
   produces. Whenever you write `response_model=X`, mentally re-read the function body and check
   that what's `return`ed really is (or trivially becomes) an `X`.
4. **Prefer the class that's actually named for the job.** `Plans` vs `PlansTable` vs `PlanRead`
   all exist in this file already — the plans router bugs come from reaching for the first one
   that "looked right" instead of the one built for that use (a `select()` needs the table class;
   a response needs the `Read` class with `id`).
5. **For a payments-adjacent service, design the failure/retry/webhook paths before the
   happy-path CRUD.** It's tempting to build create/read/update/delete first because it's
   familiar, but the hard, project-specific part of "integrate a payment platform" is
   idempotency, async status updates, and reconciliation — sketch those on paper (or in a state
   diagram) before writing the first router.

---

## 5. About `cration_of _trnasactions.py`

That script (in this same root folder) seeds a few hundred `TransactionTable` rows — along with
the `UserTable` / `InvoiceTable` rows they must reference — directly through SQLAlchemy Core
`insert()` rather than through the model layer, specifically *because* of bug 2.1: constructing
hundreds of `UserTable` instances would run the broken DB-querying email validator hundreds of
times (and eventually raise, since later dummy users would collide by design). See the comments
at the top of that file for the full reasoning. Once you fix section 2.1's root cause, the normal
`session.add(UserTable(...))` path becomes safe to use for seeding too.

Use the rows it creates to build pagination (`?limit=&offset=`) on `GET /transactions` yourself —
there is currently no `GET /transactions` list endpoint either, so that's a second gap you'll
need to fill in before pagination has anything to page through.
