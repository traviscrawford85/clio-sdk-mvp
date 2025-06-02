# OAuth login redirect and flow handling
# clio-integration/auth/oauth_flow.py

import os
import requests

# --- Clio OAuth helpers ---
def build_clio_auth_url(state: str = "default") -> str:
    redirect_uri = os.getenv("CLIO_REDIRECT_URI")
    return (
        f"https://app.clio.com/oauth/authorize?"
        f"client_id={os.getenv('CLIO_CLIENT_ID')}&"
        f"redirect_uri={redirect_uri}&"
        f"response_type=code&"
        f"scope=all&"
        f"state={state}"
    )

def exchange_clio_code_for_tokens(code: str) -> dict:
    payload = {
        "grant_type": "authorization_code",
        "client_id": os.getenv("CLIO_CLIENT_ID"),
        "client_secret": os.getenv("CLIO_CLIENT_SECRET"),
        "redirect_uri": os.getenv("CLIO_REDIRECT_URI"),
        "code": code,
    }
    token_response = requests.post("https://app.clio.com/oauth/token", data=payload)
    token_response.raise_for_status()
    tokens = token_response.json()
    tokens["expires_at"] = int(os.environ.get("EPOCH", 0)) + tokens.get("expires_in", 3600)
    return tokens

# --- QBO OAuth helpers ---
def build_qbo_auth_url(state: str = "default") -> str:
    redirect_uri = os.getenv("QBO_REDIRECT_URI")
    return (
        f"https://appcenter.intuit.com/connect/oauth2?"
        f"client_id={os.getenv('QBO_CLIENT_ID')}&"
        f"redirect_uri={redirect_uri}&"
        f"response_type=code&"
        f"scope=com.intuit.quickbooks.accounting&"
        f"state={state}"
    )

def exchange_qbo_code_for_tokens(code: str) -> dict:
    payload = {
        "grant_type": "authorization_code",
        "client_id": os.getenv("QBO_CLIENT_ID"),
        "client_secret": os.getenv("QBO_CLIENT_SECRET"),
        "redirect_uri": os.getenv("QBO_REDIRECT_URI"),
        "code": code,
    }
    token_response = requests.post("https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer", data=payload)
    token_response.raise_for_status()
    tokens = token_response.json()
    tokens["expires_at"] = int(os.environ.get("EPOCH", 0)) + tokens.get("expires_in", 3600)
    return tokens



