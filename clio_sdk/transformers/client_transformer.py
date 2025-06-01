from typing import Optional

from clio_sdk.adapter_factory.transformer import register_transformer
from clio_sdk.unified_models.client import Client as DomainClient


def transform_client_fields(data: dict, context: Optional[dict] = None) -> dict:
    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "created_at": data.get("created_at"),
        "updated_at": data.get("updated_at"),
        # Add more fields as needed based on the unified model
    }

register_transformer("client", transform_client_fields)
