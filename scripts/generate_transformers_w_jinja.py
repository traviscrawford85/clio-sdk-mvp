import importlib
import inspect
import os
from typing import Type

from jinja2 import Template
from pydantic import BaseModel

UNIFIED_MODEL_PACKAGE = "clio_sdk.unified_models"
CLIO_MODEL_PACKAGE = "clio_client.models"
TRANSFORMER_OUTPUT_DIR = "adapter_factory/transformers"

TRANSFORM_TEMPLATE = Template(
    """
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
)


def get_model_fields(model_cls: Type[BaseModel]) -> list[str]:
    return list(model_cls.model_fields.keys())


def resolve_model_class(package: str, model_name: str) -> Type[BaseModel]:
    module_path = f"{package}.{model_name.lower()}"
    module = importlib.import_module(module_path)
    return getattr(module, model_name)


def generate_transformer(resource: str):
    unified_model_name = resource.capitalize()
    clio_model_name = resource.capitalize()

    unified_model_module = f"{UNIFIED_MODEL_PACKAGE}.{resource}"
    clio_model_module = f"{CLIO_MODEL_PACKAGE}.{resource}"

    try:
        unified_cls = resolve_model_class(UNIFIED_MODEL_PACKAGE, unified_model_name)
        clio_cls = resolve_model_class(CLIO_MODEL_PACKAGE, clio_model_name)
    except (ImportError, AttributeError):
        print(f"⚠️  Skipping {resource}: model not found")
        return

    unified_fields = set(get_model_fields(unified_cls))
    clio_fields = set(get_model_fields(clio_cls))
    common_fields = unified_fields & clio_fields

    rendered = TRANSFORM_TEMPLATE.render(
        resource=resource,
        clio_model_module=clio_model_module,
        unified_model_module=unified_model_module,
        clio_model_name=clio_model_name,
        unified_model_name=unified_model_name,
        fields=sorted(common_fields),
    )

    output_path = os.path.join(TRANSFORMER_OUTPUT_DIR, f"{resource}.py")
    with open(output_path, "w") as f:
        f.write(rendered)
    print(f"✅ Transformer generated for: {resource}")


def generate_all():
    resources = ["matter", "contact", "task", "user"]
    for resource in resources:
        generate_transformer(resource)


if __name__ == "__main__":
    generate_all()
