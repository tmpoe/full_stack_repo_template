import datetime
from mongoengine import Document, StringField, IntField, EmbeddedDocument, UUIDField, EmbeddedDocumentField, DateField


class Metadata(EmbeddedDocument):
    insertion_date = DateField(required=True, default=datetime.datetime.now(datetime.timezone.utc))
    last_update = DateField(required=True, default=datetime.datetime.now(datetime.timezone.utc))

class AddressDoc(EmbeddedDocument):
    street = StringField(required=True)
    house_number = IntField(min_value=0, required=True)
    city = StringField(required=True)
    postal_code = IntField(min_value=0, max_value=10000, required=True)
    country = StringField(required=True)


class UserDoc(Document):
    _id = UUIDField(required=True)
    first_name = StringField(max_length=20, required=True)
    last_name = StringField(max_length=20, required=True)
    age = IntField(min_value=0, max_value=99, required=True)
    address = EmbeddedDocumentField(AddressDoc)
    metadata = EmbeddedDocumentField(Metadata, default=Metadata(), required=True)
