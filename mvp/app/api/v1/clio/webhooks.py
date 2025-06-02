# app/api/v1/clio/webhooks.py
from fastapi import APIRouter, Request
from app.core.webhook_verification import verify_clio_webhook
from app.core.config import settings
import logging
from app.auth.token_store import get_access_token  # Adjusted import for your project structure
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_slack_agent_mvp.slack_mvp.handlers.commands import handle_slack_command

router = APIRouter()

logger = logging.getLogger("webhooks.clio")
logging.basicConfig(level=logging.INFO)

@router.post("/clio")
async def clio_webhook(request: Request):
    payload = await request.body()
    signature = request.headers.get("X-Signature")

    if signature:
        if not verify_clio_webhook(payload, signature, settings.CLIO_CLIENT_SECRET):
            logger.warning("❌ Invalid Clio webhook signature")
            return {"message": "Invalid signature"}, 401
    else:
        logger.warning("❌ Missing X-Signature header from Clio — proceeding without verification.")

    logger.info("✅ Received valid webhook from Clio")
    return {"message": "Webhook received successfully"}

def register_clio_webhook(callback_url: str, event_types: list[str]):
    """
    Register a webhook with Clio's API using ClioSDK.
    """
    clio_sdk = ClioSDK(access_token=get_access_token())
    response = clio_sdk.webhooks.create_webhook(callback_url=callback_url, event_types=event_types)
    if response.status_code == 201:
        logger.info("✅ Webhook registered successfully.")
    else:
        logger.error(f"❌ Failed to register webhook: {response.status_code} {response.text}")
