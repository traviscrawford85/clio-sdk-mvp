from typing import Optional

from clio_sdk.adapter_factory.transformer import register_transformer
from clio_sdk.unified_models.calendar import Calendar as DomainCalendar


def transform_calendar_fields(data: dict, context: Optional[dict] = None) -> dict:
    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "color": data.get("color"),
        "created_at": data.get("created_at"),
        "etag": data.get("etag"),
        "updated_at": data.get("updated_at"),
        "data": data.get("data"),
        "all_day": data.get("all_day"),
        "calendar_owner_id": data.get("calendar_owner_id"),
        "court_rule": data.get("court_rule"),
        "description": data.get("description"),
        "end_at": data.get("end_at"),
        "location": data.get("location"),
        "parent_calendar_entry_id": data.get("parent_calendar_entry_id"),
        "permission": data.get("permission"),
        "recurrence_rule": data.get("recurrence_rule"),
        "start_at": data.get("start_at"),
        "start_at_time_zone": data.get("start_at_time_zone"),
        "summary": data.get("summary"),
        "time_entries_count": data.get("time_entries_count"),
        "light_color": data.get("light_color"),
        "visible": data.get("visible"),
        "court_rules_default_calendar": data.get("court_rules_default_calendar"),
        "source": data.get("source"),
        "type": data.get("type"),
    }


register_transformer("calendar", transform_calendar_fields)
