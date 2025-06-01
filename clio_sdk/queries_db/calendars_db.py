# clio_sdk/queries_db/calendars.py
from core.database.db import SessionLocal
from core.database.legacy_models import CalendarEntries
from sqlalchemy.orm import Session


def list_calendar_entries_db(start_date: str = None, end_date: str = None):
    with SessionLocal() as db:
        query = db.query(CalendarEntries)
        if start_date and end_date:
            query = query.filter(CalendarEntries.Start >= start_date, CalendarEntries.End <= end_date)
        return query.all()