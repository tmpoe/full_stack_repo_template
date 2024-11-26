import datetime
from uuid import UUID, uuid4
from sqlaclhemy import String, Integer, ForeignKey
from sqlaclhemy.orm import declarative_base, mapped_column, relationship

Base = declarative_base()

class AddressORM(Base):
    _id = mapped_column(Integer, primary_key=True)
    street = mapped_column(String, nullable=False)
    house_number = mapped_column(String, nullable=False)
    city = mapped_column(String, nullable=False)
    postal_code = mapped_column(Integer, nullable=False)
    country = mapped_column(String, nullable=False)


class UserORM(Base):
    __tablename__ = 'user'
    _id = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    first_name = mapped_column(String, nullable=False)
    last_name = mapped_column(String, nullable=False)
    age = mapped_column(Integer, nullable=False)
    address_id = mapped_column(Integer, ForeignKey('address.id'), nullable=False)
    address = relationship("AddressORM", backref="users")
