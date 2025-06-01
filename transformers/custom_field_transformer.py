from typing import Optional

from clio_client.models import CustomField as ClioCustomField
from clio_sdk.adapter_factory.transformer import register_transformer
from clio_sdk.unified_models.custom_field import CustomField as DomainCustomField


def transform_custom_field_fields(data: dict, context: Optional[dict] = None) -> dict:
    # TODO: Add field mapping logic here
    return data

register_transformer("custom_field", transform_custom_field_fields)
