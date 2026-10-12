
from ..DB import SessionDep, create_tables
from ..models import Invoice,InvoiceTable, InvoiceCreate,InvoiceRead,InvoiceUpdate
from ..models import InvoiceTable
from fastapi import  HTTPException,status,APIRouter
from sqlmodel import select

router = APIRouter()

@router.get("/{user_id}/invoices", response_model=list[InvoiceRead],tags=["invoices"])
async def get_list_invoices(session:SessionDep,user_id):
    return session.exec(
        select(InvoiceTable).where(InvoiceTable.user_id==user_id)
    )


@router.post("/invoice",response_model=InvoiceRead,status_code=status.HTTP_201_CREATED)
async def create_invoice(session:SessionDep):
    pass

