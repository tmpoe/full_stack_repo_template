from enum import Enum
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field



class SupportedCountry(Enum):
    GERMANY = "DE"
    HUNGARY = "HU"
    AUSTRIA = "AT"
    CROATIA = "HR"


class Address(BaseModel):
    street: str
    house_number: str
    city: str
    postal_code: int
    country: SupportedCountry


class User(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    age: int
    address: Optional[Address] = Field(default_factory=dict)
