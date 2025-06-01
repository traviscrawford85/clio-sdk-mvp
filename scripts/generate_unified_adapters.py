import os
from typing import Any

import inflection
import yaml

# Constants
INPUT_FILE = "openapi_sdk.yaml"
ADAPTER_DIR = "clio_sdk/adapters"
os.makedirs(ADAPTER_DIR, exist_ok=True)

RESOURCES = {
    "matter",
    "contact",
    "client",
    "calendar",
    "task",
    "activity",
    "document",
    "note",
    "custom_field",
    "custom_field_value",
    "webhook",
    "user",
    "report",
}


def pascal_case(name: str) -> str:
    return inflection.camelize(name)


def snake_case(name: str) -> str:
    return inflection.underscore(name)


def normalize_resource_name(name: str) -> str:
    for r in RESOURCES:
        if name.lower().startswith(r):
            return r
    return name.split("_")[0]


def resolve_ref_schema(ref: str, schemas: dict[str, Any]) -> dict[str, Any]:
    ref_name = ref.split("/")[-1]
    return schemas.get(ref_name, {})


def is_data_wrapper(schema: dict[str, Any]) -> bool:
    props = schema.get("properties", {})
    return "data" in props and isinstance(props["data"], dict)


def is_list_wrapper(schema: dict[str, Any]) -> bool:
    props = schema.get("properties", {})
    return props.get("data", {}).get("type") == "array"


# Load OpenAPI spec
with open(INPUT_FILE, encoding="utf-8") as f:
    spec = yaml.safe_load(f)
schemas = spec.get("components", {}).get("schemas", {})

# Generate unified adapters
for schema_name, schema in schemas.items():
    if "$ref" in schema:
        schema = resolve_ref_schema(schema["$ref"], schemas)

    resource = normalize_resource_name(schema_name)
    if resource not in RESOURCES:
        continue

    safe_import = snake_case(resource)
    clio_class = pascal_case(schema_name)
    internal_class = pascal_case(resource)

    import_lines = [
        f"from clio_client.models.{safe_import} import {clio_class} as Clio{clio_class}",
        f"from clio_sdk.models.{safe_import} import {internal_class}",
    ]

    if is_list_wrapper(schema):
        body = [
            f"def clio_to_internal_from_{safe_import}(obj: Clio{clio_class}) -> list[{internal_class}]:",
            f'    """Convert Clio{clio_class} (list in data) to list of {internal_class}."""',
            f"    return [ {internal_class}(**x.model_dump()) for x in obj.data ]\n",
            f"def internal_to_clio_to_{safe_import}(objs: list[{internal_class}]) -> Clio{clio_class}:",
            f'    """Convert list of {internal_class} to Clio{clio_class} (list in data)."""',
            f"    return Clio{clio_class}(data=objs)\n",
        ]
    elif is_data_wrapper(schema):
        body = [
            f"def clio_to_internal_from_{safe_import}(obj: Clio{clio_class}) -> {internal_class}:",
            f'    """Convert Clio{clio_class} (with data) to unified {internal_class}."""',
            f"    return {internal_class}(**obj.data.model_dump())\n",
            f"def internal_to_clio_to_{safe_import}(obj: {internal_class}) -> Clio{clio_class}:",
            f'    """Convert unified {internal_class} to Clio{clio_class} (with data)."""',
            f"    return Clio{clio_class}(data=obj)\n",
        ]
    else:
        body = [
            f"def clio_to_internal_from_{safe_import}(obj: Clio{clio_class}) -> {internal_class}:",
            f'    """Convert flat Clio{clio_class} to unified {internal_class}."""',
            f"    return {internal_class}(**obj.model_dump())\n",
            f"def internal_to_clio_to_{safe_import}(obj: {internal_class}) -> Clio{clio_class}:",
            f'    """Convert unified {internal_class} to flat Clio{clio_class}."""',
            f"    return Clio{clio_class}(**obj.model_dump())\n",
        ]

    path = os.path.join(ADAPTER_DIR, f"adapter_{safe_import}.py")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(import_lines) + "\n\n" + "\n".join(body))

print("✅ Generated unified adapters from OpenAPI with wrapper awareness.")
