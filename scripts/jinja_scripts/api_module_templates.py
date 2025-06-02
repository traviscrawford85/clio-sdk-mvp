from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
from pathlib import Path

# Set up Jinja environment
template_dir = "templates"
os.makedirs(template_dir, exist_ok=True)
env = Environment(loader=FileSystemLoader(template_dir), autoescape=select_autoescape())

# Create a refined Jinja template with type hints, parameters, return types, and method integration
detailed_template = """\"\"\"{{ tag_group.name }} API Module\"\"\"

from clio_sdk.http import request
from clio_sdk.models import *
from typing import Any

{% for tag in tag_group.tags %}
# Tag: {{ tag }}
{% for op in operations_by_tag.get(tag, []) %}
def {{ op.operation_id|replace('#', '_')|lower }}(
    {{ 'id: int, ' if '/{id}' in op.path else '' }}**kwargs: Any
) -> Any:
    \"\"\"{{ op.summary }}\"\"\"
    return request(
        method="{{ op.method }}",
        path=f"{{ op.path }}",
        **kwargs
    )

{% endfor %}
{% endfor %}
"""

template_path = os.path.join(template_dir, "api_module_by_group.py.jinja")
with open(template_path, "w") as f:
    f.write(detailed_template)

# Render full module outputs for all tag groups
rendered_files_dir = Path("/mnt/data/rendered_modules")
rendered_files_dir.mkdir(exist_ok=True)

template = env.get_template("api_module_by_group.py.jinja")

for tag_group in tag_groups:
    module_code = template.render(
        tag_group=tag_group, operations_by_tag=operations_by_tag
    )
    module_filename = f"{tag_group['name'].replace(' ', '_').lower()}.py"
    module_path = rendered_files_dir / module_filename
    with open(module_path, "w") as f:
        f.write(module_code)

# Confirm output file paths
rendered_file_paths = [str(p) for p in rendered_files_dir.glob("*.py")]
rendered_file_paths
