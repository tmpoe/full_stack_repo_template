from backend import config
from products.product_name.backend.service_name.domain.repository.idatabase import IDatabase

from infrastructure.database._mongodb._database import MongoDatabase


def get_database() -> IDatabase | None:
    if config.database_type == "mongo":
        return MongoDatabase()
    return None
