from random import Random as rng
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

