# copilot-enabled: true
# Description: This file is part of the Clio SDK, which standardizes adapters, services, and transformers for interacting with the Clio API using unified Pydantic models.
# Objective: Refactor and maintain this module to follow current SDK standards.
# Constraints:
# - Use interfaces from `clio_sdk.interfaces`.
# - Use adapters from `clio_sdk.adapter_factory` via `get_adapter()`.
# - Ensure services return unified models from `clio_sdk.unified_models`.
# - Match method signatures to their declared interfaces.
# - Maintain type safety with `mypy`.
# - Format with `black`, import-sort with `isort`, and validate with `flake8`.
# Tasks:
# 1. Refactor outdated service/adapters/transformers to match latest structure.
# 2. Fill in missing logic based on Clio OpenAPI client responses or SDK models.
# 3. Write new test stubs under `tests/` for any new methods.
# 4. Annotate any assumptions or TODOs inline with `# copilot: consider`.
