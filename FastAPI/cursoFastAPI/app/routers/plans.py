from fastapi import HTTPException, status, APIRouter
from ..DB import SessionDep
from ..models import PlanRead, Plans,PlansTable
from sqlmodel import select

router = APIRouter()

@router.post("/plans", response_model=PlanRead, status_code=status.HTTP_201_CREATED,tags=["Plans"])
async def create_plan(plan_inf: Plans, session: SessionDep):
    plan = PlansTable.model_validate(plan_inf)
    session.add(plan)
    session.commit()
    session.refresh(plan)
    return plan

@router.get("/plans", response_model=list[PlanRead], status_code=status.HTTP_200_OK, tags=["Plans"])
async def read_all(session: SessionDep):
    plans = session.exec(select(PlansTable)).all()
    return plans