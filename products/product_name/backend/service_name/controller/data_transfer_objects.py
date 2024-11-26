from typing import Optional
from pydantic import BaseModel, Field


class AddressDTO(BaseModel):
    street: str
    house_number: str
    city: str
    postal_code: int
    country: str


class UserDTO(BaseModel):
    first_name: str
    last_name: str
    age: int
    address: Optional[AddressDTO] = Field(default_factory=dict)

