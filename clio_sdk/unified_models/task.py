from datetime import date, datetime
from typing import Any, List, Optional

from pydantic import BaseModel
from clio_sdk.unified_models.base import ClioBaseModel


class Task(ClioBaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    updated_at: Optional[str] = None
    data: str
    description: Optional[str] = None
    name: Optional[str] = None
    templates_count: Optional[int] = None
    priority: Optional[str] = None
    private: Optional[bool] = None
    deleted_at: Optional[str] = None
    completed_at: Optional[str] = None
    due_at: Optional[str] = None
    notify_completion: Optional[bool] = None
    permission: Optional[str] = None
    status: Optional[str] = None
    statute_of_limitations: Optional[bool] = None
    time_entries_count: Optional[int] = None
    time_estimated: Optional[int] = None
