from datetime import date

from fastapi import FastAPI, Query, Depends
from typing import Optional
from pydantic import BaseModel

from bookings.router import router as router_bookings
from users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)


class HotelsSearArgs:
    def __init__(self, hotel_id: int,
                 date_from: date,
                 date_to: Optional[date] = None,
                 stars: Optional[int] = Query(None, ge=1, le=5)
                 ):
        self.hotel_id = hotel_id
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars


class SHotel(BaseModel):
    adress: str
    name: str
    stars: int


list[SHotel]


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/hotels/{hotel_id}")
async def hotels(search_args: HotelsSearArgs = Depends()):

    return search_args

