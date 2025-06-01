import os
from typing import Any, Dict

import inflection
import yaml

INPUT_FILE = "openapi_sdk.yaml"
MODEL_DIR = "clio_sdk/unified_models"
ADAPTER_DIR = "clio_sdk/unified_adapters"

os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(ADAPTER_DIR, exist_ok=True)

def pascal_case(name: str) -> str:
    return inflection.camelize(name)

def snake_case(name: str) -> str:
    return inflection.underscore(name)

def resolve_ref_schema(ref: str, schemas: Dict[str, Any]) -> Dict[str, Any]:
    ref_name = ref.split("/")[-1]
    return schemas.get(ref_name, {})

def infer_type(prop: Dict[str, Any]) -> str:
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
        "object": "dict"
    }.get(t, "Any")

def generate_model_and_adapter(resource: str, schemas: Dict[str, Any]) -> None:
    pascal = pascal_case(resource)
    snake = snake_case(resource)

    schema = schemas.get(pascal) or schemas.get(resource)
    if not schema:
        print(f"❌ Schema for '{resource}' not found.")
        return

    # Resolve if schema is a ref
    if "$ref" in schema:
        schema = resolve_ref_schema(schema["$ref"], schemas)

    properties = schema.get("properties", {})
    required = set(schema.get("required", []))

    # Generate model
    model_path = os.path.join(MODEL_DIR, f"{snake}.py")
    with open(model_path, "w") as f:
        f.write("from pydantic import BaseModel\n")
        f.write("from typing import Optional, Any, List\n")
        f.write("from datetime import datetime, date\n\n")
        f.write(f"class {pascal}(BaseModel):\n")
        if not properties:
            f.write("    pass\n")
        else:
            for name, prop in properties.items():
                ptype = infer_type(prop)
                line = f"    {name}: {ptype}" if name in required else f"    {name}: Optional[{ptype}] = None"
                f.write(line + "\n")

    # Generate adapter
    adapter_path = os.path.join(ADAPTER_DIR, f"adapter_{snake}.py")
    with open(adapter_path, "w") as f:
        f.write(f"from clio_client.unified_models.{snake} import {pascal} as Clio{pascal}\n")
        f.write(f"from clio_sdk.models.{snake} import {pascal}\n\n")
        f.write(f"def clio_to_internal_from_{snake}(obj: Clio{pascal}) -> {pascal}:\n")
        f.write(f"    return {pascal}(**obj.model_dump())\n\n")
        f.write(f"def internal_to_clio_to_{snake}(obj: {pascal}) -> Clio{pascal}:\n")
        f.write(f"    return Clio{pascal}(**obj.model_dump())\n")

    print(f"✅ Generated model and adapter for '{resource}'")
def append_to_init(resource: str):
    init_path = os.path.join(MODEL_DIR, "__init__.py")
    class_name = pascal_case(resource)
    import_line = f"from .{snake_case(resource)} import {class_name}\n"

    # Avoid duplicate entries
    if os.path.exists(init_path):
        with open(init_path, "r") as f:
            lines = f.readlines()
        if import_line in lines:
            return

    with open(init_path, "a") as f:
        f.write(import_line)

import argparse

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python generate_single_model.py custom_field_value [another_resource ...]")
        sys.exit(1)

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        spec = yaml.safe_load(f)
    schemas = spec.get("components", {}).get("schemas", {})

    for resource_name in sys.argv[1:]:
        generate_model_and_adapter(resource_name, schemas)
        append_to_init(resource_name)



