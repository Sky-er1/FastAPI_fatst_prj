from fastapi import APIRouter, Depends

from bookings.dao import BookingDAO
from bookings.schema import SBooking
from users.dependencies import get_current_user
from users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all()

@router.post("")
async def add_booking(user: Users = Depends(get_current_user)):
    return await BookingDAO.add()
