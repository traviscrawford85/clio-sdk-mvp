# clio_sdk/queries/batch.py
from clio_sdk.client import ClioClient


async def batch_get_matters(ids: list[int]) -> list[dict]:
    clio = ClioClient()
    return [await clio.get(f"/matters/{id}.json") for id in ids]
