import os
from importlib import import_module
from pathlib import Path
from typing import Type

from jinja2 import Template
from pydantic import BaseModel

from clio_sdk.resources import RESOURCES

TEMPLATE = Template(
    """from clio_client.models import {{ clio_model }} as ClioModel
from clio_sdk.unified_models import {{ unified_model }} as UnifiedModel
from typing import Any
from pydantic import BaseModel

def from_clio(clio_obj: ClioModel) -> UnifiedModel:
    return UnifiedModel(**clio_obj.model_dump())

def to_clio(sdk_obj: UnifiedModel) -> ClioModel:
    return ClioModel(**sdk_obj.model_dump())

adapter = {
    "from_clio": from_clio,
    "to_clio": to_clio,
}
"""
)

OUTPUT_DIR = Path("clio_sdk/adapter_factory/adapters")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def resolve_model_class(module_path: str, class_name: str) -> Type[BaseModel]:
    try:
        module = import_module(module_path)
        return getattr(module, class_name)
    except ImportError:
        print(f"❌ ImportError: Module '{module_path}' not found")
        raise
    except AttributeError:
        print(
            f"❌ AttributeError: Class '{class_name}' not found in module '{module_path}'"
        )
        raise


for resource in RESOURCES:
    unified_model = resource.capitalize()
    clio_model = resource.capitalize()

    try:
        resolve_model_class(f"clio_sdk.unified_models.{resource}", unified_model)
    except Exception:
        print(f"⚠️  Skipping {resource}: unified model '{unified_model}' not found")
        continue

    try:
        resolve_model_class(f"clio_client.models.{resource}", clio_model)
    except Exception:
        print(f"⚠️  Skipping {resource}: clio model '{clio_model}' not found")
        continue

    rendered = TEMPLATE.render(
        clio_model=clio_model,
        unified_model=unified_model,
    )

    output_path = OUTPUT_DIR / f"{resource}_adapter.py"
    with open(output_path, "w") as f:
        f.write(rendered)
    print(f"✅ Adapter generated: {output_path}")
