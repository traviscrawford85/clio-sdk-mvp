# app/api/v1/slack_routes.py

from fastapi import APIRouter, Depends
from app.auth.jwt_auth import auth_wrapper
from app.services.slack_service import send_slack_message  # we will make this too
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
router = APIRouter()

@router.post("/slack/send_message")
async def slack_send_message(channel: str, text: str, token_data=Depends(auth_wrapper)):
    result = send_slack_message(channel, text)
    return {"status": "success", "details": result}
