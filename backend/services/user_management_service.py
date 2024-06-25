from typing import Self

from backend.domain.entities import User
from backend.infrastructure.database.database_factory import get_database


class UserManagementService():
    def __init__(self: Self) -> None:
        self.database = get_database()

    def create_user(self, user: User) -> None:
        self.database.create_user(user=user)