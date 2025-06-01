from clio_client.models import Activity as ClioActivity
from clio_sdk.adapter_factory.base import make_model_adapter
from clio_sdk.unified_models.activity import Activity as DomainActivity

adapter = make_model_adapter(ClioActivity, DomainActivity, name="activity")
