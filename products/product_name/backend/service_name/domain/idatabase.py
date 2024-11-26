from abc import ABC, abstractmethod
from typing import Self
from uuid import UUID

from domain.entities import Address, User


class IDatabase(ABC):
    """Interface class of all Database connector."""

    @abstractmethod
    def test_connection(self: Self) -> None:
        """Check database conenction."""
        raise NotImplementedError

    @abstractmethod
    def get_user(self: Self, user_id: UUID) -> User:
        """Retrieve User object from database."""
        raise NotImplementedError

    @abstractmethod
    def create_user(self: Self, user: User) -> None:
        """Insert User to database."""
        raise NotImplementedError

    @abstractmethod
    def delete_user(self: Self, user: User) -> None:
        """Insert User to database."""
        raise NotImplementedError

    @abstractmethod
    def add_address_to_user(self: Self, user: User, address: Address) -> None:
        """Insert User to database."""
        raise NotImplementedError
