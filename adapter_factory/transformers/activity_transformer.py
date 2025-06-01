from typing import Optional
from clio_client.models.activity import ClioActivity
from clio_sdk.models.activity import Activity
from clio_sdk.adapter_factory.transformer import register_transformer

from typing import Any, Dict, Optional


class ActivityTransformer:
    @staticmethod
    def from_clio(data: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return {
        
        }

    @staticmethod
    def transform_activity_fields(data: dict, context: Optional[dict] = None) -> dict:
        if not isinstance(data, dict):
            raise ValueError("Expected data to be a dictionary")
        return {
            
        }

register_transformer("activity", ActivityTransformer.transform_activity_fields)

context = {
    "resource": resource,
    "resource_name": resource.capitalize(),
    ...
}