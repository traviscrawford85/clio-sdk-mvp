from datetime import date, datetime
from typing import Any, List, Optional

from pydantic import BaseModel
from clio_sdk.unified_models.base import ClioBaseModel


class Note(ClioBaseModel):
    data: str
    created_at: Optional[str] = None
    date: Optional[str] = None
    detail: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    subject: Optional[str] = None
    time_entries_count: Optional[int] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None
