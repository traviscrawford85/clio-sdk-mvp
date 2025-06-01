# clio_sdk/queries_db/contacts.py
from core.database.db import SessionLocal
from core.database.legacy_models import Contacts
from sqlalchemy.orm import Session


def get_contact_by_id_db(contact_id: int):
    with SessionLocal() as db:
        return db.query(Contacts).filter(Contacts.ID == contact_id).first()


def list_contacts_db():
    with SessionLocal() as db:
        return db.query(Contacts).all()