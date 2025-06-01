#!/usr/bin/env python3
# copilot-enabled: true
# purpose: Used by GitHub Copilot for code refactoring, generation, or maintenance

import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API = "https://api.github.com"

assert GITHUB_TOKEN, "❌ GITHUB_TOKEN not set in environment."

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

def check_auth():
    print("🔍 Verifying token permissions...")
    response = requests.get(f"{GITHUB_API}/user", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Authenticated as {data['login']}")
    else:
        print(f"❌ Failed to authenticate: {response.status_code} - {response.text}")
        return

    scopes = response.headers.get("X-OAuth-Scopes", "")
    print(f"🔐 Token scopes: {scopes}")
    missing_scopes = [scope for scope in ["repo", "workflow", "write:discussion", "read:user", "user:email"]
                      if scope not in scopes]
    if missing_scopes:
        print(f"⚠️ Missing recommended scopes: {', '.join(missing_scopes)}")
    else:
        print("✅ All recommended scopes are present.")

if __name__ == "__main__":
    check_auth()
