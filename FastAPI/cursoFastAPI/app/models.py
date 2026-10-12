from pydantic import EmailStr, PositiveInt,field_validator
from sqlmodel import SQLModel, Field, Relationship,Session, select
from .DB import engine
from enum import Enum
##own data types
class SubscriptionEnum(str,Enum):
    FREETIER="freetier"
    PAYED="active"
    INACTIVE="inactive"
    
#link tables
class UserPlans(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    plan_id: int = Field(foreign_key="planstable.id")
    user_id: int = Field(foreign_key="usertable.id")
    subscription:SubscriptionEnum = Field(default=SubscriptionEnum.FREETIER)


# ---------- User ----------
class User(SQLModel):                       # shared base
    name: str                               # required (no fake None default)
    email: EmailStr =Field(default=None,unique=True)                         # required
    age: int | None = None                  # genuinely optional
    """ @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        session=Session(engine)
        query=(
            select(UserTable)
            .where(UserTable.email==value)
        )
        db=session.exec(query).first()
        if db !=None:
            raise ValueError(
                "that email is already registered"
            )
        return value 
     """    
        
    
class UserTable(User, table=True):
    id: int | None = Field(default=None, primary_key=True)
    active: bool = Field(default=True)
    password: str
    invoices: list["InvoiceTable"] = Relationship(back_populates="user")
    plans: list["PlansTable"] = Relationship(
        back_populates="users", link_model=UserPlans
    )
class UserCreate(User):                     # input: adds password
    password: str

class UserRead(User):                       # output: adds id, NO password
    id: int

class UserUpdate(SQLModel):                 # partial update: all optional
    name: str | None = None
    email: EmailStr | None = None
    age: int | None = None
    password: str | None = None


# ---------- Invoice ----------
class Invoice(SQLModel):                     # shared base
    user_id: int = Field(foreign_key="usertable.id")   # was "userout.id"

class InvoiceTable(Invoice, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user: UserTable | None = Relationship(back_populates="invoices")
    transactions: list["TransactionTable"] = Relationship(back_populates="invoice")
    

    def total(self) -> int:
        return sum(t.amount for t in self.transactions)

class InvoiceCreate(Invoice):
    pass

class InvoiceRead(Invoice):
    id: int
    user_id:int

class InvoiceUpdate(SQLModel):
    user_id: int | None = None


# ---------- Transaction ----------
class Transaction(SQLModel):                 # shared base
    amount: PositiveInt                      # required, must be > 0
    invoice_id: int = Field(foreign_key="invoicetable.id")

class TransactionTable(Transaction, table=True):
    id: int | None = Field(default=None, primary_key=True)
    invoice: InvoiceTable | None = Relationship(back_populates="transactions")

class TransactionCreate(Transaction):
    pass

class TransactionRead(Transaction):
    id: int

class TransactionUpdate(SQLModel):
    amount: PositiveInt | None = None
    invoice_id: int | None = None
# ---------- plans ----------
class Plans(SQLModel):
    name: str
    price: int
    description: str


# --- table models ---
class PlansTable(Plans, table=True):
    id: int | None = Field(default=None, primary_key=True)
    users: list["UserTable"] = Relationship(
        back_populates="plans", link_model=UserPlans
    )

class PlanRead(Plans):
    id: int