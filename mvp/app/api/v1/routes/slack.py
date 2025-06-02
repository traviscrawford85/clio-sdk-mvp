from fastapi import APIRouter
from app.api.v1.slack.routes import router as send_message_router
from app.api.v1.slack.webhooks import router as webhook_router
from app.api.v1.slack.commands import router as commands_router

router = APIRouter()
router.include_router(send_message_router)
router.include_router(webhook_router)
router.include_router(commands_router)

# Example Slack route (expand as needed)
# @router.post("/event")
# async def slack_event_handler(payload: dict):
#     # Handle Slack event here
#     return {"status": "received"}

# Add your Slack API endpoints here as your app grows.
