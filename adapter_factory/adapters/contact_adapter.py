from clio_client.models.contact import ClioContact
from clio_sdk.models.contact import Contact
from clio_sdk.adapter_factory.base import make_model_adapter

adapter = make_model_adapter(ClioContact, Contact, name="contact")