from pathlib import Path
from typing import List

# Define constants
RESOURCES = [
    "matter",
    "contact",
    "client",
    "calendar",
    "task",
    "activity",
    "document",
    "note",
    "custom_field",
    "custom_field_value",
    "webhook",
    "user",
    "report",
]

TRANSFORMER_DIR = Path("clio_sdk/transformers")
TRANSFORMER_DIR.mkdir(parents=True, exist_ok=True)

# Generate transformer stubs
for resource in RESOURCES:
    model = resource.title().replace("_", "")
    transformer_path = TRANSFORMER_DIR / f"{resource}_transformer.py"

    input_import = f"from clio_client.models import {model} as Clio{model}"
    output_import = (
        f"from clio_sdk.unified_models.{resource} import {model} as Domain{model}"
    )
    factory_import = "from adapter_factory.base import make_model_adapter\n"

    transformer_code = f"""{input_import}
{output_import}
{factory_import}


def transform_{resource}_fields(data: dict, context: dict = None) -> dict:
    # TODO: Add field mapping logic here
    return data


adapter = make_model_adapter(
    Clio{model},
    Domain{model},
    name="{resource}",
)
"""

    transformer_path.write_text(transformer_code)

"✅ Transformer stubs for all selected resources have been created."
