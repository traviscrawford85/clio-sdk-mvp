.PHONY: help generate-models generate-unified-adapters generate-transformers generate-sdk derive clean-sdk clean-adapters clean-transformers clean-tests generate-tests run-tests aggregate-models-init adapters transformers all

# SDK Paths
CLIO_SDK_MODELS=clio_sdk/unified_models
CLIO_SDK_ADAPTERS=clio_sdk/unified_adapters
CLIO_SDK_TRANSFORMERS=clio_sdk/transformers
TESTS_DIR=tests

help:
	@echo "🛠️  Clio SDK Development Tasks"
	@echo ""
	@echo "Usage: make <target>"
	@echo ""
	@echo "SDK Generation:"
	@echo "  generate-single            Generate a single unified model + adapter (RESOURCE=custom_field_value)"
	@echo "  generate-models            Generate Pydantic models for clio_sdk from OpenAPI spec"
	@echo "  generate-unified-adapters  Generate unified adapters with wrapper support"
	@echo "  generate-transformers      Generate transformer stubs for unified models"
	@echo "  generate-sdk               Generate full SDK (models, adapters, transformers)"
	@echo ""
	@echo "Advanced:"
	@echo "  derive                     Derive query logic from models or OpenAPI spec"
	@echo "  generate-tests             Generate pytest test stubs for models and adapters"
	@echo "  run-tests                  Run all tests with pytest"
	@echo ""
	@echo "Cleanup:"
	@echo "  clean-sdk                  Remove all generated SDK models, adapters, and transformers"
	@echo "  clean-adapters             Remove only generated adapters"
	@echo "  clean-transformers         Remove only generated transformers"
	@echo "  clean-tests                Remove all generated tests"

generate-single:
	@echo "🎯 Generating one or more unified models + adapters. Usage: make generate-single RESOURCE=\"custom_field_value contact\""
	@python3 scripts/generate_single_model_and_adapter.py $(RESOURCE)

generate-models:
	@echo "🧬 Generating clio_sdk models from OpenAPI spec..."
	datamodel-codegen \
	  --input openapi_final_cleaned.yaml \
	  --input-file-type openapi \
	  --output clio_sdk/models/models.py \
	  --output-model-type pydantic_v2.BaseModel \
	  --field-constraints \
	  --use-standard-collections \
	  --use-double-quotes \
	  --force-optional
	$(MAKE) aggregate-models-init

aggregate-models-init:
	@echo "📦 Aggregating model imports in __init__.py..."
	PYTHONPATH=. python3 scripts/aggregate_models_init.py

generate-unified-adapters:
	@echo "🔁 Generating unified adapters with wrapper support..."
	PYTHONPATH=. python3 scripts/generate_unified_adapters.py

generate-transformers:
	@echo "🔁 Generating transformer stubs for unified models..."
	PYTHONPATH=. python3 scripts/generate_transformers.py

generate-sdk:
	@echo "⚙️  Generating full clio_sdk (models + adapters + transformers + services)..."
	PYTHONPATH=. python3 scripts/generate_models_and_adapters.py
	PYTHONPATH=. python3 scripts/generate_transformers.py
	PYTHONPATH=. python3 scripts/generate_services.py

derive:
	@echo "📡 Deriving query logic and API operations..."
	python3 scripts/derive_api_calls.py

generate-tests:
	@echo "🧪 Generating pytest suite for models and adapters..."
	python3 scripts/generate_tests.py

run-tests:
	@echo "🚀 Running pytest suite..."
	PYTHONPATH=. pytest -v tests/

clean-sdk:
	@echo "🧼 Cleaning all clio_sdk model, adapter, and transformer files..."
	find $(CLIO_SDK_MODELS) -type f -name "*.py" -delete
	find $(CLIO_SDK_MODELS) -type d -name "__pycache__" -exec rm -r {} +
	find $(CLIO_SDK_ADAPTERS) -type f -name "*.py" -delete
	find $(CLIO_SDK_ADAPTERS) -type d -name "__pycache__" -exec rm -r {} +
	find $(CLIO_SDK_TRANSFORMERS) -type f -name "*.py" -delete
	find $(CLIO_SDK_TRANSFORMERS) -type d -name "__pycache__" -exec rm -r {} +

clean-adapters:
	@echo "🧼 Cleaning only generated adapters..."
	find $(CLIO_SDK_ADAPTERS) -type f -name "*.py" -delete
	find $(CLIO_SDK_ADAPTERS) -type d -name "__pycache__" -exec rm -r {} +

clean-transformers:
	@echo "🧽 Cleaning generated transformer files..."
	find $(CLIO_SDK_TRANSFORMERS) -type f -name "*.py" -delete
	find $(CLIO_SDK_TRANSFORMERS) -type d -name "__pycache__" -exec rm -r {} +

clean-tests:
	@echo "🧽 Removing generated test files..."
	rm -rf $(TESTS_DIR)/test_models/*.py
	rm -rf $(TESTS_DIR)/test_adapters/*.py

adapter_py_files = $(wildcard adapter_factory/adapters/*_adapter.py)
transformer_py_files = $(wildcard adapter_factory/transformers/*_transformer.py)

adapters:
	python scripts/patch_adapters.py

transformers:
	python scripts/transformer_helper.py

all: adapters transformers
