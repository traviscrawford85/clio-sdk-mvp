from fastapi import APIRouter, Request, HTTPException
from app.core.webhook_verification import verify_qbo_webhook
from app.core.config import settings
import logging

router = APIRouter()

logger = logging.getLogger("webhooks.qbo")
logging.basicConfig(level=logging.INFO)

@router.post("")
async def qbo_webhook(request: Request):
    payload = await request.json()

    if not verify_qbo_webhook(payload, settings.QBO_VERIFICATION_TOKEN):
        logger.warning("❌ QBO webhook verification failed")
        raise HTTPException(status_code=401, detail="Invalid QuickBooks webhook verification token")

    logger.info("✅ Valid QuickBooks webhook received: %s", payload)
    return {"message": "Webhook received"}
