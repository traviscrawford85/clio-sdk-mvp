from clio_client.models import CustomField as ClioCustomField
from clio_sdk.adapter_factory.base import make_model_adapter
from clio_sdk.unified_models.custom_field import CustomField as DomainCustomField

adapter = make_model_adapter(ClioCustomField, DomainCustomField, name="custom_field")
