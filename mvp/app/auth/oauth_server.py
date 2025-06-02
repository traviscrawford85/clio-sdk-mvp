# OAuth token endpoint
# firm_clio/auth/oauth_server.py

import json
import os
import time

import requests
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse
from app.auth.oauth_flow import (
    build_clio_auth_url, exchange_clio_code_for_tokens,
    build_qbo_auth_url, exchange_qbo_code_for_tokens
)
from app.database.models import ClioToken, QBOToken
from app.database.db import SessionLocal

router = APIRouter()


def build_auth_url(state: str = "default") -> str:
    redirect_uri = os.getenv("CLIO_REDIRECT_URI")
    print(f"🔗 Using redirect_uri: {redirect_uri}")
    return (
        f"https://app.clio.com/oauth/authorize?"
        f"client_id={os.getenv('CLIO_CLIENT_ID')}&"
        f"redirect_uri={redirect_uri}&"
        f"response_type=code&"
        f"scope=all&"
        f"state={state}"
    )


@router.get("/oauth/clio/authorize")
def clio_authorize():
    """Redirect user to Clio's OAuth authorization page."""
    return RedirectResponse(build_clio_auth_url())


@router.get("/oauth/clio/callback")
def clio_callback(code: str):
    """Handle Clio OAuth callback, exchange code for tokens, and store in DB."""
    tokens = exchange_clio_code_for_tokens(code)
    db = SessionLocal()
    db.add(ClioToken(**tokens))
    db.commit()
    db.close()
    return {"status": "Clio tokens stored"}


@router.get("/oauth/qbo/authorize")
def qbo_authorize():
    """Redirect user to QuickBooks' OAuth authorization page."""
    return RedirectResponse(build_qbo_auth_url())


@router.get("/oauth/qbo/callback")
def qbo_callback(code: str):
    """Handle QuickBooks OAuth callback, exchange code for tokens, and store in DB."""
    tokens = exchange_qbo_code_for_tokens(code)
    db = SessionLocal()
    db.add(QBOToken(**tokens))
    db.commit()
    db.close()
    return {"status": "QBO tokens stored"}
