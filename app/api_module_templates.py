from jinja2 import Environment, FileSystemLoader
import yaml

# Load your openapi.yaml
with open("openapi.yaml") as f:
    spec = yaml.safe_load(f)

tag_groups = spec.get("x-tagGroups", [])
paths = spec["paths"]

# Organize operations by tag
operations_by_tag = {}
for path, path_item in paths.items():
    for method, op in path_item.items():
        if method in {"get", "post", "put", "delete"}:
            for tag in op.get("tags", []):
                operations_by_tag.setdefault(tag, []).append(
                    {
                        "name": op["operationId"],
                        "description": op.get("summary", ""),
                    }
                )clio-sdk-mvp/scripts/jinja_scripts

# Render
env = Environment(loader=FileSystemLoader("custom_templates"))
template = env.get_template("api_module_by_group.py.jinja")
output = template.render(tag_groups=tag_groups, operations_by_tag=operations_by_tag)

with open("clio_sdk/generated/api_modules.py", "w") as f:
    f.write(output)
