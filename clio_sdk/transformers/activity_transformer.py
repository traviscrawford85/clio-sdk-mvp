from typing import Optional

from clio_sdk.adapter_factory.transformer import register_transformer
from clio_sdk.unified_models.activity import Activity as DomainActivity


def transform_activity_fields(data: dict, context: Optional[dict] = None) -> dict:
    return {
        "amount": data.get("amount"),
        "hierarchy": data.get("hierarchy"),
        "non_billable_amount": data.get("non_billable_amount"),
        "type": data.get("type"),
        "data": data.get("data"),
        "accessible_to_user": data.get("accessible_to_user"),
        "category_type": data.get("category_type"),
        "created_at": data.get("created_at"),
        "default": data.get("default"),
        "etag": data.get("etag"),
        "id": data.get("id"),
        "name": data.get("name"),
        "updated_at": data.get("updated_at"),
        "utbms_activity_id": data.get("utbms_activity_id"),
        "utbms_task_id": data.get("utbms_task_id"),
        "utbms_task_name": data.get("utbms_task_name"),
        "visible_to_co_counsel": data.get("visible_to_co_counsel"),
        "xero_service_code": data.get("xero_service_code"),
        "co_counsel_contact_id": data.get("co_counsel_contact_id"),
        "contact_id": data.get("contact_id"),
        "flat_rate": data.get("flat_rate"),
        "rate": data.get("rate"),
        "calendar_owner_id": data.get("calendar_owner_id"),
        "billed": data.get("billed"),
        "contingency_fee": data.get("contingency_fee"),
        "date": data.get("date"),
        "no_charge": data.get("no_charge"),
        "non_billable": data.get("non_billable"),
        "non_billable_total": data.get("non_billable_total"),
        "note": data.get("note"),
        "on_bill": data.get("on_bill"),
        "price": data.get("price"),
        "quantity": data.get("quantity"),
        "quantity_in_hours": data.get("quantity_in_hours"),
        "quantity_redacted": data.get("quantity_redacted"),
        "reference": data.get("reference"),
        "rounded_quantity": data.get("rounded_quantity"),
        "rounded_quantity_in_hours": data.get("rounded_quantity_in_hours"),
        "tax_setting": data.get("tax_setting"),
        "total": data.get("total"),
    }


register_transformer("activity", transform_activity_fields)
