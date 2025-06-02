# File: app/api/v1/slack/commands.py

from fastapi import APIRouter
from clio_slack_agent_mvp.slack_mvp.handlers.commands import handle_slack_command

router = APIRouter()

@router.post("/commands")
async def slack_commands(request):
    return await handle_slack_command(request)
