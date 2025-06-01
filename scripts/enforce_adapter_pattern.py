import os

import inflection
import yaml

# Constants
INPUT_FILE = "openapi_sdk.yaml"
MODEL_DIR = "clio_sdk/models"
ADAPTER_DIR = "clio_sdk/adapter_frags"
os.makedirs(MODEL_DIR, exist_ok=True)
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
    return ""


def resolve_ref_schema(ref: str, schemas: dict) -> dict:
    ref_name = ref.split("/")[-1]
    return schemas.get(ref_name, {})


# Load OpenAPI spec
with open(INPUT_FILE, encoding="utf-8") as f:
    spec = yaml.safe_load(f)
schemas = spec.get("components", {}).get("schemas", {})

for schema_name, schema in schemas.items():
    if "$ref" in schema:
        schema = resolve_ref_schema(schema["$ref"], schemas)
    props = schema.get("properties", {})
    if not props:
        print(f"⚠️  No properties found in schema: {schema_name}")
        continue

    safe_import = snake_case(schema_name)
    clio_class = pascal_case(schema_name)
    internal_resource = (
        normalize_resource_name(schema_name) or schema_name.split("_")[0]
    )
    internal_class = pascal_case(internal_resource)

    import_lines = [
        f"from clio_sdk.models.{internal_resource} import {internal_class}",
        f"from clio_client.models.{safe_import} import {clio_class} as Clio{clio_class}",
    ]

    # Detect if this schema is a wrapper with a top-level 'data' property
    is_data_wrapper = "data" in props and (
        props["data"].get("type") == "object" or "$ref" in props["data"]
    )

    # Determine which fields to map
    if is_data_wrapper:
        # Use the fields from the inner schema referenced by 'data'
        if "$ref" in props["data"]:
            inner_schema_name = props["data"]["$ref"].split("/")[-1]
            inner_schema = schemas.get(inner_schema_name, {})
            inner_props = inner_schema.get("properties", {})
            fields = sorted(inner_props.keys())
        else:
            fields = sorted(props["data"].get("properties", {}).keys())
    else:
        fields = sorted(props.keys())

    # Generate adapter code
    if is_data_wrapper:
        forward_lines = [f"        {f}=getattr(obj.data, '{f}', None)," for f in fields]
        reverse_lines = [f"        '{f}': getattr(obj, '{f}', None)," for f in fields]
        adapter_code = [
            f"FIELDS = {fields}\n",
            f"def clio_to_internal_from_{safe_import}(obj: Clio{clio_class}) -> {internal_class}:",
            f'    """Convert Clio{clio_class} (with data wrapper) to unified {internal_class}."""',
            f"    return {internal_class}(",
            *forward_lines,
            "    )\n",
            f"def internal_to_clio_to_{safe_import}(obj: {internal_class}) -> Clio{clio_class}:",
            f'    """Convert unified {internal_class} to Clio{clio_class} (with data wrapper)."""',
            f"    return Clio{clio_class}(data={{",
            *reverse_lines,
            "    }})\n",
        ]
    else:
        forward_lines = [f"        {f}=getattr(obj, '{f}', None)," for f in fields]
        reverse_lines = [f"        '{f}': getattr(obj, '{f}', None)," for f in fields]
        adapter_code = [
            f"FIELDS = {fields}\n",
            f"def clio_to_internal_from_{safe_import}(obj: Clio{clio_class}) -> {internal_class}:",
            f'    """Convert Clio{clio_class} (flat) to unified {internal_class}."""',
            f"    return {internal_class}(",
            *forward_lines,
            "    )\n",
            f"def internal_to_clio_to_{safe_import}(obj: {internal_class}) -> Clio{clio_class}:",
            f'    """Convert unified {internal_class} to Clio{clio_class} (flat)."""',
            f"    return Clio{clio_class}(",
            *reverse_lines,
            "    )\n",
        ]

    adapter_path = os.path.join(ADAPTER_DIR, f"adapter_{safe_import}.py")
    with open(adapter_path, "w") as f:
        for line in import_lines:
            f.write(line + "\n")
        f.write("\n")
        for line in adapter_code:
            f.write(line + "\n")

print("✅ Generated adapters with auto-detected data wrapper pattern.")
