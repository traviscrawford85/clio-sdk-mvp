import logging

from fastapi import HTTPException

from clio_sdk.calculators.statute import compute_limitations_date
from clio_sdk.client import ClioClient
from clio_sdk.constants import CustomFieldNames
from clio_sdk.interfaces.i_statute_service import IStatuteService

logger = logging.getLogger(__name__)

class StatuteService(IStatuteService):
    async def compute_statute_for_matter(self, matter_id: int) -> str:
        logger.info(f"🔍 Fetching matter {matter_id}")
        clio = ClioClient()
        matter = await clio.get(f"/matters/{matter_id}")
        logger.debug(f"📄 Matter data: {matter}")

        # 1. Get all custom field definitions
        custom_fields_resp = await clio.get("/custom_fields.json?fields=id,name")
        custom_fields = custom_fields_resp.get("custom_fields", [])
        logger.debug(f"Custom field definitions: {custom_fields}")

        # 2. Find the definition for "Date of Incident"
        incident_field_def = next(
            (f for f in custom_fields if f.get("name", "").lower() == CustomFieldNames.INCIDENT_DATE.lower()),
            None
        )
        if not incident_field_def:
            logger.error("Custom field definition for 'Date of Incident' not found.")
            raise HTTPException(status_code=400, detail=f"Custom field '{CustomFieldNames.INCIDENT_DATE}' not found")
        incident_field_id = incident_field_def["id"]

        # 3. Find the value for that field in the matter
        custom_fields_values = matter.get("custom_field_values", [])
        logger.debug(f"Custom field values: {custom_fields_values}")
        incident_field_value = next(
            (v for v in custom_fields_values if v.get("custom_field") == incident_field_id or v.get("custom_field_id") == incident_field_id),
            None
        )
        if not incident_field_value:
            logger.error("Custom field value for 'Date of Incident' not found in matter.")
            raise HTTPException(status_code=400, detail="Incident date is missing")
        date_of_incident = incident_field_value.get("value")
        if not date_of_incident:
            logger.error("Incident date is missing in the custom field value.")
            raise HTTPException(status_code=400, detail="Incident date is missing")

        limitations_date = compute_limitations_date(date_of_incident)
        logger.info(f"Computed statute of limitations date: {limitations_date}")

        if not limitations_date:
            logger.error("Invalid incident date format. Expected YYYY-MM-DD")
            raise HTTPException(status_code=422, detail="Invalid incident date format. Expected YYYY-MM-DD")

        return limitations_date
