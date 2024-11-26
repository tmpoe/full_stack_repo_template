from typing import Self
from uuid import UUID

from domain.entities import User
from infrastructure.database.database_factory import get_database
from service_name.domain.service.IUserManagementService import IUserManagementService


class UserManagementService(IUserManagementService):
    def __init__(self: Self) -> None:
        self.database = get_database()

    def create_user(self, user: User) -> None:
        self.database.create_user(user=user)

    def get_user(self, user_id: UUID) -> User:
        return self.database.get_user(user_id=user_id)