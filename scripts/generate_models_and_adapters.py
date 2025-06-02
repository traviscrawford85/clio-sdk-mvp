from pathlib import Path
from typing import Dict, Any
import os
import yaml
import inflection
from jinja2 import Environment, FileSystemLoader

# Setup paths and environment
BASE_DIR = Path(".")
TEMPLATE_DIR = BASE_DIR / "sdk_templates"
MODEL_DIR = BASE_DIR / "clio_sdk/unified_models"
ADAPTER_DIR = BASE_DIR / "clio_sdk/unified_adapters"
INPUT_FILE = BASE_DIR / "openapi_sdk.yaml"

MODEL_DIR.mkdir(parents=True, exist_ok=True)
ADAPTER_DIR.mkdir(parents=True, exist_ok=True)

env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))

# Jinja2 templates
model_template = env.get_template("model_template.j2")
adapter_template = env.get_template("adapter_template.j2")

# Type resolution
TYPE_MAPPING = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "object": "dict",
}


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
    return TYPE_MAPPING.get(t, "Any")


def generate_model_and_adapter(resource: str, schemas: Dict[str, Any]) -> None:
    pascal = pascal_case(resource)
    snake = snake_case(resource)
    schema = schemas.get(pascal) or schemas.get(resource)
    if not schema:
        print(f"❌ Schema for '{resource}' not found.")
        return
    if "$ref" in schema:
        schema = resolve_ref_schema(schema["$ref"], schemas)

    properties = schema.get("properties", {})
    required = set(schema.get("required", []))
    fields = [
        {
            "name": name,
            "type": infer_type(prop),
            "required": name in required,
        }
        for name, prop in properties.items()
    ]

    model_code = model_template.render(class_name=pascal, fields=fields)
    (MODEL_DIR / f"{snake}.py").write_text(model_code)

    adapter_code = adapter_template.render(class_name=pascal, module_name=snake)
    (ADAPTER_DIR / f"adapter_{snake}.py").write_text(adapter_code)

    append_to_init(resource)
    print(f"✅ Generated model and adapter for '{resource}'")


def append_to_init(resource: str):
    init_path = MODEL_DIR / "__init__.py"
    class_name = pascal_case(resource)
    import_line = f"from .{snake_case(resource)} import {class_name}\n"

    if init_path.exists():
        lines = init_path.read_text().splitlines(keepends=True)
        if import_line in lines:
            return

    with open(init_path, "a") as f:
        f.write(import_line)


# Save script to file system for user reference
script_path = "/mnt/data/refactored_generate_single_model.py"
with open(script_path, "w") as f:
    f.write(Path(__file__).read_text())

script_path
