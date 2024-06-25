from backend.domain.entities import User, Address
from backend.infrastructure.database._mongodb._models import UserDoc, AddressDoc


def map_user_to_user_doc(user: User) -> UserDoc:
    userdoc = UserDoc(
        _id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age,
    )
    if user.address:
        userdoc.address = AddressDoc(
            street=user.address.street,
            house_number=user.address.house_number,
            city=user.address.city,
            postal_code=user.address.postal_code,
            country=user.address.country,
        )
    print(userdoc.to_json())
    return userdoc


def map_userdoc_to_user(userdoc: UserDoc) -> User:
    if userdoc.address:
        return User(
            id=userdoc._id,
            first_name=userdoc.first_name,
            last_name=userdoc.last_name,
            age=userdoc.age,
            address=Address(
                street=userdoc.address.street,
                house_number=userdoc.address.house_number,
                city=userdoc.address.city,
                postal_code=userdoc.address.postal_code,
                country=userdoc.address.country,
            ),
        )
    return User(
        id=userdoc._id,
        first_name=userdoc.first_name,
        last_name=userdoc.last_name,
        age=userdoc.age,
        address={},
    )


def map_adress_to_address_doc(address: Address) -> AddressDoc:
    return AddressDoc(
        street=address.street,
        house_number=address.house_number,
        city=address.city,
        postal_code=address.postal_code,
        country=address.country,
    )