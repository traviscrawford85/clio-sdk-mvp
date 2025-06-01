# app/lifecycle/webhook_lifecycle.py

from fastapi import FastAPI

from clio.api.routes.webhooks import register_clio_webhook
from clio.database.db import SessionLocal
from clio.database.models import ClioToken


def init_webhook_registration(app: FastAPI):
    @app.on_event("startup")
    async def register_webhook():
        print("🔔 Registering Clio webhook...")

        # Retrieve token from your local SQLite token table
        db = SessionLocal()
        token = db.query(ClioToken).first()
        db.close()

        if not token or getattr(token, "access_token", None) is None:
            print("❌ No access token available for webhook registration.")
            return

        # Determine the correct access token string
        access_token = token.access_token.value if hasattr(token.access_token, "value") else token.access_token
        if not isinstance(access_token, str) or not access_token:
            print("❌ Access token is not a valid string.")
            return

        register_clio_webhook(
            callback_url="https://e2bc-69-255-203-57.ngrok-free.app/webhooks/clio",
            event_types=["matter.create", "matter.update"],
            access_token=access_token
        )
