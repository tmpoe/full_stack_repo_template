from typing import Self
from uuid import UUID
from mongoengine import connect

from config import mongo_url, mongo_db, mongo_username, mongo_password
from domain.entities import Address, User
from products.product_name.backend.service_name.domain.repository.idatabase import IDatabase
from infrastructure.database._mongodb._models import UserDoc
from infrastructure.database._mongodb._mapping import (
    map_userdoc_to_user, map_user_to_user_doc, map_adress_to_address_doc
)


class MongoDatabase(IDatabase):
    def __init__(self: Self) -> None:
        self.connection = connect(
            db=mongo_db, username=mongo_username, password=mongo_password, host=mongo_url,
        )

    def test_connection(self: Self) -> None:
        try:
            self.connection.admin.command("ping")
        except Exception as e:
            msg = f"Cannot connect to MongoDB. Error message: {e}"
            raise ConnectionError(msg)

    def get_user(self: Self, user_id: UUID) -> User:
        userdoc = UserDoc.objects(_id=user_id).first()
        return map_userdoc_to_user(userdoc=userdoc)

    def create_user(self: Self, user: User) -> None:
        userdoc = map_user_to_user_doc(user=user)
        userdoc.save()

    def delete_user(self: Self, user: User) -> None:
        UserDoc.objects(_id=user.id).first().delete()

    def add_address_to_user(self: Self, user: User, address: Address) -> None:
        if user.address:
            return

        address_doc = map_adress_to_address_doc(address=address)
        UserDoc.objects(_id=user.id).update_one(address=address_doc)
