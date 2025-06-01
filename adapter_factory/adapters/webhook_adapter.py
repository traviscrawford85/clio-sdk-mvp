from clio_client.models.webhook import ClioWebhook
from clio_sdk.models.webhook import Webhook
from clio_sdk.adapter_factory.base import make_model_adapter

adapter = make_model_adapter(ClioWebhook, Webhook, name="webhook")