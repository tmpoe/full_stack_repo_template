from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from service_name.controller.authentication.auth import get_current_user
from service_name.domain.exception import translate_service_exception
from service_name.containers import Container
from service_name.domain.service.IUserManagementService import IUserManagementService
from service_name.infrastructure.fastapi_utils import APIRouter
from service_name.controller.data_transfer_objects import UserDTO
from service_name.controller.mapping import map_user_dto_to_domain
from service_name.service.auth_service import AuthService

def get_prefix() -> str:
    return "/user"

@inject
def user_routes(
    user_management_service: IUserManagementService = Provide[Container.user_management_service],
) -> APIRouter:
    """Define endpoints to control User related CRUD operations."""

    auth_service = AuthService()

    router = APIRouter(prefix=get_prefix())

    @router.post("")
    @translate_service_exception
    async def create(
        userdto: UserDTO,
        current_user = Depends(get_current_user)
    ):
        user = map_user_dto_to_domain(userdto)
        user_management_service.create_user(user=user)

    @router.get("/{user_id}")
    @translate_service_exception
    async def get_user(
            user_id: UUID,
            current_user = Depends(get_current_user)
        ) -> UserDTO:
        return user_management_service.get_user(user=user_id)

    return router
