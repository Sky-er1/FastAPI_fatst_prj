from dao.base import BaseDao
from bookings.models import Bookings


class BookingDAO(BaseDao):
    model = Bookings
