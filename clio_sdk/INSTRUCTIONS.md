### INSTRUCTIONS.md

# GitHub Copilot Instructions for clio-sdk

## Overview

This repo contains:

-   `clio_sdk/clio_client/`: OpenAPI-generated models and API client (do not edit manually)
-   `clio_sdk/`: Unified Pydantic models, adapters, transformers, services, interfaces

## Copilot Guidance

-   Prefer typing hints on all functions (`-> Optional[Model]`)
-   Use `model_dump()` / `model_validate()` for conversions
-   Interface-first design (e.g., `IMatterService`, `IAdapterFactory`)
-   Place tests under `tests/` and name them `test_<module>.py`

## Architecture

```text
clio_sdk/
├── clio_client/           # Generated client
├── unified_models/        # Pydantic base models
├── adapter_factory/       # Adapters & transformers
├── services/              # Logic using client
├── interfaces/            # Contracts
├── queries/               # Query cases
├── commands/              # Mutations
```

## Update OpenAPI client

Run:

```bash
make update-client
```

Which calls:

```bash
bash scripts/update_openapi.sh
```

---

### scripts/update_openapi.sh

#!/bin/bash
set -e

# Adjust path to your actual openapi.json

OPENAPI_JSON="../openapi.json"
CLIENT_TARGET="clio_sdk/clio_client"

rm -rf "$CLIENT_TARGET"
mkdir -p "$CLIENT_TARGET"

# Regenerate using openapi-python-client

openapi-python-client generate --path "$OPENAPI_JSON" --output "$CLIENT_TARGET" --config scripts/client-config.json

# Optional: Symlink external schema files if needed

# ln -s /some/external/resource "$CLIENT_TARGET/resources"
