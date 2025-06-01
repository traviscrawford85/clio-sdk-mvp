from clio_client.models import Webhook as ClioWebhook
from clio_sdk.adapter_factory.base import make_model_adapter
from clio_sdk.unified_models.webhook import Webhook as DomainWebhook

adapter = make_model_adapter(ClioWebhook, DomainWebhook, name="webhook")
