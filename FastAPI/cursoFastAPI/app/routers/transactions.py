from sqlmodel import select

from ..DB import SessionDep
from ..models import UserTable,Transaction,Invoice,TransactionRead,TransactionTable,TransactionUpdate,TransactionCreate
from fastapi import  HTTPException, Query,status,APIRouter

router=APIRouter()

@router.post("/transactions", response_model=TransactionRead, status_code=status.HTTP_201_CREATED, tags=["Transactions"])
async def create_transaction(data:TransactionCreate,session:SessionDep):
    data_dict=data.model_dump()
    user=session.get(UserTable,data_dict.get("user_id"))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user {data_dict.get('user_id')} not found")
    transaction_db=TransactionTable.model_validate(data_dict)
    session.add(transaction_db)
    #We dont pass the table because the model validate method   created an object of that class so the nature of the object 
    #tels wich table should go in 
    session.commit()
    session.refresh(transaction_db)
    return transaction_db
@router.get("/transactions",tags=["transactions"],response_model=list[TransactionRead])
async def read_transactions(session:SessionDep,skip:int=Query(0,description=" values to omit"),limit:int=Query(20,description="paginates every 20  items")):
    query=select(TransactionTable).offset(skip).limit(limit)
    transactions=session.exec(query).all()
    return transactions