from uuid import UUID

from ._models import (  # Assuming these are in the same package
    UserORM,
)
from service_name.domain.entities import (  # Assuming these are in the same package
    Address,
    User,
)
from service_name.infrastructure.user_repository._postgresdb._mapping import (  # Assuming these are in the same package
    address_domain_to_orm,
    user_domain_to_orm,
    user_orm_to_domain,
)
from service_name.domain.repository.IUserRepository import IUserRepository
from .utils import get_session

class PostgresUserRepository(IUserRepository):
    """Implementation of the IUserRepository interface for PostgreSQL."""

    def test_connection(self) -> None:
        """Check database connection."""
        with get_session() as session:
            try:
                session.execute("SELECT 1")  # Simple query to test the connection
            except Exception as e:
                raise ConnectionError("Failed to connect to the database") from e

    def get_user(self, user_id: UUID) -> User:
        """Retrieve User object from database."""
        with get_session() as session:
            user_orm = session.query(UserORM).filter(UserORM._id == user_id).first()
            if user_orm:
                return user_orm_to_domain(user_orm)
            else:
                return None  # Or raise an exception

    def create_user(self, user: User) -> None:
        """Insert User to database."""
        with get_session() as session:
            user_orm = user_domain_to_orm(user, session)
            session.add(user_orm)
            session.commit()

    def delete_user(self, user: User) -> None:
        """Delete User from database."""
        with get_session() as session:
            user_orm = session.query(UserORM).filter(UserORM._id == user.id).first()
            if user_orm:
                session.delete(user_orm)
                session.commit()

    def add_address_to_user(self, user: User, address: Address) -> None:
        """Add address to existing user in the database."""
        with get_session() as session:
            user_orm = session.query(UserORM).filter(UserORM._id == user.id).first()
            if user_orm:
                address_orm = address_domain_to_orm(address, session)
                user_orm.address = address_orm 
                session.commit()