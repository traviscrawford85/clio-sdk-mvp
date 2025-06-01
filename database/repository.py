# clio/database/repository.py
import json
from typing import Optional

from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.orm import Session

from clio.database.legacy_models import Matters


def upsert_matter(db: Session, clio_data: dict):
    """
    Upsert a Clio matter into the local database.
    Stores both parsed and raw JSON content.
    """
    stmt = insert(Matters).values(
        ID=clio_data["id"],
        Status=clio_data.get("status"),
        Client=clio_data.get("client", {}).get("id"),
        Description=clio_data.get("description"),
        Display_Number=clio_data.get("display_number"),
        JSON=json.dumps(clio_data),
    )
    stmt = stmt.on_conflict_do_update(
        index_elements=[Matters.ID],
        set_={
            "Status": stmt.excluded.Status,
            "Client": stmt.excluded.Client,
            "Description": stmt.excluded.Description,
            "Display_Number": stmt.excluded.Display_Number,
            "JSON": stmt.excluded.JSON,
        },
    )
    db.execute(stmt)
    db.commit()


def get_matter_by_id(db: Session, matter_id: int) -> Optional[Matters]:
    return db.query(Matters).filter(Matters.ID == matter_id).first()
