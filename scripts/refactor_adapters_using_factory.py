from pathlib import Path

adapter_dir = Path("clio_sdk/unified_adapters")
transformer_dir = Path("clio_sdk/transformers")
resource_list = [
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

# Ensure the target directory exists before writing files
adapter_dir.mkdir(parents=True, exist_ok=True)

# Retry writing refactored adapter files
for resource in resource_list:
    resource_pascal = resource.replace("_", " ").title().replace(" ", "")
    file_path = adapter_dir / f"adapter_{resource}.py"
    adapter_code = f"""\
from clio_client.models.{resource} import {resource_pascal} as Clio{resource_pascal}
from clio_sdk.unified_models.{resource} import {resource_pascal} as Domain{resource_pascal}
from adapter_factory import make_model_adapter

adapter = make_model_adapter(
    source_model=Clio{resource_pascal},
    target_model=Domain{resource_pascal},
    name="{resource}"
)
"""
    with open(file_path, "w") as f:
        f.write(adapter_code)
