script_path = "scripts/generate_selected_adapters.py"

script_content = """\
import os
import sys
import yaml
import inflection

# Constants
INPUT_FILE = "openapi_sdk.yaml"
ADAPTER_DIR = "clio_sdk/adapter_frags"
os.makedirs(ADAPTER_DIR, exist_ok=True)

PRIMITIVES = {"str", "int", "float", "bool", "Any", "dict", "List"}

def pascal_case(name: str) -> str:
    return inflection.camelize(name)

def snake_case(name: str) -> str:
    return inflection.underscore(name)

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
        "object": "dict"
    }.get(t, "Any")

if len(sys.argv) < 2:
    print("Usage: python3 generate_selected_adapters.py <SchemaName1> <SchemaName2> ...")
    sys.exit(1)

selected_schemas = set(sys.argv[1:])

# Load OpenAPI spec
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    spec = yaml.safe_load(f)
schemas = spec.get("components", {}).get("schemas", {})

for schema_name in selected_schemas:
    schema = schemas.get(schema_name)
    if not schema:
        print(f"⚠️  Schema not found: {schema_name}")
        continue
    if "$ref" in schema:
        schema = resolve_ref_schema(schema["$ref"], schemas)
    props = schema.get("properties", {})
    if not props:
        print(f"⚠️  No properties in schema: {schema_name}")
        continue

    safe_import = snake_case(schema_name)
    clio_class = pascal_case(schema_name)
    resource = schema_name.split("_")[0]
    internal_class = pascal_case(resource)

    import_lines = {
        f"from clio_sdk.models.{resource} import {internal_class}",
        f"from clio_client.models.{safe_import} import {clio_class} as Clio{clio_class}"
    }

    extra_imports = set()
    forward_lines = []
    reverse_lines = []
    required = set(schema.get("required", []))

    for k, v in sorted(props.items()):
        if "$ref" in v:
            nested = v["$ref"].split("/")[-1]
            nested_func = snake_case(nested)
            extra_imports.add(f"from clio_sdk.adapter_frags.adapter_{nested_func} import clio_to_internal_from_{nested_func}, internal_to_clio_to_{nested_func}")
            forward_lines.append(f"        {k}=clio_to_internal_from_{nested_func}(obj.{k}) if getattr(obj, '{k}', None) else None,")
            reverse_lines.append(f"        {k}=internal_to_clio_to_{nested_func}(obj.{k}) if getattr(obj, '{k}', None) else None,")
        elif v.get("type") == "array" and "$ref" in v.get("items", {}):
            nested = v["items"]["$ref"].split("/")[-1]
            nested_func = snake_case(nested)
            extra_imports.add(f"from clio_sdk.adapter_frags.adapter_{nested_func} import clio_to_internal_from_{nested_func}, internal_to_clio_to_{nested_func}")
            forward_lines.append(f"        {k}=[clio_to_internal_from_{nested_func}(item) for item in getattr(obj, '{k}', [])],")
            reverse_lines.append(f"        {k}=[internal_to_clio_to_{nested_func}(item) for item in getattr(obj, '{k}', [])],")
        else:
            forward_lines.append(f"        {k}=getattr(obj, '{k}', None),")
            reverse_lines.append(f"        {k}=getattr(obj, '{k}', None),")

    adapter_code = [
        f"def clio_to_internal_from_{safe_import}(obj: Clio{clio_class}) -> {internal_class}:",
        f"    return {internal_class}(", *forward_lines, "    )\n",
        f"def internal_to_clio_to_{safe_import}(obj: {internal_class}) -> Clio{clio_class}:",
        f"    return Clio{clio_class}(", *reverse_lines, "    )\n"
    ]

    with open(os.path.join(ADAPTER_DIR, f"adapter_{safe_import}.py"), "w") as f:
        for line in sorted(import_lines | extra_imports):
            f.write(line + "\\n")
        f.write("\\n")
        for line in adapter_code:
            f.write(line + "\\n")

print("✅ Selected adapters generated.")
"""

with open(script_path, "w") as f:
    f.write(script_content)

script_path
