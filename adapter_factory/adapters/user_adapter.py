from typing import Any

from pydantic import BaseModel

from clio_client.models.user import ClioUser
from clio_sdk.models.user import User
from clio_sdk.adapter_factory.base import make_model_adapter

adapter = make_model_adapter(ClioUser, User, name="user")
