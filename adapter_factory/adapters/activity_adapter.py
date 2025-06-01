from clio_client.models.activity import ClioActivity
from clio_sdk.models.activity import Activity
from clio_sdk.adapter_factory.base import make_model_adapter

adapter = make_model_adapter(ClioActivity, Activity, name="activity")