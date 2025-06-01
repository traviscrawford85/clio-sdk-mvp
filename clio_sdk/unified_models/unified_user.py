from datetime import date, datetime
from typing import Any, List, Optional

from pydantic import BaseModel

from .unified_user import UnifiedUser


class UnifiedUser(BaseModel):
    data: str
    account_owner: Optional[bool] = None
    clio_connect: Optional[bool] = None
    court_rules_default_attendee: Optional[bool] = None
    created_at: Optional[str] = None
    default_calendar_id: Optional[int] = None
    email: Optional[str] = None
    enabled: Optional[bool] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[int] = None
    initials: Optional[str] = None
    last_name: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    rate: Optional[float] = None
    roles: Optional[List[str]] = None
    subscription_type: Optional[str] = None
    time_zone: Optional[str] = None
    updated_at: Optional[str] = None
