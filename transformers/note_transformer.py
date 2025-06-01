from typing import Optional

from clio_client.models import Note as ClioNote
from clio_sdk.adapter_factory.transformer import register_transformer
from clio_sdk.unified_models.note import Note as DomainNote


def transform_note_fields(data: dict, context: Optional[dict] = None) -> dict:
    # TODO: Add field mapping logic here
    return data

register_transformer("note", transform_note_fields)
