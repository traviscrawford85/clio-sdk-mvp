# clio/token_store.py

import os
from datetime import datetime, timedelta, timezone

# clio/token_store.py
import requests

from clio.database.db import SessionLocal
from clio.database.models import ClioToken


def refresh_clio_token_if_needed(refresh_data: dict) -> dict:
    CLIO_TOKEN_URL = os.getenv("CLIO_TOKEN_URL", "https://app.clio.com/oauth/token")
    CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")

    response = requests.post(
        CLIO_TOKEN_URL,
        data={
            "grant_type": "refresh_token",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "refresh_token": refresh_data["refresh_token"],
        },
        headers={"Accept": "application/json"}
    )

    if response.status_code != 200:
        raise Exception(f"❌ Token refresh failed: {response.text}")

    return response.json()


def store_tokens(access_token: str, refresh_token: str, expires_in: int):
    session = SessionLocal()
    try:
        expires_at = datetime.now(timezone.utc) + timedelta(seconds=expires_in)
        token = ClioToken(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_at=expires_at,
        )
        session.merge(token)
        session.commit()
        print("💾 Token stored in DB")
        print("🔐 Access Token:", access_token)
        print("♻️ Refresh Token:", refresh_token)
        print("⏳ Expires At:", expires_at.isoformat())
    finally:
        session.close()



def get_stored_token_data() -> dict | None:
    session = SessionLocal()
    try:
        token = session.query(ClioToken).order_by(ClioToken.expires_at.desc()).first()
        if token is None or token.expires_at is None:
            return None
        return {
            "access_token": token.access_token,
            "refresh_token": token.refresh_token,
            "expires_at": int(token.expires_at.timestamp())
        }
    finally:
        session.close()

def get_access_token() -> str:
    session = SessionLocal()
    try:
        token = session.query(ClioToken).order_by(ClioToken.expires_at.desc()).first()

        if token is None or token.expires_at is None:
            raise Exception("❌ No valid Clio token found. Please complete OAuth.")

        print("📦 Access token retrieved from database:")
        print(f"🔑 Token: {token.access_token}")
        print(f"⏳ Expires at: {token.expires_at.isoformat()}")
        print(f"♻️ Refresh token: {token.refresh_token}")
        
        now_utc = datetime.now(timezone.utc)
        expires_at_utc = token.expires_at.replace(tzinfo=timezone.utc)

        if expires_at_utc < now_utc:
            print("🔁 Token expired. Refreshing...")
            refreshed = refresh_clio_token_if_needed({
                "refresh_token": token.refresh_token,
                "expires_at": int(token.expires_at.timestamp())
            })
            store_tokens(
                access_token=refreshed["access_token"],
                refresh_token=refreshed["refresh_token"],
                expires_in=refreshed["expires_in"],
            )
            return refreshed["access_token"]

        return str(token.access_token)
    finally:
        session.close()
