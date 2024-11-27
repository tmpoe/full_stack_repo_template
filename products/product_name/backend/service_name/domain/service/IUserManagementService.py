from abc import abstractmethod, ABC
from uuid import UUID
from service_name.domain.entities import User

class IUserManagementService(ABC):
    @abstractmethod
    def create_user(self, user: User) -> None:
        ...

    @abstractmethod
    def get_user(self, user_id: UUID) -> User:
        ...