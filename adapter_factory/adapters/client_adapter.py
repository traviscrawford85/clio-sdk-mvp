from clio_client.models.client import ClioClient
from clio_sdk.models.client import Client
from clio_sdk.adapter_factory.base import make_model_adapter

adapter = make_model_adapter(ClioClient, Client, name="client")