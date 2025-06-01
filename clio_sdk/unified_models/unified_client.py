from datetime import date, datetime
from typing import Any, List, Optional

from pydantic import BaseModel


class UnifiedClient(BaseModel):
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    unread_count: Optional[int] = None
    unread_notifiable_count: Optional[int] = None
    updated_at: Optional[str] = None
    data: dict
    client_connect_user_id: Optional[int] = None
    date_of_birth: Optional[str] = None
    first_name: Optional[str] = None
    initials: Optional[str] = None
    is_matter_client: Optional[bool] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    name: Optional[str] = None
    prefix: Optional[str] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    title: Optional[str] = None
    type: Optional[str] = None
