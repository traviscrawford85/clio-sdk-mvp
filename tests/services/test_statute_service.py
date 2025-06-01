import pytest
from fastapi import HTTPException

from clio_sdk.client import ClioClient
from clio_sdk.services.statute_service import compute_statute_for_matter


@pytest.mark.asyncio
async def test_compute_statute_for_matter(monkeypatch):
    async def mock_get(path, params=None):
        assert path == "/matters/123"
        return {
            "custom_field_values": [
                {"name": "Date of Incident", "value": "2023-05-28"}
            ]
        }

    monkeypatch.setattr(ClioClient, "get", lambda self, path, params=None: mock_get(path, params))
    result = await compute_statute_for_matter(123)
    assert result == "2025-05-28"


@pytest.mark.asyncio
async def test_missing_date_of_incident(monkeypatch):
    async def mock_get(path, params=None):
        return {
            "custom_field_values": []
        }

    monkeypatch.setattr(ClioClient, "get", lambda self, path, params=None: mock_get(path, params))
    with pytest.raises(HTTPException) as exc_info:
        await compute_statute_for_matter(123)
    assert exc_info.value.status_code == 400
    assert "Date of Incident not found" in str(exc_info.value.detail)


@pytest.mark.asyncio
async def test_malformed_date(monkeypatch):
    async def mock_get(path, params=None):
        return {
            "custom_field_values": [
                {"name": "Date of Incident", "value": "not-a-date"}
            ]
        }

    monkeypatch.setattr(ClioClient, "get", lambda self, path, params=None: mock_get(path, params))
    with pytest.raises(HTTPException) as exc_info:
        await compute_statute_for_matter(123)
    assert exc_info.value.status_code == 422
    assert "Invalid incident date format" in str(exc_info.value.detail)
