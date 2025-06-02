# app/api/v1/schemas.py

from pydantic import BaseModel
from datetime import date

class UpdateStatuteResponse(BaseModel):
    status: str
    matter_id: int
    date_of_incident: date
    new_statute_due_date: date

class UpdatePayloadModel(BaseModel):
    description: str | None = None
    status: str | None = None
    value: str
    custom_field_id: int | None = None
    custom_field_value_id: int | None = None
    responsible_staff: int | None = None
    close_date: date | None = None
    practice_area: str | None = None
    statute_of_limitations: date | None = None
