from typing import Optional

from clio_client.models import User as ClioUser
from clio_sdk.adapter_factory.transformer import register_transformer
from clio_sdk.unified_models.user import User as DomainUser


def transform_user_fields(data: dict, context: Optional[dict] = None) -> dict:
    # TODO: Add field mapping logic here
    return data

register_transformer("user", transform_user_fields)
