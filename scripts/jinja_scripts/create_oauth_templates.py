from pathlib import Path

template_dir = Path("templates")

# Define the templates and their content
templates = {
    "auth_flow.py.jinja": '''\
import http.server
import socketserver
import webbrowser
from urllib.parse import urlparse, parse_qs
import httpx

CLIENT_ID = "{{ client_id }}"
CLIENT_SECRET = "{{ client_secret }}"
REDIRECT_URI = "{{ redirect_uri }}"
TOKEN_URL = "{{ token_url }}"

class OAuthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        code = query.get("code", [None])[0]
        if not code:
            self.send_error(400, "Missing code")
            return

        tokens = self.exchange_code_for_tokens(code)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"✅ Authorization successful. You can close this tab.")

    def exchange_code_for_tokens(self, code):
        response = httpx.post(
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
        response.raise_for_status()
        return response.json()

def run_oauth_flow():
    url = (
        f"https://app.clio.com/oauth/authorize?response_type=code"
        f"&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=all"
    )
    webbrowser.open(url)
    with socketserver.TCPServer(("127.0.0.1", 8001), OAuthHandler) as httpd:
        httpd.handle_request()
''',

    "auth_utils.py.jinja": '''\
from datetime import datetime, timedelta
import json
from pathlib import Path

TOKEN_FILE = Path("~/.clio_tokens.json").expanduser()

def store_tokens(access_token: str, refresh_token: str, expires_in: int):
    expires_at = datetime.utcnow() + timedelta(seconds=expires_in)
    token_data = {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "expires_at": expires_at.isoformat(),
    }
    with TOKEN_FILE.open("w") as f:
        json.dump(token_data, f, indent=2)

def load_tokens():
    if not TOKEN_FILE.exists():
        return None
    with TOKEN_FILE.open() as f:
        return json.load(f)
''',

    "response.py.jinja": '''\
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")

class APIResponse(BaseModel, Generic[T]):
    data: Optional[T]
    message: Optional[str] = None
    success: bool = True
    errors: Optional[dict] = None
'''
}

# Create templates directory and write files
template_dir.mkdir(parents=True, exist_ok=True)
for filename, content in templates.items():
    (template_dir / filename).write_text(content)

"✅ Created initial templates: auth_flow, auth_utils, and response models."
