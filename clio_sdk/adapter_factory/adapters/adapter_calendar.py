from typing import Any

from pydantic import BaseModel

from clio_client.models import Calendar as ClioModel

# Update the import path below to the correct module where Calendar is defined
from clio_sdk.unified_models.calendar import Calendar as UnifiedModel


def from_clio(clio_obj: ClioModel) -> UnifiedModel:
    return UnifiedModel(**clio_obj.model_dump())


def to_clio(sdk_obj: UnifiedModel) -> ClioModel:
    return ClioModel(**sdk_obj.model_dump())


adapter = {
    "from_clio": from_clio,
    "to_clio": to_clio,
}
