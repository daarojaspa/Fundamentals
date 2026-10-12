from fastapi import HTTPException, status, APIRouter,Query
from ..models import User, Plans,TransactionCreate, TransactionRead, TransactionUpdate, UserCreate, UserRead, UserUpdate,SubscriptionEnum
from ..models import UserTable , UserPlans,PlansTable
from ..DB import SessionDep, create_tables
from sqlmodel import select
from ..security import hash_password
router = APIRouter()


@router.get("/users", response_model=list[UserRead], tags=["users"])
async def list_of_users(session: SessionDep):
    return session.exec(select(UserTable)).all()


@router.get("/users/{user_id}", response_model=UserRead, tags=["users"])
async def read_user(user_id: int, session: SessionDep):
    user = session.get(UserTable, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the user with id {user_id} is not in database",
        )
    return user


@router.delete("/users/{user_id}", tags=["users"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, session: SessionDep):
    user = session.get(UserTable, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the user with id {user_id} is not in database",
        )
    session.delete(user)
    # commit explícito
    session.commit()
    # 204 → no body


@router.post("/users", response_model=UserRead, tags=["users"], status_code=status.HTTP_201_CREATED)
async def create_user(user_info: UserCreate, session: SessionDep):
    user = UserTable(
        **user_info.model_dump(exclude={"password"}),   # copy safe fields
        password=hash_password(user_info.password),      # hash before storing
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.patch("/users/{user_id}", status_code=status.HTTP_200_OK, response_model=UserRead, tags=["users"])
async def update_user(user_id: int, data: UserUpdate, session: SessionDep):
    # validate it exists
    user = session.get(UserTable, user_id)
    if not user:
        raise HTTPException(
            # uso de status codes
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the user with id {user_id} is not in database",
        )
    user_dic = data.model_dump(exclude_unset=True)
    user.sqlmodel_update(user_dic)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
@router.post("/user/{user_id}/plans/{plan_id}")
async def create_user_plan(session:SessionDep,user_id:int,plan_id:int,subscription:SubscriptionEnum=Query()):
    user_db=session.get(UserTable,user_id)
    plan_db=session.get(PlansTable,plan_id)
    if not user_db or not plan_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND       ,
            detail="user or plan do not exist"
        )
    Userplan_db=UserPlans(plan_id=plan_db.id,user_id=user_db.id)
    session.add(Userplan_db)
    session.commit()
    session.refresh(Userplan_db)
    return Userplan_db

@router.get("/user/{user_id}/plans",response_model=list[Plans])
async def lists_user_plans(user_id:int,session:SessionDep,subscription:SubscriptionEnum=Query()):
    user_db=session.get(UserTable,user_id)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    query= (
        select(UserPlans)
        .where(UserPlans.user_id==user_id)
        .where(UserPlans.subscription==subscription)
        
    )
    plans=session.exec(query).all()
    return plans