from uuid import UUID

from dependency_injector import inject, Provide

from service_name.containers import Container
from service_name.domain.service.IUserManagementService import IUserManagementService
from service_name.infrastructure.fastapi_utils import APIRouter
from service_name.controller.data_transfer_objects import UserDTO
from controller.mapping import map_user_dto_to_domain
from service_name.service.user_management_service import UserManagementService

def get_prefix() -> str:
    return "/user"

@inject
def user_routes(user_management_service: IUserManagementService = Provide[Container.user_management_service]) -> APIRouter:
    """Define endpoints to control User related CRUD operations."""
    router = APIRouter(prefix=get_prefix())

    @router.get("/{user_id}")
    async def root(user_id: str) -> None:
        return {"Tec Exchange XII": "Welcome"}

    @router.post("")
    async def create(userdto: UserDTO):
        user = map_user_dto_to_domain(userdto)
        user_management_service.create_user(user=user)

    async def get_user(user_id: UUID) -> UserDTO:
        return user_management_service.get_user(user=user_id)

    return router
