from clio_sdk.client import ClioClient


async def get_custom_field_definition(name: str):
    clio = ClioClient()
    fields = await clio.get("/custom_fields.json", params={"parent_type": "Matter"})
    return next((f for f in fields.get("data", []) if f["name"] == name), None)
