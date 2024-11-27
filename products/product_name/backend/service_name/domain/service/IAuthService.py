

from abc import abstractmethod, ABC
from uuid import UUID

class IUserManagementService(ABC):
    @abstractmethod
    async def get_current_user(token: str) -> dict:
        ...

    @abstractmethod
    def create_access_token(data: dict) -> dict:
        ...
