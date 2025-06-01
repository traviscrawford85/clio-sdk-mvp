from typing import Optional
from clio_client.models.user import ClioUser
from clio_sdk.models.user import User
from clio_sdk.adapter_factory.transformer import register_transformer

from typing import Any, Dict, Optional


class UserTransformer:
    @staticmethod
    def from_clio(data: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return {
        
        }

    @staticmethod
    def transform_user_fields(data: dict, context: Optional[dict] = None) -> dict:
        if not isinstance(data, dict):
            raise ValueError("Expected data to be a dictionary")
        return {
            
        }

register_transformer("user", UserTransformer.transform_user_fields)

context = {
    "resource": resource,
    "resource_name": resource.capitalize(),
    ...
}