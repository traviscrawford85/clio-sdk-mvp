from clio_client.models import CustomFieldValue as ClioCustomFieldValue
from clio_sdk.adapter_factory.base import make_model_adapter
from clio_sdk.unified_models.custom_field_value import (
    CustomFieldValue as DomainCustomFieldValue,
)

adapter = make_model_adapter(ClioCustomFieldValue, DomainCustomFieldValue, name="custom_field_value")
