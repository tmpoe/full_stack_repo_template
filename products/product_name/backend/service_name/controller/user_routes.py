from uuid import UUID

from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from service_name.domain.service.IAuthService import IAuthService
from service_name.domain.exception import translate_service_exception
from service_name.containers import Container
from service_name.domain.service.IUserManagementService import IUserManagementService
from service_name.infrastructure.fastapi_utils import APIRouter
from service_name.controller.data_transfer_objects import UserDTO
from service_name.controller.mapping import map_user_dto_to_domain

def get_prefix() -> str:
    return "/user"

@inject
def user_routes(
    user_management_service: IUserManagementService = Provide[Container.user_management_service],
    auth_service: IAuthService = Provide[Container.auth_service]
) -> APIRouter:
    """Define endpoints to control User related CRUD operations."""
    router = APIRouter(prefix=get_prefix())
    async def get_current_user(token: str = Depends(lambda: auth_service.oauth2_scheme)):
        return await auth_service.get_current_user(token)

    @router.get("/{user_id}")
    @translate_service_exception
    async def root(user_id: str) -> None:
        return {"Tec Exchange XII": "Welcome"}

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
