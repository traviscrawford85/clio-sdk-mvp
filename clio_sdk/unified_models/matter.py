from datetime import date, datetime
from enum import Enum
from typing import Any, List, Optional, Union

from pydantic import BaseModel
from clio_sdk.unified_models.base import ClioBaseModel


# --- Main Matter Model ---
class Matter(ClioBaseModel):
    amount: Optional[float] = None
    id: Optional[int] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    updated_at: Optional[str] = None
    budget: Optional[float] = None
    include_expenses: Optional[bool] = None
    notification_threshold: Optional[int] = None
    notify_users: Optional[bool] = None
    data: str
    client_connect_user_id: Optional[int] = None
    contact_created_at: Optional[str] = None
    contact_updated_at: Optional[str] = None
    description: Optional[str] = None
    first_name: Optional[str] = None
    initials: Optional[str] = None
    is_client: Optional[bool] = None
    last_name: Optional[str] = None
    matter_id: Optional[int] = None
    matter_number: Optional[str] = None
    middle_name: Optional[str] = None
    name: Optional[str] = None
    prefix: Optional[str] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    relationship_name: Optional[str] = None
    secondary_email_address: Optional[str] = None
    secondary_phone_number: Optional[str] = None
    title: Optional[str] = None
    type: Optional[str] = None
    event: Optional[str] = None
    payload: Optional[dict] = None
    timestamp: Optional[str] = None
    on_invoice: Optional[bool] = None
    deleted_at: Optional[str] = None
    start_date: Optional[str] = None
    start_time: Optional[str] = None
    status: Optional[str] = None
    order: Optional[int] = None
    practice_area_id: Optional[str] = None
    billable: Optional[bool] = None
    billing_method: Optional[str] = None
    client_id: Optional[int] = None
    client_reference: Optional[str] = None
    close_date: Optional[str] = None
    custom_number: Optional[str] = None
    display_number: Optional[str] = None
    has_tasks: Optional[bool] = None
    last_activity_date: Optional[str] = None
    location: Optional[str] = None
    maildrop_address: Optional[str] = None
    matter_stage_updated_at: Optional[str] = None
    number: Optional[int] = None
    open_date: Optional[str] = None
    pending_date: Optional[str] = None
    shared: Optional[bool] = None

# --- Update Input Model and Enums ---
class MatterStatusEnum(str, Enum):
    open = "open"
    closed = "closed"
    pending = "pending"

class ResponsibleStaffModel(BaseModel):
    id: int

class PracticeAreaModel(BaseModel):
    id: int

class StatuteOfLimitationsModel(BaseModel):
    due_at: date

class CustomFieldValueModel(BaseModel):
    id: Union[int, str]
    value: Union[str, int, float, bool]
    custom_field: Optional[Any] = None  # Use Any or a more specific type if available

class GroupModel(BaseModel):
    id: int

class MatterUpdateInputModel(BaseModel):
    description: Optional[str] = None
    status: Optional[MatterStatusEnum] = None
    close_date: Optional[date] = None
    open_date: Optional[date] = None
    responsible_staff: Optional[ResponsibleStaffModel] = None
    statute_of_limitations: Optional[StatuteOfLimitationsModel] = None
    practice_area: Optional[PracticeAreaModel] = None
    custom_field_values: Optional[List[CustomFieldValueModel]] = None
    group: Optional[GroupModel] = None
