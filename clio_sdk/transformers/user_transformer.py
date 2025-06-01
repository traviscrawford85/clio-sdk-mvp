from typing import Optional

from clio_sdk.adapter_factory.transformer import register_transformer
from clio_sdk.unified_models.user import User as DomainUser


def transform_user_fields(data: dict, context: Optional[dict] = None) -> dict:
    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "email": data.get("email"),
        "created_at": data.get("created_at"),
        "updated_at": data.get("updated_at"),
        # Add more fields as needed based on the unified model
    }

register_transformer("user", transform_user_fields)
