from pathlib import Path

# Create templates directory and template files for services and transformers
templates_dir = Path("templates")
templates_dir.mkdir(exist_ok=True)

# Jinja2 service template
service_template = """
from clio_sdk.interfaces.i_{{ resource }}_service import I{{ class_name }}Service
from clio_sdk.unified_models.{{ resource }} import {{ class_name }}, {{ class_name }}UpdateInputModel
from clio_sdk.unified_adapters import get_adapter
from clio_sdk.queries.{{ resource }} import get_{{ resource }}_by_id, list_{{ resource }}s, build_full_update_request
from clio_sdk.client import ClioClient
from typing import List, Optional


class {{ class_name }}Service(I{{ class_name }}Service):
    def __init__(self, client: ClioClient):
        self.client = client
        self.adapter = get_adapter("{{ resource }}")

    async def get_{{ resource }}(self, {{ resource }}_id: int) -> Optional[{{ class_name }}]:
        data = await get_{{ resource }}_by_id({{ resource }}_id)
        if data:
            return self.adapter["from_clio"](data)
        return None

    async def list_{{ resource }}s(self) -> List[{{ class_name }}]:
        raw = await list_{{ resource }}s()
        return [self.adapter["from_clio"](item) for item in raw]

    async def update_{{ resource }}(self, {{ resource }}_id: int, update: {{ class_name }}UpdateInputModel) -> bool:
        req = build_full_update_request(update)
        resp = await self.client.patch(f"/{{ resource }}s/{{ '{{' }}{{ resource }}_id{{ '}}' }}", data=req.model_dump())
        return bool(resp)
"""

# Jinja2 transformer template
transformer_template = """
from typing import Optional
from {{ clio_model_module }} import {{ clio_model_name }}
from {{ unified_model_module }} import {{ unified_model_name }}
from clio_sdk.adapter_factory.transformer import register_transformer

def transform_{{ resource }}_fields(data: dict, context: Optional[dict] = None) -> dict:
    return {
    {% for field in fields %}
        "{{ field }}": data.get("{{ field }}"),
    {% endfor %}
    }

register_transformer("{{ resource }}", transform_{{ resource }}_fields)
"""

# Save templates
(templates_dir / "service_template.j2").write_text(service_template.strip())
(templates_dir / "transformer_template.j2").write_text(transformer_template.strip())

"✅ Jinja2 templates created for service and transformer generation."
