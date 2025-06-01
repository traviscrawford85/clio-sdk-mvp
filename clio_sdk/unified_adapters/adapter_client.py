from clio_client.models import Client as ClioClient
from clio_sdk.adapter_factory.base import make_model_adapter
from clio_sdk.unified_models.client import Client as DomainClient

adapter = make_model_adapter(ClioClient, DomainClient, name="client")
