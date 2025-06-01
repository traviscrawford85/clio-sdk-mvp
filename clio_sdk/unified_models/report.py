from datetime import date, datetime
from typing import Any, List, Optional

from clio_sdk.unified_models.base import ClioBaseModel


class Report(ClioBaseModel):
    data: str
    category: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    format: Optional[str] = None
    id: Optional[int] = None
    kind: Optional[str] = None
    last_generated_at: Optional[str] = None
    name: Optional[str] = None
    options: Optional[str] = None
    updated_at: Optional[str] = None
    day_of_month: Optional[int] = None
    days_of_week: Optional[List[int]] = None
    effective_from: Optional[str] = None
    every_no_of_months: Optional[int] = None
    frequency: Optional[str] = None
    next_scheduled_date: Optional[str] = None
    report_preset_id: Optional[int] = None
    status: Optional[str] = None
    status_updated_at: Optional[str] = None
    time_of_day: Optional[str] = None
    time_zone: Optional[str] = None
    progress: Optional[int] = None
    source: Optional[str] = None
    state: Optional[str] = None
