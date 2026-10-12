from utilities import (
    FIRST_NAMES,
    LAST_NAMES,
    _unique_email,
    EMAIL_DOMAINS,
    DUMMY_PASSWORD_HASH,
    rng
)
from fastapi import status
from sqlmodel import Session, create_engine, SQLModel
import pytest

from sqlmodel import Session, select
from sqlalchemy import func

from ..models import UserTable


@pytest.fixture
def user_id(session: Session):
    last_id = session.exec(select(func.max(UserTable.id))).one()
    return last_id or 0
@pytest.fixture
def user_email(session:Session,user_id):
    email = session.exec(
    select(UserTable.email).where(UserTable.id == user_id)
).one()
    return email

@pytest.fixture
def user_data(user_id):
    first = rng.choice(FIRST_NAMES)
    last = rng.choice(LAST_NAMES)
    dictionary = {
        "name": f"{first} {last}",
        "email": _unique_email(user_id, rng.randint(5, 5000)),
        # Age is genuinely optional on the model, so leave a
        # realistic spread rather than always filling it in — that
        # mirrors real-world data, where optional fields are often
        # missing.
        "age": rng.choice([None, *range(18, 75)]),
        "active": True,
        "password": DUMMY_PASSWORD_HASH,
    }
    return dictionary

def test_create_user(client, user_data):
    response = client.post("/user", json=user_data)
    assert response.status_code == status.HTTP_201_CREATED

def test_read_nonexistent_user(client):
    response = client.get("/user/999999")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    
def test_read_existing_user(client, user_id, user_email):
    response = client.get(f"/user/{user_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["email"] == user_email
