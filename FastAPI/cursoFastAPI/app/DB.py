from sqlmodel import  Session, create_engine,SQLModel
from fastapi import Depends,FastAPI
from typing import Annotated
name="ProjectDB"
URL=f"sqlite:///{name}.db"
engine=create_engine(URL)
def create_tables(app:FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
def get_session():
    with Session(engine) as session:
        yield session
        #the endpoint call SessionDep and come reads this note 
SessionDep=Annotated[Session,Depends(get_session)]#depends is de injection of the function before calling the endpoint