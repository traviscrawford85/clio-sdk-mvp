from pathlib import Path

# Recreate the transformer template after code environment reset
transformer_template_path = Path("clio-sdk-mvp/templates/transformer.py.jinja")
transformer_template_path.parent.mkdir(parents=True, exist_ok=True)

transformer_template_content = """
from typing import Any, Dict, Optional


class {{ resource_name }}Transformer:
    @staticmethod
    def from_clio(data: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return {
        {% for field in model_fields %}
            "{{ field.name }}": {% if field.is_nested %}
            {
            {% for sub in field.subfields %}
                "{{ sub.name }}": data.get("{{ field.source_key }}", {}).get("{{ sub.source_key }}"),
            {% endfor %}
            }
            {% else %}
            data.get("{{ field.source_key }}")
            {% endif %},
        {% endfor %}
        }
"""

transformer_template_path.write_text(transformer_template_content.strip())
transformer_template_path
