import http.server
import os
import socketserver
import webbrowser
from datetime import datetime, timedelta
from urllib.parse import parse_qs, urlparse

import httpx
from dotenv import load_dotenv

from clio.database.db import engine
from clio.database.init_db import init_db
from clio.database.models import Base
from clio.token_store import store_tokens

load_dotenv()

PORT = 8001
CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")
REDIRECT_URI = os.getenv("CLIO_REDIRECT_URI")
TOKEN_URL = os.getenv("CLIO_TOKEN_URL", "https://app.clio.com/oauth/token")
MAX_RETRIES = 3

assert CLIENT_ID and CLIENT_SECRET and REDIRECT_URI, "❌ Missing OAuth env vars"

# Step 1: Ensure database is initialized
init_db()


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def request_tokens_with_retry(code: str) -> dict:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"🔁 Attempt {attempt} to fetch tokens...")
            resp = httpx.post(
                TOKEN_URL,
                data={
                    "grant_type": "authorization_code",
                    "client_id": CLIENT_ID,
                    "client_secret": CLIENT_SECRET,
                    "redirect_uri": REDIRECT_URI,
                    "code": code,
                },
                headers={"Accept": "application/json"},
            )
            resp.raise_for_status()
            return resp.json()
        except httpx.RequestError as e:
            print(f"⚠️ Network error during attempt {attempt}: {e}")
        except httpx.HTTPStatusError as e:
            print(f"❌ HTTP error: {e.response.status_code} - {e.response.text}")
            break  # Don't retry on HTTP errors

    raise Exception("🚫 Failed to fetch tokens after multiple attempts.")


class OAuthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"🔍 Received path: {self.path}")
        query = parse_qs(urlparse(self.path).query)
        code = query.get("code", [None])[0]

        if not code:
            self.send_error(400, "Missing code in callback.")
            return

        try:
            tokens = request_tokens_with_retry(code)
            store_tokens(
                access_token=tokens["access_token"],
                refresh_token=tokens["refresh_token"],
                expires_in=tokens["expires_in"],
            )

            access_token = tokens.get("access_token")
            refresh_token = tokens.get("refresh_token")
            print(
                "🔐 Access Token:",
                (access_token[:8] + "...") if access_token else "None",
            )
            print(
                "♻️ Refresh Token:",
                (refresh_token[:8] + "...") if refresh_token else "None",
            )
            print("⏳ Expires In:", tokens.get("expires_in"), "seconds")

            self.send_response(200)
            self.end_headers()
            self.wfile.write(
                "✅ Clio Authorization Complete! You can close this tab.".encode(
                    "utf-8"
                )
            )
            print("✅ OAuth token saved and ready for use in API calls.")

        except Exception as e:
            self.send_error(500, f"OAuth flow failed: {e}")
            raise


def run_oauth_flow():
    auth_url = (
        f"https://app.clio.com/oauth/authorize"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=all"
    )
    print("🌐 Opening browser for Clio OAuth...")
    webbrowser.open(auth_url)

    with ReusableTCPServer(("127.0.0.1", PORT), OAuthHandler) as httpd:
        print(f"⏳ Waiting for OAuth callback on port {PORT}...")
        httpd.handle_request()


if __name__ == "__main__":
    run_oauth_flow()
