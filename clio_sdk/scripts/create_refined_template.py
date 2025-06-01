"""{{ tag_group.name }} API Module"""

from clio_sdk.http import request
from clio_sdk.models import *
from typing import Any
from pathlib import Path
from jinja2 import Template

# Define where to save the Jinja template
sdk_templates_dir = Path(__file__).parent.parent / "sdk_templates"
sdk_templates_dir.mkdir(exist_ok=True)
template_path = sdk_templates_dir / "api_module.py.jinja"

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

# Overwrite the template with detailed version
with open(template_path, "w") as f:
    f.write(detailed_template)

# Render full module outputs for all tag groups
rendered_files_dir = Path("rendered_modules")
rendered_files_dir.mkdir(exist_ok=True)

# Assume tag_groups, operations_by_tag, and template are defined elsewhere in the script or imported
# If not, add logic to load or define them as needed
# Example placeholder:
tag_groups = []  # Should be a list of tag group dicts
operations_by_tag = {}  # Should be a dict mapping tag to operations

template = Template(detailed_template)

for tag_group in tag_groups:
    module_code = template.render(tag_group=tag_group, operations_by_tag=operations_by_tag)
    module_filename = f"{tag_group['name'].replace(' ', '_').lower()}.py"
    module_path = rendered_files_dir / module_filename
    with open(module_path, "w") as f:
        f.write(module_code)

# Confirm output file paths
rendered_file_paths = [str(p) for p in rendered_files_dir.glob("*.py")]
rendered_file_paths
