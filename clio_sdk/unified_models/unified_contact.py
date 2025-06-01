from datetime import date, datetime
from typing import Any, List, Optional

from pydantic import BaseModel

from .unified_contact import UnifiedContact


class UnifiedContact(BaseModel):
    data: str
    client_connect_user_id: Optional[int] = None
    clio_connect_email: Optional[str] = None
    created_at: Optional[str] = None
    date_of_birth: Optional[str] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    has_clio_for_clients_permission: Optional[bool] = None
    id: Optional[int] = None
    initials: Optional[str] = None
    is_bill_recipient: Optional[bool] = None
    is_client: Optional[bool] = None
    is_clio_for_client_user: Optional[bool] = None
    is_co_counsel: Optional[bool] = None
    last_name: Optional[str] = None
    ledes_client_id: Optional[str] = None
    locked_clio_connect_email: Optional[bool] = None
    middle_name: Optional[str] = None
    name: Optional[str] = None
    prefix: Optional[str] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    sales_tax_number: Optional[str] = None
    secondary_email_address: Optional[str] = None
    secondary_phone_number: Optional[str] = None
    title: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None
