from enum import Enum
from typing import Optional, Self
from uuid import UUID, uuid4
from pydantic import BaseModel

from router.data_transfer_objects import AddressDTO, UserDTO


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


class User(AppModel):
    """Model class represents user profile."""

    id: UUID
    first_name: str
    last_name: str
    age: int
    address: Optional[Address] = {}