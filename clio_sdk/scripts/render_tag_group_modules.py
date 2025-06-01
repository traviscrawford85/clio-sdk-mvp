"""
Render API modules for each tag group using the Jinja template and OpenAPI-derived groupings.
"""
import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Paths
BASE_DIR = Path(__file__).parent.parent
TEMPLATE_PATH = BASE_DIR / "sdk_templates" / "api_module.py.jinja"
TAG_GROUPS_PATH = BASE_DIR / "suggested_x_tagGroups.yaml"
OPENAPI_PATH = BASE_DIR / "openapi_sdk.yaml"
OUTPUT_DIR = BASE_DIR / "api_modules"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load tag groups
tag_groups_yaml = yaml.safe_load(open(TAG_GROUPS_PATH, encoding="utf-8"))
tag_groups = tag_groups_yaml.get("x-tagGroups", [])

# Load OpenAPI spec
openapi_spec = yaml.safe_load(open(OPENAPI_PATH, encoding="utf-8"))

# Build operations_by_tag dict
operations_by_tag = {}
for path, methods in openapi_spec.get("paths", {}).items():
    for method, op in methods.items():
        if method.lower() not in {"get", "post", "put", "delete", "patch"}:
            continue
        for tag in op.get("tags", []):
            op_dict = {
                "operation_id": op.get("operationId", ""),
                "summary": op.get("summary", ""),
                "description": op.get("description", ""),
                "method": method.upper(),
                "path": path,
                # You can add more fields as needed for the template
                "signature": "**kwargs: Any",  # TODO: Generate real signature
                "request_args": "**kwargs",   # TODO: Generate real request args
            }
            operations_by_tag.setdefault(tag, []).append(op_dict)

# Set up Jinja environment
env = Environment(loader=FileSystemLoader(str(TEMPLATE_PATH.parent)))
template = env.get_template(TEMPLATE_PATH.name)

# Render and write a module for each tag group
for tag_group in tag_groups:
    module_code = template.render(tag_group=tag_group, operations_by_tag=operations_by_tag)
    module_filename = f"api_{tag_group['name'].replace(' ', '_').lower()}.py"
    module_path = OUTPUT_DIR / module_filename
    with open(module_path, "w", encoding="utf-8") as f:
        f.write(module_code)
    print(f"✅ Generated: {module_path}")

print(f"\nAll tag group modules written to: {OUTPUT_DIR}")
