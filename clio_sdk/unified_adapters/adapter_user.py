from clio_client.models import User as ClioUser
from clio_sdk.adapter_factory.base import make_model_adapter
from clio_sdk.unified_models.user import User as DomainUser

adapter = make_model_adapter(ClioUser, DomainUser, name="user")
