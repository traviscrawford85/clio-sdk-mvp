import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
def send_slack_message(text: str):
    slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not slack_webhook_url:
        raise ValueError("Missing SLACK_WEBHOOK_URL in environment variables.")

    payload = {
        "text": text
    }

    response = requests.post(slack_webhook_url, json=payload)

    if response.status_code != 200:
        raise Exception(f"Slack webhook error: {response.status_code} {response.text}")

    print("✅ Sent Slack notification.")
