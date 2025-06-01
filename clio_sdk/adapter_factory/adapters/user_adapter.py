from typing import Any

from pydantic import BaseModel

from clio_client.models import User as ClioModel
from clio_sdk.unified_models.unified_user import UnifiedUser
from clio_sdk.adapter_factory.base import make_model_adapter

adapter = make_model_adapter(ClioModel, UnifiedUser, name="user")
