# clio_sdk/queries/contacts.py
from typing import Optional

from clio_sdk.client import ClioClient


async def get_contact_by_id(contact_id: int) -> dict:
    clio = ClioClient()
    return await clio.get(f"/contacts/{contact_id}.json")

async def list_contacts(search: Optional[str] = None) -> list[dict]:
    clio = ClioClient()
    params = {"query": search} if search else {}
    return await clio.get("/contacts.json", params=params)