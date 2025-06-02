from pathlib import Path
from jinja2 import Environment

# Async interface Jinja template
correct_interface_template_text = '''"""
{{ interface_name }} Interface
"""
from typing import Any, Protocol
import typing

class I{{ interface_name }}Service(Protocol):
    {% for method in methods %}
    async def {{ method.name }}(self, {{ method.signature }}) -> {{ method.response_type or 'Any' }}:
        ...
    {% endfor %}
'''

# Save the interface template
interface_template_path = Path("clio_sdk/interface_service.jinja")
interface_template_path.write_text(correct_interface_template_text)

# Prepare Jinja2 environment
env = Environment()
interface_template = env.from_string(correct_interface_template_text)

# Assume tag_groups, operations_by_tag, and interface_output_dir are defined elsewhere in your script

for group in tag_groups:
    group_name = group["name"]
    interface_name = group_name.replace(" ", "")
    group_tags = group["tags"]

    methods = []
    for tag in group_tags:
        for op in operations_by_tag.get(tag, []):
            methods.append(
                {
                    "name": op["operation_id"].replace("#", "_").lower(),
                    "signature": op["signature"],
                    "response_type": op["response_type"],
                }
            )

    output = interface_template.render(interface_name=interface_name, methods=methods)
    interface_output_file = (
        interface_output_dir / f"i_{interface_name.lower()}_service.py"
    )
    interface_output_file.write_text(output)

interface_output_dir.name
