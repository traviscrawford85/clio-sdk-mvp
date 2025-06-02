from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import JSONResponse
from app.core.webhook_verification import verify_slack_webhook
import os
import logging
import json

router = APIRouter()

logger = logging.getLogger("webhooks.slack")
logging.basicConfig(level=logging.INFO)

SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

@router.post("/slack")
async def slack_webhook(request: Request):
    headers = request.headers
    payload = await request.body()

    timestamp = headers.get("X-Slack-Request-Timestamp")
    signature = headers.get("X-Slack-Signature")

    if not verify_slack_webhook(payload, timestamp, signature, SLACK_SIGNING_SECRET):
        raise HTTPException(status_code=400, detail="Invalid Slack webhook signature.")

    data = await request.json()

    if data.get("type") == "url_verification":
        return {"challenge": data["challenge"]}

    event = data.get("event", {})
    event_type = event.get("type")
    user_id = event.get("user")
    text = event.get("text")
    channel_id = event.get("channel")

    logger.info(f"✅ Slack event received: type={event_type}, user={user_id}, text={text}, channel={channel_id}")

    return {"status": "received", "source": "Slack"}

from clio_slack_agent_mvp.slack_mvp.handlers.commands import handle_find_matter, handle_task_list

COMMAND_DISPATCHER = {
    "/find-matter": handle_find_matter,
    "/task-list": handle_task_list,
}
@router.post("/slack/commands")
async def slack_commands(
    token: str = Form(...),
    team_id: str = Form(...),
    team_domain: str = Form(...),
    channel_id: str = Form(...),
    user_id: str = Form(...),
    command: str = Form(...),
    text: str = Form(...)
):


    handler = COMMAND_DISPATCHER.get(command)

    if handler:
        return handler( user_id, text)
    else:
        return JSONResponse(content={"text": f"❓ Unknown command: {command}"})



@router.post("/slack/interactive")
async def slack_interactive(payload: str = Form(...)):
    payload_data = json.loads(payload)

    # Example: Log the button click
    action_id = payload_data['actions'][0]['action_id']
    user_id = payload_data['user']['id']

    if action_id == "say_hi_button":
        return {
            "text": f"👋 Hi there, <@{user_id}>! Thanks for clicking!"
        }
    elif action_id == "dismiss_button":
        return {
            "text": f"🚪 Dismissed by <@{user_id}>!"
        }

    return {"text": "Unknown action"}