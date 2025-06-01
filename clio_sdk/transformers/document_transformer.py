from typing import Optional

from clio_sdk.adapter_factory.transformer import register_transformer
from clio_sdk.unified_models.document import Document as DomainDocument


def transform_document_fields(data: dict, context: Optional[dict] = None) -> dict:
    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "created_at": data.get("created_at"),
        "updated_at": data.get("updated_at"),
        "description": data.get("description"),
        # Add more fields as needed based on the unified model
    }

register_transformer("document", transform_document_fields)
