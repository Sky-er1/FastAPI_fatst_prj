from dao.base import BaseDao
from users.models import Users


class UsersDAO(BaseDao):
    model = Users
