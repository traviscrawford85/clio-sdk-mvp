from datetime import date, datetime
from typing import Any, List, Optional

from pydantic import BaseModel

from .unified_activity import UnifiedActivity


class UnifiedActivity(BaseModel):
    amount: Optional[float] = None
    hierarchy: Optional[str] = None
    non_billable_amount: Optional[float] = None
    type: Optional[str] = None
    data: str
    accessible_to_user: Optional[bool] = None
    category_type: Optional[str] = None
    created_at: Optional[str] = None
    default: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    updated_at: Optional[str] = None
    utbms_activity_id: Optional[int] = None
    utbms_task_id: Optional[int] = None
    utbms_task_name: Optional[str] = None
    visible_to_co_counsel: Optional[bool] = None
    xero_service_code: Optional[str] = None
    co_counsel_contact_id: Optional[int] = None
    contact_id: Optional[int] = None
    flat_rate: Optional[bool] = None
    rate: Optional[float] = None
    calendar_owner_id: Optional[int] = None
    billed: Optional[bool] = None
    contingency_fee: Optional[bool] = None
    date: Optional[str] = None
    no_charge: Optional[bool] = None
    non_billable: Optional[bool] = None
    non_billable_total: Optional[float] = None
    note: Optional[str] = None
    on_bill: Optional[bool] = None
    price: Optional[float] = None
    quantity: Optional[float] = None
    quantity_in_hours: Optional[float] = None
    quantity_redacted: Optional[bool] = None
    reference: Optional[str] = None
    rounded_quantity: Optional[float] = None
    rounded_quantity_in_hours: Optional[float] = None
    tax_setting: Optional[str] = None
    total: Optional[float] = None
