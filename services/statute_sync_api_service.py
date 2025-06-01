# clio_sdk/services/statute_sync_service.py

import logging

from fastapi import HTTPException

from clio_sdk.calculators.statute import compute_limitations_date
from clio_sdk.client import ClioClient
from clio_sdk.constants import CustomFieldNames
from clio_sdk.interfaces.i_statute_sync_api_service import IStatuteSyncApiService

logger = logging.getLogger(__name__)

def extract_incident_field(custom_fields: list) -> tuple:
    for field in custom_fields:
        if field.get("field_name") == CustomFieldNames.INCIDENT_DATE:
            return field.get("value"), field.get("id")
    return None, None

def build_patch_payload(incident_date: str, custom_field_id: str, deadline: str) -> dict:
    return {
        "custom_field_values": [
            {
                "id": custom_field_id,
                "value": incident_date,
            }
        ],
        "statute_of_limitations": {
            "due_at": deadline
        }
    }

class StatuteSyncApiService(IStatuteSyncApiService):
    async def sync_statute_to_matter(self, matter_id: int) -> dict:
        """
        Computes statute of limitations and PATCHes the matter with the computed date.
        """
        logger.info(f"Syncing statute for matter {matter_id}")
        clio = ClioClient()
        matter = await clio.get(f"/matters/{matter_id}")
        custom_fields = matter.get("custom_field_values", [])
        statute = matter.get("statute_of_limitations", {})

        incident_date, custom_field_id = extract_incident_field(custom_fields)

        if not incident_date:
            all_fields = await clio.get("/custom_fields.json", params={"parent_type": "Matter"})
            field_def = next(
                (f for f in all_fields.get("data", []) if f.get("name") == CustomFieldNames.INCIDENT_DATE),
                None
            )
            if not field_def:
                logger.error("Custom field definition for 'Date of Incident' not found.")
                raise HTTPException(
                    status_code=400,
                    detail=f"Custom field definition for '{CustomFieldNames.INCIDENT_DATE}' not found."
                )
            custom_field_id = field_def.get("id")
            logger.error("'Date of Incident' custom field not populated on matter.")
            raise HTTPException(
                status_code=400,
                detail=f"'{CustomFieldNames.INCIDENT_DATE}' custom field not populated on matter."
            )

        if not incident_date:
            logger.error("Incident date is missing from matter.")
            raise HTTPException(status_code=400, detail="Incident date is missing")

        deadline = compute_limitations_date(incident_date)
        if not deadline:
            logger.error("Invalid incident date format: {incident_date}")
            raise HTTPException(status_code=422, detail="Invalid incident date format")

        patch_payload = build_patch_payload(incident_date, custom_field_id, deadline)

        updated = await clio.patch(f"/matters/{matter_id}", patch_payload)
        logger.info(f"Successfully updated statute for matter {matter_id}: {deadline}")
        return updated
