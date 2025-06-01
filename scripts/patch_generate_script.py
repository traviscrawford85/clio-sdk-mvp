# Append transformer generation to the existing generate-sdk script
from pathlib import Path

generate_sdk_script_path = Path("scripts/generate_models_and_adapters.py")

with open(generate_sdk_script_path, "a") as f:
    f.write(
        """

# Generate transformer stubs
TRANSFORMER_DIR = "clio_sdk/transformers"
os.makedirs(TRANSFORMER_DIR, exist_ok=True)

for model in ["Contact", "Matter", "Task"]:
    input_import = f"from clio_client.models import {model} as Clio{model}"
    output_import = f"from clio_sdk.unified_models.{model.lower()} import {model} as Domain{model}"

    transformer_code = f\"\"\"{input_import}
{output_import}


class {model}Transformer:
    @staticmethod
    def from_clio(clio: Clio{model}) -> Domain{model}:
        return Domain{model}(
            # TODO: map fields explicitly
        )
\"\"\"

    transformer_file = os.path.join(TRANSFORMER_DIR, f"{model.lower()}_transformer.py")
    with open(transformer_file, "w") as tf:
        tf.write(transformer_code)

print("✅ Generated transformer stubs.")
"""
    )

"✅ Transformer stub generation appended to `scripts/generate_models_and_adapters.py`. This now runs as part of `make generate-sdk`."
