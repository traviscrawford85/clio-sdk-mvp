# clio_sdk/services/statute_sync_db_service.py

import logging

from fastapi import HTTPException
from sqlalchemy.orm import Session

from clio.database.repository import get_matter_by_id, upsert_matter
from clio_sdk.calculators.statute import compute_limitations_date
from clio_sdk.client import ClioClient
from clio_sdk.interfaces.i_statute_sync_db_service import IStatuteSyncDbService
from clio_sdk.unified_models.statute import StatuteSyncResult

logger = logging.getLogger(__name__)


class StatuteSyncDbService(IStatuteSyncDbService):
    async def sync_statute_of_limitations_db(
        self, matter_id: int, db: Session
    ) -> StatuteSyncResult:
        # Step 1: Attempt local DB fetch
        local_matter = get_matter_by_id(db, matter_id)
        if local_matter:
            logger.info(f"Local matter found: {matter_id}")
            incident_date = local_matter.JSON.get("incident_date")
            statute_due = local_matter.JSON.get("statute_due")
        else:
            logger.info(f"Fetching matter from Clio: {matter_id}")
            clio = ClioClient()
            matter = await clio.get(
                f"/matters/{matter_id}.json",
                params={
                    "fields": "statute_of_limitations{id,due_at},custom_field_values{id,value,custom_field}"
                },
            )
            db_matter = upsert_matter(db, matter)
            incident_date = next(
                (
                    f.get("value")
                    for f in matter.get("custom_field_values", [])
                    if f.get("custom_field", {}).get("name") == "Date of Incident"
                ),
                None,
            )
            statute_due = matter.get("statute_of_limitations", {}).get("due_at")

        if not incident_date:
            raise HTTPException(status_code=400, detail="Missing Date of Incident")
        if statute_due:
            logger.info("Statute already present. No update needed.")
            return StatuteSyncResult(status="unchanged", statute_due_at=statute_due)

        deadline = compute_limitations_date(incident_date)
        if not deadline:
            raise HTTPException(status_code=422, detail="Invalid incident date")

        clio = ClioClient()
        patch_payload = {
            "statute_of_limitations": {"due_at": deadline}
        }
        await clio.patch(f"/matters/{matter_id}.json", data=patch_payload)
        logger.info(f"Updated statute for matter {matter_id}: {deadline}")
        return StatuteSyncResult(status="updated", statute_due_at=deadline)
