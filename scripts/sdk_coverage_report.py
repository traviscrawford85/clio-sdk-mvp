from pathlib import Path

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
    "statute",
]

# Base paths for adapters and transformers
adapter_base = Path("clio_sdk/adapter_factory")
transformer_base = adapter_base / "transformers"

# Gather missing files
missing_adapters = []
missing_transformers = []

for resource in RESOURCES:
    adapter_path = adapter_base / f"adapter_{resource}.py"
    transformer_path = transformer_base / f"{resource}_transformer.py"
    if not adapter_path.exists():
        missing_adapters.append(str(adapter_path))
    if not transformer_path.exists():
        missing_transformers.append(str(transformer_path))

import pandas as pd
import ace_tools as tools

# Combine results into a DataFrame for display
df = pd.DataFrame({
    "Resource": RESOURCES,
    "Adapter Exists": [res not in missing_adapters for res in [f"clio_sdk/adapter_factory/adapter_{r}.py" for r in RESOURCES]],
    "Transformer Exists": [res not in missing_transformers for res in [f"clio_sdk/adapter_factory/transformers/{r}_transformer.py" for r in RESOURCES]],
})
tools.display_dataframe_to_user(name="SDK Coverage Report", dataframe=df)
