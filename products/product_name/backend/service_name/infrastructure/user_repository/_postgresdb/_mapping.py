from sqlalchemy.orm import Session

from service_name.domain.entities import (  # Assuming these are in the same package
    AddressORM,
    UserORM,
)
from service_name.domain.entities import (  # Assuming these are in the same package
    Address,
    SupportedCountry,
    User,
)

def address_orm_to_domain(address_orm: AddressORM) -> Address:
    return Address(
        street=address_orm.street,
        house_number=address_orm.house_number,
        city=address_orm.city,
        postal_code=address_orm.postal_code,
        country=SupportedCountry(address_orm.country),
    )

def user_orm_to_domain(user_orm: UserORM) -> User:
    address = address_orm_to_domain(user_orm.address) if user_orm.address else None
    return User(
        id=user_orm._id,
        first_name=user_orm.first_name,
        last_name=user_orm.last_name,
        age=user_orm.age,
        address=address,
    )


def address_domain_to_orm(address_domain: Address, session: Session) -> AddressORM:
    address_orm = AddressORM(
        street=address_domain.street,
        house_number=address_domain.house_number,
        city=address_domain.city,
        postal_code=address_domain.postal_code,
        country=address_domain.country.value,  # Get the enum value
    ) 
    return address_orm


def user_domain_to_orm(user_domain: User, session: Session) -> UserORM:
    address_orm = address_domain_to_orm(user_domain.address, session) if user_domain.address else None
    user_orm = UserORM(
        _id=user_domain.id,
        first_name=user_domain.first_name,
        last_name=user_domain.last_name,
        age=user_domain.age,
        address=address_orm,  # Assign the AddressORM instance
    )
    return user_orm