from enum import Enum
from typing import Optional, Self
from uuid import UUID, uuid4
from pydantic import BaseModel

from backend.router.data_transfer_objects import AddressDTO, UserDTO


class AppModel(BaseModel):
    """Covering Model of the application."""


class SupportedCountries(Enum):
    """Enum class for representing supported countries."""

    GERMANY = "DE"
    HUNGARY = "HU"
    AUSTRIA = "AT"
    CROATIA = "HR"


class Address(AppModel):
    """Model class represents User's address."""

    street: str
    house_number: str
    city: str
    postal_code: int
    country: SupportedCountries

    @staticmethod
    def from_dto(addressdto: AddressDTO) -> Self:
        if addressdto:
            return Address(
                street=addressdto.street,
                house_number=addressdto.house_number,
                city=addressdto.city,
                postal_code=addressdto.postal_code,
                country=addressdto.country,
            )
        return {}

class User(AppModel):
    """Model class represents user profile."""

    id: UUID
    first_name: str
    last_name: str
    age: int
    address: Optional[Address] = {}

    @staticmethod
    def from_dto(userdto: UserDTO) -> Self:
        user = User(
            id=uuid4(),
            first_name=userdto.first_name,
            last_name=userdto.last_name,
            age=userdto.age,
        )
        if userdto.address:
            user.address = Address.from_dto(userdto.address),

        return user