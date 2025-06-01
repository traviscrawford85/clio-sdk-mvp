import os

OPENAPI_ROOT = "./openapi"
COPILOT_PROMPT = """\
# copilot-audit: true
# Description: This file is part of a Python SDK for Clio, generated from an OpenAPI spec.
# Objective: Audit the clio_sdk/models and clio_sdk/adapters for modularity, correctness, and maintainability.
# Tasks:
# 1. For each fragmented model (schema) in the OpenAPI spec or clio_client/models:
#    - Ensure there is a dedicated adapter file: adapter_{fragment}.py.
#    - Each adapter file must import only the relevant Clio model (from clio_client.models) and the unified model (from clio_sdk.models).
#    - Each adapter file must generate only the conversion functions for that fragment (e.g., clio_to_internal_from_{fragment}, internal_to_clio_to_{fragment}).
# 2. Confirm that the codegen logic loops over each schema and generates a file per schema, not grouping multiple fragments into a single adapter.
# 3. Verify that all adapters use correct import casing and naming conventions (snake_case for filenames, PascalCase for class names).
# 4. Ensure unified models in clio_sdk/models are used throughout the SDK and business logic, and that only adapters import from clio_client.models.
# 5. Check that all conversion functions are present and correctly map fields between the fragmented and unified models.
# 6. Detect and flag any adapters that import unrelated models or contain unrelated conversion functions.
# 7. Output:
#    - A checklist of errors or improvements, preferably with line references.
#    - Suggestions for how to fix or improve structure, modularity, naming, and import hygiene.
#
# NOTE: This audit enforces a strict 1:1 mapping between fragmented models and adapters for clarity, modularity, and maintainability.
"""

def check_prompt_in_file(filepath: str) -> bool:
    with open(filepath, encoding="utf-8") as f:
        return COPILOT_PROMPT.strip().splitlines()[0] in f.read()

def prepend_prompt_to_yaml_files():
    for subdir, _, files in os.walk(OPENAPI_ROOT):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                path = os.path.join(subdir, file)
                if not check_prompt_in_file(path):
                    with open(path, encoding="utf-8") as f:
                        content = f.read()
                    with open(path, "w", encoding="utf-8") as fw:
                        fw.write(COPILOT_PROMPT + "\n" + content)
                    print(f"Prepended prompt to: {path}")

if __name__ == "__main__":
    prepend_prompt_to_yaml_files()
    print("Copilot prompt prepended to all YAML files where it was missing.")
# Ensure only correct imports from clio_sdk.models and clio_client.models are present, and remove any redefinitions of models in builder scripts. Only import the custom model where needed.
