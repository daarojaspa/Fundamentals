from datetime import datetime
from fastapi import FastAPI, HTTPException,status
from zoneinfo import ZoneInfo
from .models import User, Invoice, Transaction
from .DB import SessionDep, create_tables
from sqlmodel import select
from .routers.users import router as user_router
from .routers.transactions import router as transaction_router
from .routers.invoices import router as invoice_router
from .routers.plans import router as plan_router


dic_timezones = {
    "CO": "America/Bogota",       # Colombia
    "US": "America/New_York",     # USA (Eastern — US has many, pick one)
    "MX": "America/Mexico_City",  # Mexico
    "AR": "America/Argentina/Buenos_Aires",  # Argentina
    "ES": "Europe/Madrid",        # Spain
    "GB": "Europe/London",        # UK
    "DE": "Europe/Berlin",        # Germany
    "JP": "Asia/Tokyo",           # Japan
    "IN": "Asia/Kolkata",         # India
    "BR": "America/Sao_Paulo",    # Brazil
}
app=FastAPI(lifespan=create_tables)

@app.get("/")
async def root():
    return{"message":"holaperras"}
@app.get("/timezone/{input_zone}")
def timezone_management (input_zone:str):
    iso_code=input_zone.upper()
    time_zone=dic_timezones.get(iso_code)
    if not time_zone:
        raise HTTPException(status_code=404,
                           detail=f" iso code or time zone no supported")    
    else:
        time= datetime.now(ZoneInfo(time_zone))#how to compute de time?
        return {"time":time,"time_zone": time_zone,"iso_code":iso_code}
    
    
    #################################### data models###################
app.include_router(user_router)
app.include_router(transaction_router)
app.include_router(invoice_router)
app.include_router(plan_router)
