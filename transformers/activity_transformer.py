from typing import Optional

from clio_client.models import Activity as ClioActivity
from clio_sdk.adapter_factory.transformer import register_transformer
from clio_sdk.unified_models.activity import Activity as DomainActivity


def transform_activity_fields(data: dict, context: Optional[dict] = None) -> dict:
    # TODO: Add field mapping logic here
    return data

register_transformer("activity", transform_activity_fields)
