from datetime import date, datetime
from typing import Any, List, Optional

from pydantic import BaseModel

from .unified_document import UnifiedDocument


class UnifiedDocument(BaseModel):
    data: str
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    message: Optional[str] = None
    progress: Optional[float] = None
    size: Optional[int] = None
    state: Optional[str] = None
    updated_at: Optional[str] = None
    export_formats: Optional[str] = None
    filename: Optional[str] = None
    name: Optional[str] = None
    content_type: Optional[str] = None
    document_id: Optional[int] = None
    fully_uploaded: Optional[bool] = None
    put_url: Optional[str] = None
    received_at: Optional[str] = None
    uuid: Optional[str] = None
    version_number: Optional[int] = None
    deleted_at: Optional[str] = None
    locked: Optional[bool] = None
    type: Optional[str] = None
