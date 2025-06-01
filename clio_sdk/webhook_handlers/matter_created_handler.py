# clio_sdk/webhook_handlers/matter_created_handler.py
import logging

import httpx
from fastapi import APIRouter, HTTPException, Request

from clio_sdk.calculators.statute import compute_limitations_date
from clio_sdk.client import ClioClient

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/webhook/matter.created")
async def handle_matter_created_webhook(request: Request):
    body = await request.json()
    matter_id = body.get("data", {}).get("id")
    if not matter_id:
        raise HTTPException(status_code=400, detail="Missing matter ID in webhook payload")

    logger.info(f"Webhook received for new matter ID: {matter_id}")

    clio = ClioClient()

    # Step 1: Get the matter with filtered custom_field_values
    matter = await clio.get(
        f"/matters/{matter_id}.json",
        params={
            "fields": "statute_of_limitations{id,name,status,description,due_at},custom_field_values{id,field_name,value}"
        }
    )

    custom_fields = matter.get("custom_field_values", [])
    statute_data = matter.get("statute_of_limitations", {})

    # Step 2: Check if Date of Incident is present and statute due_at is not already set
    incident_date = None
    incident_field_id = None
    for field in custom_fields:
        if field.get("field_name") == "Date of Incident":
            incident_date = field.get("value")
            incident_field_id = field.get("id")
            break

    if not incident_date:
        logger.warning("Date of Incident not found in custom fields.")
        return {"status": "ignored", "reason": "Date of Incident missing"}

    if statute_data.get("due_at"):
        logger.info("Statute of limitations already set. No action needed.")
        return {"status": "ignored", "reason": "Statute already computed"}

    # Step 3: Compute statute date
    deadline = compute_limitations_date(incident_date)
    if not deadline:
        raise HTTPException(status_code=422, detail="Invalid date format in Date of Incident")

    # Step 4: Patch matter with statute_of_limitations
    patch_payload = {
        "statute_of_limitations": {"due_at": deadline}
    }
    await clio.patch(f"/matters/{matter_id}.json", data=patch_payload)

    logger.info(f"Statute of limitations computed and updated: {deadline}")
    return {"status": "updated", "statute_due_at": deadline}
