from pathlib import Path
from jinja2 import Environment

# Output directories
interface_output_dir = Path("/mnt/data/generated_sdk_interfaces")
service_output_dir = Path("/mnt/data/generated_sdk_services")
interface_output_dir.mkdir(exist_ok=True)
service_output_dir.mkdir(exist_ok=True)

env = Environment()

# Async interface template
interface_template_text = '''"""
{{ interface_name }} Interface
"""
from typing import Any, Protocol

class I{{ interface_name }}Service(Protocol):
    {% for method in methods %}
    async def {{ method.name }}(self, {{ method.signature }}) -> {{ method.response_type or 'Any' }}:
        ...
    {% endfor %}
'''
interface_template = env.from_string(interface_template_text)

# Async service template
service_template_text = '''"""
{{ class_name }}Service Implementation
"""
from typing import Any
from clio_async_client.client import AuthenticatedClient
from clio_sdk.interfaces.i_{{ class_name.lower() }}_service import I{{ class_name }}Service

class {{ class_name }}Service(I{{ class_name }}Service):
    def __init__(self, client: AuthenticatedClient):
        self.client = client

    {% for method in methods %}
    async def {{ method.name }}(self, {{ method.signature }}) -> {{ method.response_type or 'Any' }}:
        # TODO: Implement using self.client and await the appropriate async method
        raise NotImplementedError("Implement {{ method.name }}")
    {% endfor %}
'''
service_template = env.from_string(service_template_text)

# Generate interfaces and services
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

    # Interface
    interface_output = interface_template.render(
        interface_name=interface_name, methods=methods
    )
    interface_output_file = (
        interface_output_dir / f"i_{interface_name.lower()}_service.py"
    )
    interface_output_file.write_text(interface_output)

    # Service
    service_output = service_template.render(class_name=interface_name, methods=methods)
    service_output_file = service_output_dir / f"{interface_name.lower()}_service.py"
    service_output_file.write_text(service_output)

print(f"✅ Generated async interfaces in {interface_output_dir}")
print(f"✅ Generated async services in {service_output_dir}")
