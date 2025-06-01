from jinja2 import Template
from pathlib import Path

RESOURCES = [
    "matter", "contact", "client", "calendar", "task", "activity", "document", "note",
    "custom_field", "custom_field_value", "webhook", "user", "report"
]

ADAPTER_TEMPLATE = Template(
    'from clio_client.models.{{ resource }} import Clio{{ resource|capitalize }}\n'
    'from clio_sdk.models.{{ resource }} import {{ resource|capitalize }}\n'
    'from clio_sdk.adapter_factory.base import make_model_adapter\n\n'
    'adapter = make_model_adapter(Clio{{ resource|capitalize }}, {{ resource|capitalize }}, name="{{ resource }}")\n'
)

ADAPTERS_DIR = Path("adapter_factory/adapters")
ADAPTERS_DIR.mkdir(parents=True, exist_ok=True)

for resource in RESOURCES:
    file_path = ADAPTERS_DIR / f"{resource}_adapter.py"
    content = ADAPTER_TEMPLATE.render(resource=resource)
    file_path.write_text(content)
