from jinja2 import Environment, FileSystemLoader
import yaml
from pathlib import Path

# Constants
resources = [
    "matter", "contact", "client", "calendar", "task", "activity", "document", "note",
    "custom_field", "custom_field_value", "webhook", "user", "report", "statute"
]
openapi_path = Path("openapi_sdk.yaml")
template_path = Path("templates/transformer_template.j2")
output_dir = Path("adapter_factory/transformers")
output_dir.mkdir(parents=True, exist_ok=True)

# Load template
env = Environment(loader=FileSystemLoader(template_path.parent))
template = env.get_template(template_path.name)

# Load OpenAPI schema
with open(openapi_path) as f:
    spec = yaml.safe_load(f)

components = spec.get("components", {}).get("schemas", {})

def extract_model_fields(schema: dict):
    props = schema.get("properties", {})
    fields = []
    for name, prop in props.items():
        if "$ref" in prop:
            fields.append({
                "name": name,
                "source_key": name,
                "is_nested": True,
                "subfields": [{"name": "id", "source_key": "id"}]  # Simplified nested logic
            })
        else:
            fields.append({
                "name": name,
                "source_key": name,
                "is_nested": False
            })
    return fields

generated_files = []

for resource in resources:
    schema = components.get(resource.capitalize()) or components.get(resource.title())
    if not schema:
        continue

    context = {
        "resource": resource,
        "clio_model_module": f"clio_client.models.{resource}",
        "clio_model_name": f"Clio{resource.capitalize()}",
        "unified_model_module": f"clio_sdk.models.{resource}",
        "unified_model_name": resource.capitalize(),
        "model_fields": extract_model_fields(schema)
    }

    rendered = template.render(context)
    output_file = output_dir / f"{resource}_transformer.py"
    output_file.write_text(rendered.strip())
    generated_files.append(str(output_file))

generated_files[:5]  # preview a few of the generated paths
