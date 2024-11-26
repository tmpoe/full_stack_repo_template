from backend import config
from products.product_name.backend.service_name.domain.repository.IUserRepository import IDatabase

from products.product_name.backend.service_name.infrastructure.user_repository._mongodb.mongo_db_user_repository import MongoDBUserRepository


def get_database() -> IDatabase | None:
    if config.database_type == "mongo":
        return MongoDBUserRepository()
    return None
