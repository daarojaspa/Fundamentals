import pytest
from fastapi.testclient import TestClient
from sqlmodel import  Session, create_engine,SQLModel
from sqlalchemy.pool import StaticPool
from fastapi import Depends,FastAPI
from typing import Annotated
from app.main import app
name="testDB"
TEST_URL=f"sqlite://{name}.db"
engine=create_engine(TEST_URL,
                     connect_args={"check_same_thread":False},
                     poolclass=StaticPool)
@pytest.fixture(name="session")
#compressing life cycle of schema to  the session life cycle+
def get_session():
    SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)

@pytest.fixture(name="client")#before running the test  creates the client and dependencie injection that are need it 
def client_fixture(session:Session):
    def get_session_overwrite():
        return session
    app.dependency_overrides[get_session]=get_session_overwrite
    with TestClient as client:
        yield client 
        app.dependency_overrides.clear()