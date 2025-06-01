import logging
from typing import Optional

from httpx import AsyncClient, HTTPStatusError, RequestError

from clio.token_store import get_access_token
from clio_client.api.matters_api import MattersApi
from clio_client.api_client import ApiClient
from clio_client.configuration import Configuration

logger = logging.getLogger(__name__)


class ClioClient:
    def __init__(self, base_url: str = "https://app.clio.com/api/v4"):
        self.base_url = base_url
        self.client: Optional[AsyncClient] = None
        self.sdk_client = self._init_sdk_client()
        self.matters_api = MattersApi(self.sdk_client)

    def _init_sdk_client(self) -> ApiClient:
        token = get_access_token()
        config = Configuration()
        config.api_key["Authorization"] = token
        config.api_key_prefix["Authorization"] = "Bearer"
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

    async def get(self, path: str, params: Optional[dict] = None):
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

    async def post(self, path: str, data: Optional[dict] = None):
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

    async def patch(self, path: str, data: Optional[dict] = None):
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
        if self.client:
            logger.debug("🔚 Closing AsyncClient session.")
            await self.client.aclose()

    async def __aenter__(self):
        await self._refresh_client()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()
