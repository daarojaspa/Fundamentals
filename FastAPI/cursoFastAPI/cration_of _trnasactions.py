#!/usr/bin/env python3
"""
Seed script: generates dummy Users, Invoices and (hundreds of) Transactions.

WHY THIS SCRIPT EXISTS
-----------------------
`GET /transactions` doesn't exist yet, and none of the current list endpoints
(`GET /users`, `GET /plans`) paginate — they just `select(...).all()` the whole
table. That's invisible with 3 rows in the DB. This script exists to make it
*visible*: it inserts a few hundred `TransactionTable` rows (plus the `Users`
and `Invoices` they must reference, since `Transaction.invoice_id` and
`Invoice.user_id` are foreign keys) so there's enough data to notice that
"return everything" is the wrong choice, and to build `?limit=&offset=`
pagination against.

WHY THIS GOES THROUGH SQLAlchemy CORE, NOT THE NORMAL `session.add(...)` PATH
--------------------------------------------------------------------------
Normally you'd write `session.add(UserTable(name=...,           =..., ...))`, same
as the routers do. This script deliberately does NOT do that, for a concrete
reason documented in report.md (section 2.1): `User.email_validator` (in
app/models.py) is a Pydantic `field_validator` that queries the database on
*every* instantiation of a `User`-derived model to check the email isn't
already taken. That's fine for one signup. It is not fine for a loop that
creates hundreds of users:
  1. It would run hundreds of extra SELECT queries (one DB round trip per
     validated instance), which is slow for no benefit in a seed script.
  2. Dummy emails are generated programmatically here and are guaranteed
     unique *within this run* (see `_unique_email` below), so the check is
     redundant for our purposes anyway.
So instead of building `UserTable(...)` Python objects (which would trigger
that validator through Pydantic), this script builds plain `dict` rows and
inserts them with SQLAlchemy Core's `insert()` against `UserTable.__table__`.
Core inserts talk straight to SQL and never run Pydantic/SQLModel validation
at all — the right tool when you're deliberately bulk-loading data you
already trust, as opposed to validating one untrusted request at a time.

WHY IDs ARE ASSIGNED EXPLICITLY INSTEAD OF LEFT TO AUTOINCREMENT
------------------------------------------------------------------
`Invoice.user_id` and `Transaction.invoice_id` are foreign keys, so invoice
rows need real user ids and transaction rows need real invoice ids *before*
they're inserted. With the normal ORM flow you'd `session.flush()` after
adding users to get their auto-assigned ids back, then build invoices, flush
again, etc. That works, but it means one flush per "layer" and hides what id
each row actually got. Since we're already bypassing the ORM for speed, it's
just as easy (and more explicit) to compute the ids ourselves:
  - read `MAX(id)` currently in each table (so re-running this script keeps
    adding new rows instead of colliding with what's already there), then
  - hand out sequential ids for the new batch in plain Python before
    building the insert statements.
This also means the whole run is a single `engine.begin()` transaction: if
anything fails partway through, nothing is committed — you never end up with
transactions pointing at invoices that didn't actually get inserted.

WHY PASSWORDS AREN'T HASHED ONE-BY-ONE
----------------------------------------
`security.hash_password` uses bcrypt, which is *intentionally* slow (that's
the whole point of it as a KDF) — bcrypt-hashing a few hundred distinct
passwords would make this script noticeably slow for zero benefit, since
nobody is ever going to log in as `dummy_user_137`. So it's hashed once and
reused for every dummy user. This shortcut is only acceptable because these
are throwaway seed accounts; never reuse a single hash across real users.

USAGE
-----
    python3 "cration_of _trnasactions.py"
    python3 "cration_of _trnasactions.py" --users 60 --transactions 600
    python3 "cration_of _trnasactions.py" --seed 42          # reproducible run
    python3 "cration_of _trnasactions.py" --wipe              # clear old dummy
                                                                # data first

Run it from the project root (same folder as `app/`), using the project's
virtualenv, e.g.:
    .env/bin/python3 "cration_of _trnasactions.py"
"""

from __future__ import annotations

import argparse
import random

from sqlalchemy import delete, func, insert, select
from sqlmodel import SQLModel

from app.DB import engine
from app.models import InvoiceTable, TransactionTable, UserTable
from app.security import hash_password

# Small hand-written name pools instead of a dependency like Faker: the
# project's requirements.txt doesn't include Faker, and pulling in a new
# dependency just to generate "User 137" style placeholder data isn't worth
# it. A few dozen first/last names combined with `random.choice` produce
# plenty of variety for seed data.
FIRST_NAMES = [
    "Ana", "Luis", "Maria", "Carlos", "Sofia", "Jorge", "Valentina", "Diego",
    "Camila", "Andres", "Laura", "Miguel", "Daniela", "Sebastian", "Paula",
    "Felipe", "Isabella", "Santiago", "Mariana", "Julian",
]
LAST_NAMES = [
    "Gomez", "Rodriguez", "Perez", "Martinez", "Lopez", "Garcia", "Torres",
    "Ramirez", "Diaz", "Vargas", "Castro", "Ortiz", "Rojas", "Silva", "Munoz",
]
EMAIL_DOMAINS = ["example.com", "example.org", "mailtest.dev"]

# A single bcrypt hash, computed once and reused for every dummy user — see
# the module docstring ("WHY PASSWORDS AREN'T HASHED ONE-BY-ONE") for why.
DUMMY_PASSWORD_HASH = hash_password("dummy-seed-password")


def _unique_email(index: int, rng: random.Random) -> str:
    """Build an email that's unique within this run via a monotonic index.

    Using the row's own sequential index as part of the local-part is a
    simpler and cheaper uniqueness guarantee than checking the database (the
    thing app/models.py's validator does per-row, which is exactly the cost
    this script avoids) — two dummy users can never collide because their
    indexes never repeat.
    """
    first = rng.choice(FIRST_NAMES)
    last = rng.choice(LAST_NAMES)
    domain = rng.choice(EMAIL_DOMAINS)
    return f"{first.lower()}.{last.lower()}{index}@{domain}"


def _next_id(conn, table) -> int:
    """Return the next free primary key for `table` (MAX(id) + 1, or 1)."""
    current_max = conn.execute(select(func.max(table.c.id))).scalar()
    return (current_max or 0) + 1


def build_users(start_id: int, count: int, rng: random.Random) -> list[dict]:
    rows = []
    for offset in range(count):
        user_id = start_id + offset
        first = rng.choice(FIRST_NAMES)
        last = rng.choice(LAST_NAMES)
        rows.append(
            {
                "id": user_id,
                "name": f"{first} {last}",
                "email": _unique_email(user_id, rng),
                # Age is genuinely optional on the model, so leave a
                # realistic spread rather than always filling it in — that
                # mirrors real-world data, where optional fields are often
                # missing.
                "age": rng.choice([None, *range(18, 75)]),
                "active": True,
                "password": DUMMY_PASSWORD_HASH,
            }
        )
    return rows


def build_invoices(
    start_id: int, user_ids: list[int], count: int, rng: random.Random
) -> list[dict]:
    """One row per invoice; `user_id` is picked from the users just created.

    `count` invoices are spread across `user_ids` with repeats allowed (a
    user can have several invoices), which is the realistic shape — nobody
    has exactly one invoice.
    """
    return [
        {"id": start_id + offset, "user_id": rng.choice(user_ids)}
        for offset in range(count)
    ]


def build_transactions(
    start_id: int, invoice_ids: list[int], count: int, rng: random.Random
) -> list[dict]:
    """Amounts are modeled as integer "cents" (e.g. 4599 = $45.99), matching
    `Transaction.amount: PositiveInt` on the model — SQLite/SQLModel has no
    dedicated decimal-money column here, so staying in integers avoids
    floating-point rounding entirely rather than working around it.
    """
    return [
        {
            "id": start_id + offset,
            "amount": rng.randint(500, 250_000),
            "invoice_id": rng.choice(invoice_ids),
        }
        for offset in range(count)
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Seed dummy Users/Invoices/Transactions for pagination practice.",
    )
    parser.add_argument(
        "--users", type=int, default=40,
        help="how many dummy users to insert (default: 40)",
    )
    parser.add_argument(
        "--invoices", type=int, default=120,
        help="how many dummy invoices to insert (default: 120)",
    )
    parser.add_argument(
        "--transactions", type=int, default=400,
        help="how many dummy transactions to insert (default: 400 — "
             "'hundreds', as requested)",
    )
    parser.add_argument(
        "--seed", type=int, default=None,
        help="random seed, for a reproducible run (default: nondeterministic)",
    )
    parser.add_argument(
        "--wipe", action="store_true",
        help="delete all existing rows from users/invoices/transactions "
             "before inserting new ones (opt-in: destructive, off by default)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rng = random.Random(args.seed)

    # Make sure the tables exist even on a completely fresh checkout — this
    # is the same call app/DB.py's `create_tables` makes on app startup, but
    # this script is meant to be runnable standalone, without booting the
    # FastAPI app first.
    SQLModel.metadata.create_all(engine)

    # `engine.begin()` opens one transaction and commits it automatically on
    # a clean exit, or rolls everything back if any statement raises. That
    # atomicity matters here specifically: transactions reference invoices,
    # which reference users — a partial write (say, users inserted but the
    # process crashes before invoices) would leave orphaned or dangling
    # foreign keys behind.
    with engine.begin() as conn:
        if args.wipe:
            # Children before parents, to respect the foreign keys.
            conn.execute(delete(TransactionTable.__table__))
            conn.execute(delete(InvoiceTable.__table__))
            conn.execute(delete(UserTable.__table__))

        next_user_id = _next_id(conn, UserTable.__table__)
        next_invoice_id = _next_id(conn, InvoiceTable.__table__)
        next_transaction_id = _next_id(conn, TransactionTable.__table__)

        user_rows = build_users(next_user_id, args.users, rng)
        conn.execute(insert(UserTable.__table__), user_rows)
        user_ids = [row["id"] for row in user_rows]

        invoice_rows = build_invoices(next_invoice_id, user_ids, args.invoices, rng)
        conn.execute(insert(InvoiceTable.__table__), invoice_rows)
        invoice_ids = [row["id"] for row in invoice_rows]

        transaction_rows = build_transactions(
            next_transaction_id, invoice_ids, args.transactions, rng
        )
        conn.execute(insert(TransactionTable.__table__), transaction_rows)

    print(
        f"Inserted {len(user_rows)} users "
        f"(ids {user_ids[0]}-{user_ids[-1]}), "
        f"{len(invoice_rows)} invoices "
        f"(ids {invoice_ids[0]}-{invoice_ids[-1]}), "
        f"{len(transaction_rows)} transactions "
        f"(ids {transaction_rows[0]['id']}-{transaction_rows[-1]['id']})."
    )
    print(
        "There is currently no GET /transactions endpoint in the API — "
        "add one and build ?limit=&offset= pagination against these rows."
    )


if __name__ == "__main__":
    main()
