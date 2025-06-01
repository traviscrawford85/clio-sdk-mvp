import os

import inflection
import yaml

# Constants
INPUT_FILE = "openapi_sdk.yaml"
ADAPTER_DIR = "clio_sdk/adapter_frags"
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

PRIMITIVES = {"str", "int", "float", "bool", "Any", "dict", "List"}


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
with open(INPUT_FILE, encoding="utf-8") as f:
    spec = yaml.safe_load(f)
schemas = spec.get("components", {}).get("schemas", {})

# Generate adapters per schema if the resource matches
for schema_name, schema in schemas.items():
    resource = normalize_resource_name(schema_name)
    if not resource:
        continue

    if "$ref" in schema:
        schema = resolve_ref_schema(schema["$ref"], schemas)
    props = schema.get("properties", {})
    if not props:
        print(f"⚠️  No properties found in schema: {schema_name}")
        continue

    safe_import = snake_case(schema_name)
    clio_class = pascal_case(schema_name)
    internal_class = pascal_case(resource)

    import_lines = {
        f"from clio_sdk.models.{resource} import {internal_class}",
        f"from clio_client.models.{safe_import} import {clio_class} as Clio{clio_class}",
    }
    extra_imports = set()
    forward_lines = []
    reverse_lines = []

    required = set(schema.get("required", []))
    for k, v in sorted(props.items()):
        if "$ref" in v:
            nested_schema = v["$ref"].split("/")[-1]
            nested_adapter = f"clio_to_internal_from_{snake_case(nested_schema)}"
            reverse_adapter = f"internal_to_clio_to_{snake_case(nested_schema)}"
            extra_imports.add(
                f"from clio_sdk.adapter_frags.adapter_{snake_case(nested_schema)} import {nested_adapter}, {reverse_adapter}"
            )
            if k in required:
                forward_lines.append(f"        {k}={nested_adapter}(obj.{k}),")
                reverse_lines.append(f"        {k}={reverse_adapter}(obj.{k}),")
            else:
                forward_lines.append(
                    f"        {k}={nested_adapter}(obj.{k}) if getattr(obj, '{k}', None) is not None else None,"
                )
                reverse_lines.append(
                    f"        {k}={reverse_adapter}(obj.{k}) if getattr(obj, '{k}', None) is not None else None,"
                )
        elif v.get("type") == "array" and "$ref" in v.get("items", {}):
            nested_schema = v["items"]["$ref"].split("/")[-1]
            nested_adapter = f"clio_to_internal_from_{snake_case(nested_schema)}"
            reverse_adapter = f"internal_to_clio_to_{snake_case(nested_schema)}"
            extra_imports.add(
                f"from clio_sdk.adapter_frags.adapter_{snake_case(nested_schema)} import {nested_adapter}, {reverse_adapter}"
            )
            if k in required:
                forward_lines.append(
                    f"        {k}=[{nested_adapter}(item) for item in getattr(obj, '{k}', [])],"
                )
                reverse_lines.append(
                    f"        {k}=[{reverse_adapter}(item) for item in getattr(obj, '{k}', [])],"
                )
            else:
                forward_lines.append(
                    f"        {k}=[{nested_adapter}(item) for item in getattr(obj, '{k}', [])] if getattr(obj, '{k}', None) else [],"
                )
                reverse_lines.append(
                    f"        {k}=[{reverse_adapter}(item) for item in getattr(obj, '{k}', [])] if getattr(obj, '{k}', None) else [],"
                )
        else:
            default = "[]" if v.get("type") == "array" else "None"
            if k in required:
                forward_lines.append(f"        {k}=obj.{k},")
                reverse_lines.append(f"        {k}=obj.{k},")
            else:
                forward_lines.append(f"        {k}=getattr(obj, '{k}', {default}),")
                reverse_lines.append(f"        {k}=getattr(obj, '{k}', {default}),")

    adapter_code = [
        f"def clio_to_internal_from_{safe_import}(obj: Clio{clio_class}) -> {internal_class}:",
        f'    """Convert Clio{clio_class} to unified {internal_class}."""',
        f"    return {internal_class}(",
        *forward_lines,
        "    )\n",
        f"def internal_to_clio_to_{safe_import}(obj: {internal_class}) -> Clio{clio_class}:",
        f'    """Convert unified {internal_class} to Clio{clio_class}."""',
        f"    return Clio{clio_class}(",
        *reverse_lines,
        "    )\n",
    ]

    adapter_path = os.path.join(ADAPTER_DIR, f"adapter_{safe_import}.py")
    with open(adapter_path, "w") as f:
        for line in sorted(import_lines | extra_imports):
            f.write(line + "\n")
        f.write("\n")
        for line in adapter_code:
            f.write(line + "\n")

print("✅ Generated adapters for selected resources only")
