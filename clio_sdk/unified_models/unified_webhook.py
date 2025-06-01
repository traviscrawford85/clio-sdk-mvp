from datetime import date, datetime
from typing import Any, List, Optional

from pydantic import BaseModel

from .unified_webhook import UnifiedWebhook


class UnifiedWebhook(BaseModel):
    data: str
    created_at: Optional[str] = None
    etag: Optional[str] = None
    events: Optional[List[str]] = None
    expires_at: Optional[str] = None
    fields: Optional[str] = None
    id: Optional[int] = None
    model: Optional[str] = None
    shared_secret: Optional[str] = None
    status: Optional[str] = None
    updated_at: Optional[str] = None
    url: Optional[str] = None
