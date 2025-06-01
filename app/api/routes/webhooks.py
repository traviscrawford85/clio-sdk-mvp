# app/api/routes/webhooks.py

import logging
from typing import List

import requests
from fastapi import APIRouter, HTTPException, Request

from clio_sdk.calculators.statute import compute_limitations_date
from clio_sdk.client import ClioClient

router = APIRouter(prefix="/webhooks")
logger = logging.getLogger(__name__)

@router.post("/clio")
async def handle_clio_webhook(request: Request):
    body = await request.json()
    event_type = body.get("event_type")
    matter_id = body.get("data", {}).get("id")

    if not matter_id or not event_type:
        raise HTTPException(status_code=400, detail="Invalid webhook payload")

    logger.info(f"Received Clio webhook: {event_type} for matter {matter_id}")

    if event_type == "matter.create":
        # Handle using shared logic
        return await handle_matter_created(matter_id)

    return {"status": "ignored"}

async def handle_matter_created(matter_id: int):
    clio = ClioClient()
    matter = await clio.get(
        f"/matters/{matter_id}.json",
        params={"fields": "statute_of_limitations{id,due_at},custom_field_values{field_name,value,id}"}
    )

    incident = next((f for f in matter.get("custom_field_values", [])
                     if f.get("field_name") == "Date of Incident"), None)

    if not incident:
        logger.warning("Date of Incident missing.")
        return {"status": "ignored"}

    if matter.get("statute_of_limitations", {}).get("due_at"):
        return {"status": "unchanged"}

    deadline = compute_limitations_date(incident.get("value"))
    await clio.patch(f"/matters/{matter_id}.json", data={"statute_of_limitations": {"due_at": deadline}})
    return {"status": "updated", "statute_due_at": deadline}

def register_clio_webhook(callback_url: str, event_types: List[str], access_token: str):
    """
    Register a webhook with Clio's API.

    Args:
        callback_url (str): The endpoint Clio should send event payloads to.
        event_types (List[str]): A list of event types to subscribe to.
        access_token (str): OAuth access token for authenticating with Clio.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "data": {
            "callback_url": callback_url,
            "event_types": event_types
        }
    }
    response = requests.post("https://app.clio.com/api/v4/webhooks", json=data, headers=headers)

    if response.status_code == 201:
        print("✅ Webhook registered successfully.")
    else:
        print(f"❌ Failed to register webhook: {response.status_code} {response.text}")