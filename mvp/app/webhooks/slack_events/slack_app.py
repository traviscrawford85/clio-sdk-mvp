from slack_bolt import App, Ack, Respond
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from app.auth.token_store import get_access_token
from celery import chain
from app.celery_tasks.clio_tasks import sync_tasks_from_clio
from clio_sdk_mvp.services.celery_task_queue_service import CeleryTaskQueueService

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

if not SLACK_BOT_TOKEN:
    raise RuntimeError("SLACK_BOT_TOKEN environment variable is required for Slack Bolt app.")

slack_app = App(token=SLACK_BOT_TOKEN)
celery_queue = CeleryTaskQueueService()

# Export the canonical Slack Bolt app for import in main.py
app = slack_app

@slack_app.event("app_mention")
def handle_mention(event, say):
    user = event["user"]
    say(f"Hi <@{user}>, how can I help?")

@slack_app.event("message")
def handle_message(event, say):
    if "hello" in event.get("text", "").lower():
        say("Hey there! 👋")

@slack_app.command("/create_task")
def handle_create_task(ack: Ack, respond: Respond, command):
    ack()  # Acknowledge command immediately

    text = command.get("text", "")
    parts = text.split(" ", 1)
    if not parts:
        respond("❌ Usage: /create_task [title] [optional matter_id]")
        return

    title = parts[0]
    matter_id = parts[1] if len(parts) > 1 else None

    try:
        # Use ClioSDK to create a task
        access_token = get_access_token()
        clio_sdk = ClioSDK(access_token=access_token)
        # Example: Replace with actual SDK call
        # task = clio_sdk.tasks.create_task(title=title, matter_id=matter_id)
        task_id = "fake-task-id-1234"  # Replace with actual response
        respond(f"✅ Task '{title}' created with ID `{task_id}`.")
    except Exception as e:
        respond(f"❌ Failed to create task: {str(e)}")

@slack_app.command("/task-list")
def handle_task_list(ack: Ack, respond: Respond, command):
    ack()
    try:
        access_token = get_access_token()
        clio_sdk = ClioSDK(access_token=access_token)
        # Example: Fetch tasks for the user (customize as needed)
        user_id = command.get("user_id")
        # You may want to filter by assignee_id=user_id if your SDK supports it
        tasks = clio_sdk.tasks.list_tasks()  # Add filtering if available
        if not tasks:
            respond("🎯 No tasks assigned to you at the moment.")
            return
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{task.get('name', 'No Name')}* (Due: {task.get('due_at', 'No Due Date')})"
                }
            }
            for task in tasks[:10]
        ]
        respond(blocks=blocks)
    except Exception as e:
        respond(f"❌ Failed to fetch tasks: {str(e)}")

@slack_app.command("/find-matter")
def handle_find_matter(ack: Ack, respond: Respond, command):
    ack()
    try:
        access_token = get_access_token()
        clio_sdk = ClioSDK(access_token=access_token)
        matters = clio_sdk.matters.list_matters()
        if not matters:
            respond("📁 No matters found.")
            return
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{matter.get('display_number', 'N/A')}* - {matter.get('name', 'No Name')}"
                }
            }
            for matter in matters[:10]
        ]
        respond(blocks=blocks)
    except Exception as e:
        respond(f"❌ Failed to fetch matters: {str(e)}")

@slack_app.command("/longtask")
def handle_longtask(ack, respond, command):
    ack("Processing your request...")  # Immediate response to Slack

    # Compose a chain of Celery tasks
    task_chain = chain(
        first_task.s(command["text"]),
        second_task.s(command["user_id"])
    )
    task_chain.apply_async()

@slack_app.command("/sync-tasks")
def handle_sync_tasks(ack: Ack, respond: Respond, command):
    ack("🔄 Syncing tasks from Clio in the background...")
    celery_queue.enqueue("app.celery_tasks.clio_tasks.sync_tasks_from_clio")
    respond("✅ Task sync started. You'll be notified when it's done.")

def get_socket_mode_handler():
    return SocketModeHandler(slack_app, SLACK_APP_TOKEN)
