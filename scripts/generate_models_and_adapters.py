import os

import inflection
import yaml

from clio_sdk.resources import RESOURCES

INPUT_FILE = "openapi_sdk.yaml"
MODEL_DIR = "clio_sdk/unified_models"
os.makedirs(MODEL_DIR, exist_ok=True)


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


# Load OpenAPI spec
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    spec = yaml.safe_load(f)
schemas = spec.get("components", {}).get("schemas", {})

# Group schemas by resource
grouped = {}
for name, schema in schemas.items():
    resource = normalize_resource_name(name)
    if resource:
        grouped.setdefault(resource, []).append((name, schema))

# Generate unified models
for resource, items in grouped.items():
    merged_fields = {}
    referenced_models = set()
    internal_class = pascal_case(resource)
    unified_model_class = f"Unified{internal_class}"

    for name, schema in items:
        if "$ref" in schema:
            schema = resolve_ref_schema(schema["$ref"], schemas)
        props = schema.get("properties", {})
        required = set(schema.get("required", []))
        fields = {}
        for k, v in props.items():
            ftype = infer_type(v)
            # Track referenced models for import
            if (
                ftype not in {"str", "int", "float", "bool", "dict", "Any"}
                and not ftype.startswith("List[")
            ):
                referenced_models.add(ftype)
            elif ftype.startswith("List["):
                # Extract the inner type for List[...] and check if it's a model
                inner_type = ftype[5:-1]
                if inner_type not in {"str", "int", "float", "bool", "dict", "Any"}:
                    referenced_models.add(inner_type)
            fields[k] = (ftype, k in required)
        for k, (ftype, required) in fields.items():
            if k not in merged_fields:
                merged_fields[k] = (ftype, required)
            else:
                old_type, old_req = merged_fields[k]
                if old_type != ftype:
                    merged_fields[k] = ("str", old_req or required)
                else:
                    merged_fields[k] = (old_type, old_req or required)

    model_path = os.path.join(MODEL_DIR, f"unified_{resource}.py")
    with open(model_path, "w") as f:
        f.write("from pydantic import BaseModel\n")
        f.write("from typing import Optional, Any, List\n")
        f.write("from datetime import datetime, date\n")
        # Import referenced models
        for ref in sorted(referenced_models):
            f.write(f"from .unified_{ref.lower()} import Unified{ref}\n")
        f.write("\n")
        f.write(f"class {unified_model_class}(BaseModel):\n")
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

print(
    "✅ Cleaned script generated models, adapters, and transformers without adapter fragments."
)
