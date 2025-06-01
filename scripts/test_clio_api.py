import asyncio

from clio.token_store import get_access_token
from clio_sdk.client.client import ClioClient


async def main():
    token = get_access_token()
    client = ClioClient(token)

    try:
        result = await client.get("/users/who_am_i")
        print("✅ API Response:", result)
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())
