from slack_sdk.web.async_client import AsyncWebClient
from ledyard_slack.blocks.summary_block import make_summary_block
from ledyard_ai.context import get_llm_agent

async def summarize_channel_action(ack, body: dict, client: AsyncWebClient):
    ack()
    channel_id = body["channel"]["id"]

    try:
        history = await client.conversations_history(channel=channel_id, limit=50)
        messages_list = history.get("messages") or []
        messages = [msg["text"] for msg in messages_list if "text" in msg]
        if not messages:
            await client.chat_postMessage(channel=channel_id, text="No recent messages to summarize.")
            return

        agent = get_llm_agent()
        user_input = "Summarize the following Slack channel:\n\n" + "\n".join(messages)
        summary = await agent.chat(user_input)

        await client.chat_postMessage(
            channel=channel_id,
            blocks=make_summary_block(summary),
            text="🧠 Here's your channel summary:"
        )
    except Exception as e:
        await client.chat_postMessage(
            channel=channel_id,
            text=f"⚠️ An error occurred during summarization: {str(e)}"
        )
