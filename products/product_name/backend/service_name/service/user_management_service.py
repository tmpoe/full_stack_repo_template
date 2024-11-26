from typing import Self
from uuid import UUID

from domain.entities import User
from infrastructure.user_repository.database_factory import get_database
from service_name.domain.repository.IUserRepository import IUserRepository
from service_name.domain.service.IUserManagementService import IUserManagementService


class UserManagementService(IUserManagementService):
    def __init__(self: Self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def create_user(self, user: User) -> None:
        self.user_repository.create_user(user=user)

    def get_user(self, user_id: UUID) -> User:
        return self.user_repository.get_user(user_id=user_id)