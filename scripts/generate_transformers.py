import importlib
from pathlib import Path
from typing import Type

from jinja2 import Environment, FileSystemLoader
from pydantic import BaseModel

from clio_sdk.resources import RESOURCES

# Setup Jinja2 environment
env = Environment(
    loader=FileSystemLoader("templates"), trim_blocks=True, lstrip_blocks=True
)

# Load transformer template
template = env.get_template("transformer_template.j2")

TRANSFORMER_OUTPUT_DIR = Path("clio_sdk/transformers")
TRANSFORMER_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

UNIFIED_MODEL_PACKAGE = "clio_sdk.unified_models"
CLIO_MODEL_PACKAGE = "clio_client.models"


def resolve_model_class(package: str, model_name: str) -> Type[BaseModel]:
    module_path = f"{package}.{model_name.lower()}"
    module = importlib.import_module(module_path)
    return getattr(module, model_name)


def get_model_fields(model_cls: Type[BaseModel]) -> list[str]:
    return list(model_cls.model_fields.keys())


for resource in RESOURCES:
    class_name = resource.capitalize()
    try:
        unified_cls = resolve_model_class(UNIFIED_MODEL_PACKAGE, class_name)
        clio_cls = resolve_model_class(CLIO_MODEL_PACKAGE, class_name)
    except (ImportError, AttributeError):
        print(f"⚠️  Skipping {resource}: model not found")
        continue

    unified_fields = set(get_model_fields(unified_cls))
    clio_fields = set(get_model_fields(clio_cls))
    common_fields = unified_fields & clio_fields

    content = template.render(
        resource=resource,
        clio_model_module=f"{CLIO_MODEL_PACKAGE}.{resource}",
        unified_model_module=f"{UNIFIED_MODEL_PACKAGE}.{resource}",
        clio_model_name=class_name,
        unified_model_name=class_name,
        fields=sorted(common_fields),
    )

    output_path = TRANSFORMER_OUTPUT_DIR / f"{resource}.py"
    with open(output_path, "w") as f:
        f.write(content)

print("✅ Transformer files generated for:", ", ".join(RESOURCES))
