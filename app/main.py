import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from clio.api.routes import matters_router
from clio.api.routes.statute_router import router as statute_router
from clio.database.init_db import init_db
from clio.lifecycle.webhook_lifecycle import init_webhook_registration
from clio_client.webhook_listener import router as webhook_listener_router
from clio_sdk.client import ClioClient
from webhooks import router as webhooks_router

# Load environment variables from .env
load_dotenv()

# Log critical env variables on startup
print("🔐 Clio API URL:", os.getenv("CLIO_API_URL"))
print("💾 Token DB Path:", os.getenv("CLIO_DATABASE_URL"))
print("🌍 Environment:", os.getenv("CLIO_ENVIRONMENT"))

# Initialize the token DB and tables
init_db()

# Create FastAPI app instance
app = FastAPI(
    title="Clio Integration Service",
    description="FastAPI app for computing and syncing statute of limitations",
    version="1.0.0",
)
init_webhook_registration(app)

# Enable CORS (customize origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Consider restricting for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(webhooks_router)
app.include_router(webhook_listener_router)
app.include_router(matters_router.router, prefix="/matters")
app.include_router(statute_router)

# Initialize ClioClient using the API URL from .env
clio = ClioClient(base_url=os.getenv("CLIO_API_URL", "https://app.clio.com/api/v4"))

@app.get("/some_async_endpoint")
async def some_async_endpoint():
    return await clio.get("/matters")
