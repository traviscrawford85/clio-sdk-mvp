# adapter_factory/transformers/webhook.py
from typing import Optional


def transform_webhook_fields(data: dict, context: Optional[dict] = None) -> dict:
    user = data.get("user", {})
    return {
        "id": data.get("id"),
        "url": data.get("url"),
        "fields": data.get("fields"),
        "shared_secret": data.get("shared_secret"),
        "model": data.get("model"),
        "status": data.get("status"),
        "events": data.get("events"),
        "expires_at": data.get("expires_at"),
        "created_at": data.get("created_at"),
        "updated_at": data.get("updated_at"),
        "user": {
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "enabled": user.get("enabled")
        }
    }
