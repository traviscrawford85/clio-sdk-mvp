import os

import inflection
import yaml

MODEL_DIR = "clio_sdk/models"
ADAPTER_DIR = "clio_sdk/adapter_frags"
TEST_DIR = "tests"
TEST_MODELS_DIR = os.path.join(TEST_DIR, "test_models")
TEST_ADAPTERS_DIR = os.path.join(TEST_DIR, "test_adapters")
os.makedirs(TEST_MODELS_DIR, exist_ok=True)
os.makedirs(TEST_ADAPTERS_DIR, exist_ok=True)

# Load OpenAPI spec
with open("openapi_final_cleaned.yaml", encoding="utf-8") as f:
    spec = yaml.safe_load(f)
schemas = spec.get("components", {}).get("schemas", {})

# Group schemas by resource
resource_map = {}
for schema_name in schemas:
    resource = inflection.underscore(schema_name).split("_")[0]
    resource_map.setdefault(resource, []).append(schema_name)

# Generate model and adapter tests
for resource, fragments in resource_map.items():
    model_class = inflection.camelize(resource)
    model_test_path = os.path.join(TEST_MODELS_DIR, f"test_{resource}.py")
    with open(model_test_path, "w") as f:
        f.write(f"from clio_sdk.models.{resource} import {model_class}\n\n")
        f.write(f"def test_{resource}_model_instantiation():\n")
        f.write(f"    model = {model_class}()\n")
        f.write(f"    assert isinstance(model, {model_class})\n")

    for fragment in fragments:
        snake_fragment = inflection.underscore(fragment)
        class_fragment = inflection.camelize(fragment)
        adapter_test_path = os.path.join(TEST_ADAPTERS_DIR, f"test_adapter_{snake_fragment}.py")
        with open(adapter_test_path, "w") as f:
            f.write(f"from clio_client.models.{snake_fragment} import {class_fragment} as Clio{class_fragment}\n")
            f.write(f"from clio_sdk.models.{resource} import {model_class}\n")
            f.write(f"from clio_sdk.adapter_frags.adapter_{snake_fragment} import (\n")
            f.write(f"    clio_to_internal_from_{snake_fragment},\n")
            f.write(f"    internal_to_clio_to_{snake_fragment},\n")
            f.write(")\n\n")
            f.write(f"def test_adapter_roundtrip_{snake_fragment}():\n")
            f.write(f"    clio = Clio{class_fragment}()\n")
            f.write(f"    sdk = clio_to_internal_from_{snake_fragment}(clio)\n")
            f.write(f"    assert isinstance(sdk, {model_class})\n")
            f.write(f"    roundtrip = internal_to_clio_to_{snake_fragment}(sdk)\n")
            f.write(f"    assert isinstance(roundtrip, Clio{class_fragment})\n")

"✅ Tests generated for all models and adapters in `tests/` directory."
