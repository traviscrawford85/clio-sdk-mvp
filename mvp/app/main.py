from fastapi import FastAPI
from app.core.router_loader import auto_register_routers
from app.auth.jwt_auth import create_access_token
from app.core.clio_webhook_manager import register_clio_webhooks
from app.api.v1.clio import clio_service_routes
from app.api.v1.clio import webhooks as clio_webhooks
from app.api.v1.qbo import webhooks as qbo_webhooks
from app.api.v1.slack import webhooks as slack_webhooks
from app.webhooks.slack_events.slack_app import app as slack_bolt_app
from slack_bolt.adapter.socket_mode import SocketModeHandler
from app.api.v1.clio import routes as clio_routes
from app.api.v1.qbo import routes as qbo_routes
from app.api.v1.slack import routes as slack_routes
from app.api.v1 import auth_routes
from app.api.v1.routes import clio as simple_clio_routes, slack as simple_slack_routes
import logging
from dotenv import load_dotenv
import threading
import os
from app.auth.oauth_server import router as oauth_router
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from app.auth.token_store import get_access_token
from clio_sdk_mvp.services.slack_notification_service import SlackNotificationService
from app.core.logging_config import setup_logging
from app.services.qbo_service import qbo_service

load_dotenv()

logger = setup_logging(__name__)
logger.info("🟢 Starting Clio Service API...")

# --- Initialize FastAPI app ---
app = FastAPI(
    title="Clio Service API",
    description="Handles Clio integrations and custom fields",
    version="1.0.0",
    swagger_ui_parameters={"persistAuthorization": True},
)

# --- Initialize ClioSDK client ---
clio_sdk = ClioSDK()
slack_notification_service = SlackNotificationService()

# Include all routers (comprehensive and simple)
app.include_router(clio_routes.router, prefix="/api/v1")
app.include_router(qbo_routes.router, prefix="/api/v1")
app.include_router(slack_routes.router, prefix="/api/v1")
app.include_router(auth_routes.router, prefix="/api/v1")
app.include_router(clio_webhooks.router, prefix="/api/v1/webhooks")
app.include_router(slack_webhooks.router, prefix="/api/v1/webhooks")
app.include_router(qbo_webhooks.router, prefix="/api/v1/webhooks")
# Also include simple routers if needed
app.include_router(simple_clio_routes.router, prefix='/api/clio')
app.include_router(simple_slack_routes.router, prefix='/api/slack')
# Register OAuth router (for Clio and QBO)
app.include_router(oauth_router)
# --- Inject Authorization header automatically for Swagger ---
@app.middleware("http")
async def add_authorization_header(request, call_next):
    if request.url.path.startswith("/docs") or request.url.path.startswith("/openapi.json"):
        if b"authorization" not in dict(request.scope.get("headers", [])):
            request.scope["headers"].append(
                (b"authorization", f"Bearer {access_token}".encode())
            )
    response = await call_next(request)
    return response

@app.middleware("http")
async def log_requests(request, call_next):
    logger.info(f"📥 Request: {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"📤 Response: {response.status_code} for {request.url.path}")
    return response

# --- Startup logic ---
@app.on_event("startup")
async def startup_event():
    """Startup logic for the application."""
    logger.info("🔌 Starting Slack Socket Mode...")
    os.makedirs("logs", exist_ok=True)

    thread = threading.Thread(target=start_socket_handler, daemon=True)
    thread.start()

# --- Auto-load routers ---
auto_register_routers(app, "app.api.v1.clio")
logger.info("✅ Routers auto-registered successfully.")

# --- Healthcheck endpoint ---
@app.get("/", tags=["Health"])
def read_root():
    return {"message": "Clio Service is running"}

# --- JWT Token generation endpoint ---
@app.post("/api/v1/token", tags=["Auth"])
async def generate_token():
    data = {"sub": "clio-service"}
    token = create_access_token(data)
    return {"access_token": token, "token_type": "bearer"}

# Load Slack App Token from environment variables
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

def start_socket_handler():
    """Start the Slack Socket Mode handler."""
    handler = SocketModeHandler(slack_bolt_app, SLACK_APP_TOKEN)
    handler.start()
