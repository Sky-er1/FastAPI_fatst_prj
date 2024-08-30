from datetime import date

from fastapi import FastAPI, Query, Depends
from typing import Optional
from pydantic import BaseModel

from bookings.router import router as router_bookings
from users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)


