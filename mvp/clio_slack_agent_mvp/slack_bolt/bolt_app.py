import os
import asyncio
import logging
from typing import Any, Dict

from slack_bolt.async_app import AsyncApp
from slack_bolt.adapter.socket_mode.aiohttp import AsyncSocketModeHandler
from slack_bolt.context.ack import Ack
from slack_sdk.web.async_client import AsyncWebClient

from ledyard_slack.blocks.welcome_block import welcome_blocks
from ledyard_slack.blocks.summary_block import make_summary_block
from ledyard_slack.handlers.summarize import summarize_channel_action
from ledyard_ai.context import get_llm_agent

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("slack_bot.log", mode='a')
    ]
)

app = AsyncApp(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.message("hello")
async def message_hello(message: Dict[str, Any], say):
    await say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )

@app.action("button_click")
async def action_button_click(body: Dict[str, Any], ack: Ack, say):
    await ack()
    await say(f"<@{body['user']['id']}> clicked the button")

@app.action("summarize_channel")
async def handle_summary(ack: Ack, body: Dict[str, Any], client: AsyncWebClient, context: Any):
    await summarize_channel_action(ack, body, client, context)

@app.command("/askllm")
async def handle_askllm_command(ack: Ack, respond, command: Dict[str, Any]):
    await ack()
    user_input = command.get("text", "").strip()
    logging.info(f"Received /askllm prompt: {user_input}")

    if not user_input:
        respond("❗ Please enter a question after the command, like `/askllm How do I...`")
        return

    try:
        agent = get_llm_agent()
        reply = await agent.chat(user_input)
        respond(f"🧠 *LLM says:*\n{reply}")
    except Exception as e:
        logging.error("LLM failed", exc_info=True)
        respond(f"⚠️ LLM failed: {str(e)}")

@app.command("/taskbot")
async def handle_taskbot_command(ack: Ack, respond):
    await ack()
    respond(blocks=welcome_blocks, text="Welcome to the Ledyard Law Task Assistant!")

if __name__ == "__main__":
    handler = AsyncSocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    asyncio.run(handler.start_async())
