from typing import Annotated
from uuid import UUID

from dependency_injector import inject, Provide
from fastapi import Depends

from products.product_name.backend.service_name.controller.auth import get_current_user
from service_name.containers import Container
from service_name.domain.service.IUserManagementService import IUserManagementService
from service_name.infrastructure.fastapi_utils import APIRouter
from service_name.controller.data_transfer_objects import UserDTO
from controller.mapping import map_user_dto_to_domain

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
    async def create(
        userdto: UserDTO,
        current_user: Annotated[str, Depends(get_current_user)]
    ):
        user = map_user_dto_to_domain(userdto)
        user_management_service.create_user(user=user)

    async def get_user(
            user_id: UUID,
            current_user: Annotated[str, Depends(get_current_user)]
        ) -> UserDTO:
        return user_management_service.get_user(user=user_id)

    return router
