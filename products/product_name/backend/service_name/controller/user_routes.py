from uuid import UUID

from service_name.infrastructure.fastapi_utils import APIRouter
from router.data_transfer_objects import UserDTO
from controller.mapping import map_user_dto_to_domain
from services.user_management_service import UserManagementService

def get_prefix() -> str:
    return "/user"

def user_routes() -> APIRouter:
    """Define endpoints to control User related CRUD operations."""
    router = APIRouter(prefix=get_prefix())
    service = UserManagementService()

    @router.get("/{user_id}")
    async def root(user_id: str) -> None:
        return {"Tec Exchange XII": "Welcome"}

    @router.post("")
    async def create(userdto: UserDTO):
        user = map_user_dto_to_domain(userdto)
        service.create_user(user=user)

    async def get_user(user_id: UUID) -> UserDTO:
        return service.get_user(user=user_id)

    return router
