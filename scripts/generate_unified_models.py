import os
from collections import defaultdict

import inflection
import yaml

# Constants
INPUT_FILE = "openapi_sdk.yaml"
MODEL_DIR = "clio_sdk/models"
os.makedirs(MODEL_DIR, exist_ok=True)

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

PRIMITIVES = {"str", "int", "float", "bool", "Any", "dict", "List"}

FIELD_OVERRIDES = {
    "client": {"id": "client_id"},
    # Add more per-resource field overrides here as needed
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


def infer_type(prop: dict) -> str:
    if "$ref" in prop:
        ref_name = prop["$ref"].split("/")[-1]
        return pascal_case(ref_name)
    t = prop.get("type", "Any")
    if t == "array":
        return f"List[{infer_type(prop.get('items', {}))}]"
    return {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "object": "dict",
    }.get(t, "Any")


def merge_fields(
    existing: dict[str, tuple[str, bool]], new_fields: dict[str, tuple[str, bool]]
) -> None:
    for k, (new_type, new_required) in new_fields.items():
        if k not in existing:
            existing[k] = (new_type, new_required)
        else:
            old_type, old_required = existing[k]
            if old_type != new_type:
                preferred = "datetime" if "datetime" in [old_type, new_type] else "str"
                existing[k] = (preferred, old_required or new_required)
            else:
                existing[k] = (old_type, old_required or new_required)


with open(INPUT_FILE, encoding="utf-8") as f:
    spec = yaml.safe_load(f)
schemas = spec.get("components", {}).get("schemas", {})

grouped_schemas = defaultdict(list)
for name, schema in schemas.items():
    resource = normalize_resource_name(name)
    if resource:
        grouped_schemas[resource].append((name, schema))

generated = {}

for resource, variants in grouped_schemas.items():
    merged_fields = {}
    internal_class = pascal_case(resource)
    overrides = FIELD_OVERRIDES.get(resource, {})

    for schema_name, schema in variants:
        if "$ref" in schema:
            schema = resolve_ref_schema(schema["$ref"], schemas)
        props = schema.get("properties", {})
        required = set(schema.get("required", []))

        fields = {}
        for fname, fdef in props.items():
            ftype = infer_type(fdef)
            fields[fname] = (ftype, fname in required)

        merge_fields(merged_fields, fields)

    model_path = os.path.join(MODEL_DIR, f"{resource}.py")
    with open(model_path, "w") as f:
        f.write("from pydantic import BaseModel\n")
        f.write("from typing import Optional, Any, List\n")
        f.write("from datetime import datetime, date\n\n")
        f.write(f"class {internal_class}(BaseModel):\n")
        if not merged_fields:
            f.write("    pass\n")
        else:
            for fname, (ftype, required) in merged_fields.items():
                line = (
                    f"    {fname}: {ftype}"
                    if required
                    else f"    {fname}: Optional[{ftype}] = None"
                )
                f.write(line + "\n")

    generated[resource] = True

print("✅ Generated unified models for:", sorted(generated.keys()))
