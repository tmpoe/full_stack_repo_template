from service_name.domain.entities import Address, User
from service_name.controller.data_transfer_objects import AddressDTO, UserDTO

def map_address_domain_to_dto(address: Address):
    return AddressDTO(
        street=address.street,
        house_number=address.house_number,
        city=address.city,
        postal_code=address.postal_code,
        country=address.country,
    )

def map_address_dto_to_domain(address_dto: AddressDTO):
    return Address(
        street=address_dto.street,
        house_number=address_dto.house_number,
        city=address_dto.city,
        postal_code=address_dto.postal_code,
        country=address_dto.country,
    )

def map_user_domain_to_dto(user: User):
    return UserDTO(
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age,
        address=map_address_domain_to_dto(user.address),
    )

def map_user_dto_to_domain(user_dto: UserDTO):
    return User(
        first_name=user_dto.first_name,
        last_name=user_dto.last_name,
        age=user_dto.age,
        address=map_address_dto_to_domain(user_dto.address),
    )

