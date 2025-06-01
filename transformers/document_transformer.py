from typing import Optional

from clio_client.models import Document as ClioDocument
from clio_sdk.adapter_factory.transformer import register_transformer
from clio_sdk.unified_models.document import Document as DomainDocument


def transform_document_fields(data: dict, context: Optional[dict] = None) -> dict:
    # TODO: Add field mapping logic here
    return data

register_transformer("document", transform_document_fields)
