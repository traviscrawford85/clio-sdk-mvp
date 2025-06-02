import json
import requests
from app.auth.token_store import get_access_token
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK

def register_clio_webhooks():
    print("🚀 App is starting up, registering webhooks...")

    access_token = get_access_token()
    clio_sdk = ClioSDK(access_token=access_token)

    webhook_topics = [
        {"topic": "matter.updated", "target": "https://4688-69-255-203-57.ngrok-free.app/api/v1/webhooks/clio"},
        {"topic": "task.created", "target": "https://4688-69-255-203-57.ngrok-free.app/api/v1/webhooks/clio"},
        {"topic": "task.updated", "target": "https://4688-69-255-203-57.ngrok-free.app/api/v1/webhooks/clio"},
        {"topic": "activity.created", "target": "https://4688-69-255-203-57.ngrok-free.app/api/v1/webhooks/clio"},
        {"topic": "activity.updated", "target": "https://4688-69-255-203-57.ngrok-free.app/api/v1/webhooks/clio"},
    ]

    for webhook in webhook_topics:
        model, event = webhook["topic"].split('.')
        # Use the ClioSDK's webhooks API
        response = clio_sdk.webhooks.create_webhook(
            callback_url=webhook["target"],
            event_types=[webhook["topic"]]
        )
        if hasattr(response, 'status_code') and (response.status_code == 201 or response.status_code == 200):
            print(f"✅ Successfully registered webhook for topic {webhook['topic']}")
            print(getattr(response, 'json', lambda: response)())
        else:
            print(f"❌ Failed to create webhook for topic {webhook['topic']}")
            print(f"Status code: {getattr(response, 'status_code', 'N/A')}")
            print(f"Response: {getattr(response, 'text', str(response))}")
