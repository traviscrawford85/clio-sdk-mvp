from clio_client.models import Contact as ClioContact
from clio_sdk.adapter_factory.base import make_model_adapter
from clio_sdk.unified_models.contact import Contact as DomainContact

adapter = make_model_adapter(ClioContact, DomainContact, name="contact")
