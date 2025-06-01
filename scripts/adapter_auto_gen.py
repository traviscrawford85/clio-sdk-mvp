import os
from typing import Any

import inflection
import yaml

from clio_sdk.resources import RESOURCES  # <-- Use the shared list

# Constants
INPUT_FILE = "openapi_sdk.yaml"
ADAPTER_DIR = "clio_sdk/adapters_frags"
os.makedirs(ADAPTER_DIR, exist_ok=True)


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


def detect_wrapper_schemas(schemas: dict[str, Any]) -> set:
    return {
        name
        for name, schema in schemas.items()
        if list(schema.get("properties", {}).keys()) == ["data"]
    }


def generate_adapter(
    schema_name: str,
    schema: dict[str, Any],
    schemas: dict[str, Any],
    wrapper_schemas: set,
) -> None:
    safe_import = snake_case(schema_name)
    clio_class = pascal_case(schema_name)
    internal_resource = normalize_resource_name(schema_name)
    if internal_resource not in RESOURCES:
        return
    internal_class = pascal_case(internal_resource)

    import_lines = [
        f"from clio_sdk.models.{internal_resource} import {internal_class}",
        f"from clio_client.models.{safe_import} import {clio_class} as Clio{clio_class}",
    ]

    if not schema.get("properties"):
        print(f"⚠️  No properties found in schema: {schema_name}")
        return

    is_data_wrapper = schema_name in wrapper_schemas

    if is_data_wrapper:
        adapter_code = [
            f"def clio_to_internal_from_{safe_import}(obj: Clio{clio_class}) -> {internal_class}:",
            f'    """Convert Clio{clio_class} (with data wrapper) to unified {internal_class}."""',
            f"    return {internal_class}(**obj.data.model_dump())",
            f"def internal_to_clio_to_{safe_import}(obj: {internal_class}) -> Clio{clio_class}:",
            f'    """Convert unified {internal_class} to Clio{clio_class} (with data wrapper)."""',
            f"    return Clio{clio_class}(data=obj)",
        ]
    else:
        adapter_code = [
            f"def clio_to_internal_from_{safe_import}(obj: Clio{clio_class}) -> {internal_class}:",
            f'    """Convert Clio{clio_class} (flat) to unified {internal_class}."""',
            f"    return {internal_class}(**obj.model_dump())",
            f"def internal_to_clio_to_{safe_import}(obj: {internal_class}) -> Clio{clio_class}:",
            f'    """Convert unified {internal_class} to Clio{clio_class} (flat)."""',
            f"    return Clio{clio_class}(**obj.model_dump())",
        ]

    adapter_path = os.path.join(ADAPTER_DIR, f"adapter_{safe_import}.py")
    with open(adapter_path, "w", encoding="utf-8") as f:
        for line in import_lines:
            f.write(line + "\n")
        f.write("\n")
        for line in adapter_code:
            f.write(line + "\n")


# Load OpenAPI spec
with open(INPUT_FILE, encoding="utf-8") as f:
    spec = yaml.safe_load(f)
schemas = spec.get("components", {}).get("schemas", {})
wrapper_schemas = detect_wrapper_schemas(schemas)

for schema_name, schema_def in schemas.items():
    if "$ref" in schema_def:
        schema_def = resolve_ref_schema(schema_def["$ref"], schemas)
    generate_adapter(schema_name, schema_def, schemas, wrapper_schemas)

print("✅ Generated adapters with dynamic wrapper detection from OpenAPI spec.")
if __name__ == "__main__":
    # Load OpenAPI spec
    with open(INPUT_FILE, encoding="utf-8") as f:
        spec = yaml.safe_load(f)
    schemas = spec.get("components", {}).get("schemas", {})
    wrapper_schemas = detect_wrapper_schemas(schemas)

    for schema_name, schema_def in schemas.items():
        if "$ref" in schema_def:
            schema_def = resolve_ref_schema(schema_def["$ref"], schemas)
        generate_adapter(schema_name, schema_def, schemas, wrapper_schemas)

    print("✅ Adapter fragments generated.")
