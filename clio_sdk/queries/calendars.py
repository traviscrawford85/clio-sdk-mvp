# clio_sdk/queries/calendars.py
from typing import Optional

from clio_sdk.client import ClioClient


async def list_calendar_entries(start_date: Optional[str] = None, end_date: Optional[str] = None) -> list[dict]:
    clio = ClioClient()
    params = {}
    if start_date:
        params["start_date"] = start_date
    if end_date:
        params["end_date"] = end_date
    return await clio.get("/calendar_entries.json", params=params)
