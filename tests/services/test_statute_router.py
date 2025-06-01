# tests/api/routes/test_statute_router.py
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from clio.api.routes.statute_router import router
from clio_sdk.services.statute_sync_api_service import sync_statute_to_matter

app = FastAPI()
app.include_router(router)

@pytest.mark.asyncio
async def test_sync_statute_success(monkeypatch):
    async def mock_sync_statute_to_matter(matter_id: int):
        assert matter_id == 123

    monkeypatch.setattr("clio_sdk.services.statute_sync_api_service.sync_statute_to_matter", mock_sync_statute_to_matter)

    with TestClient(app) as client:
        response = client.post("/statuteoflimitations/sync/123")
        assert response.status_code == 200
        assert response.json() == {"message": "Statute of limitations synced successfully."}
