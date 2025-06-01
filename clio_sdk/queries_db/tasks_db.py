# clio_sdk/queries_db/tasks.py
from core.database.db import SessionLocal
from core.database.legacy_models import Tasks
from sqlalchemy.orm import Session


def list_tasks_db(matter_id: int = None):
    with SessionLocal() as db:
        query = db.query(Tasks)
        if matter_id:
            query = query.filter(Tasks.Matter == matter_id)
        return query.all()