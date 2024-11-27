

from abc import abstractmethod, ABC

class IAuthService(ABC):
    oauth2_scheme = ""
    @abstractmethod
    async def get_current_user(token: str) -> dict:
        ...

    @abstractmethod
    def create_access_token(data: dict) -> dict:
        ...
