import importlib
import inspect
from pathlib import Path

import yaml
from clio_async_client.api.matters import raw_list_matters, raw_get_matter
from clio_async_client.client import AuthenticatedClient
from clio_sdk.adapter_factory import get_adapter
from clio_sdk.unified_models.matter import Matter

# Base directory and output directory
BASE_PACKAGE = "clio_client.models"
MODEL_DIR = Path("clio_client/models")
OUTPUT_DIR = Path("schemas")
OUTPUT_DIR.mkdir(exist_ok=True)


def dump_model_schemas_to_yaml():
    model_files = [f.stem for f in MODEL_DIR.glob("*.py") if f.name != "__init__.py"]

    for model_name in model_files:
        module_path = f"{BASE_PACKAGE}.{model_name}"
        try:
            module = importlib.import_module(module_path)

            for name, obj in inspect.getmembers(module, inspect.isclass):
                if obj.__module__ == module_path and hasattr(obj, "model_json_schema"):
                    schema = obj.model_json_schema()
                    output_path = OUTPUT_DIR / f"{name}.yaml"
                    with open(output_path, "w") as f:
                        yaml.dump(schema, f, sort_keys=False)
        except Exception as e:
            print(f"❌ Failed to process {module_path}: {e}")


async def list_matters(client: AuthenticatedClient) -> list[Matter]:
    """Returns all matters as SDK models"""
    resp = await raw_list_matters(client=client)
    if resp.status_code == 200 and resp.parsed:
        adapter = get_adapter("matter")
        return [adapter["from_clio"](m) for m in resp.parsed.matters]
    return []


async def get_matter_by_id(
    client: AuthenticatedClient, matter_id: int
) -> Matter | None:
    """Returns a single matter by ID"""
    resp = await raw_get_matter(client=client, id=matter_id)
    if resp.status_code == 200 and resp.parsed:
        adapter = get_adapter("matter")
        return adapter["from_clio"](resp.parsed.matter)
    return None


dump_model_schemas_to_yaml()
