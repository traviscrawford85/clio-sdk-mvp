from datetime import date, datetime
from typing import Any, List, Optional

from pydantic import BaseModel

from .unified_calendar import UnifiedCalendar


class UnifiedCalendar(BaseModel):
    color: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    updated_at: Optional[str] = None
    data: str
    all_day: Optional[bool] = None
    calendar_owner_id: Optional[int] = None
    court_rule: Optional[bool] = None
    description: Optional[str] = None
    end_at: Optional[str] = None
    location: Optional[str] = None
    parent_calendar_entry_id: Optional[int] = None
    permission: Optional[str] = None
    recurrence_rule: Optional[str] = None
    start_at: Optional[str] = None
    start_at_time_zone: Optional[str] = None
    summary: Optional[str] = None
    time_entries_count: Optional[int] = None
    light_color: Optional[str] = None
    visible: Optional[bool] = None
    court_rules_default_calendar: Optional[bool] = None
    source: Optional[str] = None
    type: Optional[str] = None
