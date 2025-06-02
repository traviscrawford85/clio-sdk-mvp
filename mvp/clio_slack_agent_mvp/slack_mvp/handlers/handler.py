# app/webhooks/slack_event_handlers/handler.py
import os
from slack_bolt.async_app import AsyncApp
from slack_bolt.adapter.socket_mode.aiohttp import AsyncSocketModeHandler
from ledyard_ai.context import get_llm_agent

slack_app = AsyncApp(token=os.getenv("SLACK_BOT_TOKEN"))
agent = get_llm_agent()

@slack_app.command("/ask-clio")
async def handle_ask_clio(ack, respond, command):
    await ack()
    prompt = command.get("text", "").strip()

    if not prompt:
        await respond("❗ Please enter a question, like `/ask-clio How do I...`")
        return

    try:
        result = await agent.chat(prompt)
        await respond(f"🧠 *LLM says:*\n{result}")
    except Exception as e:
        await respond(f"⚠️ Failed to get a response: {str(e)}")

async def start_async_handler():
    handler = AsyncSocketModeHandler(slack_app, app_token=os.getenv("SLACK_APP_TOKEN"))
    await handler.start_async()