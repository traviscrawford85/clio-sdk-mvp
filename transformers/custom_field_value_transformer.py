from typing import Optional

from clio_client.models import CustomFieldValue as ClioCustomFieldValue
from clio_sdk.adapter_factory.transformer import register_transformer
from clio_sdk.unified_models.custom_field_value import (
    CustomFieldValue as DomainCustomFieldValue,
)


def transform_custom_field_value_fields(data: dict, context: Optional[dict] = None) -> dict:
    # TODO: Add field mapping logic here
    return data

register_transformer("custom_field_value", transform_custom_field_value_fields)
