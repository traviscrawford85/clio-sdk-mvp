from typing import Optional

from clio_sdk.adapter_factory.transformer import register_transformer
from clio_sdk.unified_models.note import Note as DomainNote


def transform_note_fields(data: dict, context: Optional[dict] = None) -> dict:
    return {
        "id": data.get("id"),
        "content": data.get("content"),
        "created_at": data.get("created_at"),
        "updated_at": data.get("updated_at"),
        # Add more fields as needed based on the unified model
    }

register_transformer("note", transform_note_fields)
