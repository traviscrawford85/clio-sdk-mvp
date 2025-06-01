# adapter_factory/transformers/contact.py
from typing import Optional

from clio_client.models import Contact as ClioContact
from clio_sdk.unified_models.contact import Contact as DomainContact


def transform_contact_fields(data: dict, context: Optional[dict] = None) -> dict:
    full_name = f"{data.get('first_name', '')} {data.get('last_name', '')}".strip()
    currency = data.get("currency", {})
    address = (
        data.get("primary_address")
        or data.get("primary_work_address")
        or data.get("secondary_address")
        or {}
    )

    return {
        "id": data.get("id"),
        "full_name": full_name,
        "email": data.get("primary_email_address"),
        "phone": data.get("primary_phone_number"),
        "currency_code": currency.get("code"),
        "address": {
            "street": address.get("street"),
            "city": address.get("city"),
            "province": address.get("province"),
            "postal_code": address.get("postal_code"),
            "country": address.get("country"),
        },
        "created_at": data.get("created_at"),
        "updated_at": data.get("updated_at"),
    }
