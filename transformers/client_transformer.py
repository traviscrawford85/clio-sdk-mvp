from typing import Optional

from clio_client.models import Client as ClioClient
from clio_sdk.adapter_factory.transformer import register_transformer
from clio_sdk.unified_models.client import Client as DomainClient


def transform_client_fields(data: dict, context: Optional[dict] = None) -> dict:
    # TODO: Add field mapping logic here
    return data

register_transformer("client", transform_client_fields)
