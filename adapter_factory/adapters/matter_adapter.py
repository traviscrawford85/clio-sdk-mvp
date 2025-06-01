from typing import Any

from pydantic import BaseModel

from clio_client.models import Matter as ClioModel
from clio_sdk.unified_models import Matter as UnifiedModel
from clio_client.models.matter import ClioMatter
from clio_sdk.models.matter import Matter
from clio_sdk.adapter_factory.base import make_model_adapter

adapter = make_model_adapter(ClioMatter, Matter, name="matter")