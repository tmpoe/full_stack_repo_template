from fastapi import APIRouter

from backend.domain.entities import User
from backend.router.data_transfer_objects import UserDTO
from backend.services.user_management_service import UserManagementService


def user_routes() -> APIRouter:
    """Define endpoints to control User related CRUD operations."""
    router = APIRouter(prefix="/user")
    service = UserManagementService()

    @router.get("/{user_id}")
    async def root(user_id: str) -> None:
        return {"Tec Exchange XII": "Welcome"}

    @router.post("")
    async def create(userdto: UserDTO):
        user = User.from_dto(userdto=userdto)
        service.create_user(user=user)

    return router
