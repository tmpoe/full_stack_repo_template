from backend import config
from backend.domain.idatabase import IDatabase

from backend.infrastructure.database._mongodb._database import MongoDatabase


def get_database() -> IDatabase | None:
    if config.database_type == "mongo":
        return MongoDatabase()
    return None
