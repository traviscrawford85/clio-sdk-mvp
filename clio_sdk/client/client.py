import logging
from typing import Optional, Dict, Any

from httpx import AsyncClient, HTTPStatusError, RequestError

from clio.token_store import get_access_token
from clio_client.api.matters_api import MattersApi
from clio_client.api.contacts_api import ContactsApi
from clio_client.api_client import ApiClient
from clio_client.configuration import Configuration

logger = logging.getLogger(__name__)


class ClioSDK:
    """
    High-level async SDK for Clio API.
    Wraps the low-level client and exposes unified, business-centric methods.
    """

    def __init__(self, base_url: str = "https://app.clio.com/api/v4"):
        self.base_url = base_url
        self.client: Optional[AsyncClient] = None
        self.sdk_client = self._init_sdk_client()
        self.matters = MattersApi(self.sdk_client)
        self.contacts = ContactsApi(self.sdk_client)
        # Add more APIs as needed

    def _init_sdk_client(self) -> ApiClient:
        token = get_access_token()
        config = Configuration()
        config.api_key["Authorization"] = token
        config.api_key_prefix["Authorization"] = "Bearer"
        config.host = self.base_url
        return ApiClient(configuration=config)

    async def _refresh_client(self):
        token = get_access_token()
        if self.client:
            await self.client.aclose()
        logger.debug("🔁 Initializing AsyncClient for raw requests")
        self.client = AsyncClient(
            base_url=self.base_url,
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
            },
        )

    async def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Raw GET request with token management and logging."""
        await self._refresh_client()
        try:
            logger.info(f"🔍 GET {path} with params={params}")
            resp = await self.client.get(path, params=params)
            resp.raise_for_status()
            logger.debug(f"✅ GET {path} response: {resp.text}")
            return resp.json()
        except (HTTPStatusError, RequestError) as e:
            logger.exception(f"❌ GET request failed: {e}")
            raise

    async def post(self, path: str, data: Optional[Dict[str, Any]] = None) -> Any:
        """Raw POST request with token management and logging."""
        await self._refresh_client()
        try:
            logger.info(f"📤 POST {path} with data={data}")
            resp = await self.client.post(path, json=data)
            resp.raise_for_status()
            logger.debug(f"✅ POST {path} response: {resp.text}")
            return resp.json()
        except (HTTPStatusError, RequestError) as e:
            logger.exception(f"❌ POST request failed: {e}")
            raise

    async def patch(self, path: str, data: Optional[Dict[str, Any]] = None) -> Any:
        """Raw PATCH request with token management and logging."""
        await self._refresh_client()
        try:
            logger.info(f"🔧 PATCH {path} with data={data}")
            resp = await self.client.patch(path, json=data)
            resp.raise_for_status()
            logger.debug(f"✅ PATCH {path} response: {resp.text}")
            return resp.json()
        except (HTTPStatusError, RequestError) as e:
            logger.exception(f"❌ PATCH request failed: {e}")
            raise

    async def close(self):
        """Close the AsyncClient session."""
        if self.client:
            logger.debug("🔚 Closing AsyncClient session.")
            await self.client.aclose()

    async def __aenter__(self):
        await self._refresh_client()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()
