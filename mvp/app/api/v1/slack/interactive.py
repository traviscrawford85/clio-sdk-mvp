from fastapi import APIRouter
from clio_slack_agent_mvp.slack_mvp.handlers.interactions import handle_interactions

router = APIRouter()


@router.post("/interactive")
async def interactive_endpoint(request):
    return await handle_interactions(request)