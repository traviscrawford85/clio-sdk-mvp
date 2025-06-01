from clio_client.models import Matter as ClioMatter
from clio_sdk.adapter_factory.base import make_model_adapter
from clio_sdk.unified_models.matter import Matter as DomainMatter

adapter = make_model_adapter(ClioMatter, DomainMatter, name="matter")
