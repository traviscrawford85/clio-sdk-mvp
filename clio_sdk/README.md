# Clio SDK Scaffold

This is a customizable Python SDK for Clio, tailored to your firm's needs.

## Structure

- `models/`: Pydantic models generated from OpenAPI or refined manually
- `client/`: Authenticated HTTP client with rate limiting and retries
- `queries/`: Reusable query builders for complex operations (e.g., joining Matters + Tasks)
- `utils/`: Helpers for date logic, pagination, batching, etc.

Run `openapi-python-client generate --path openapi_final_cleaned.yaml --config config.json` to generate models into `models/`.

## Custom Models & Adapters

The `schemas/from_expanded/` and `adapters/from_expanded/` folders are generated from the fully expanded OpenAPI spec (`expanded_full.yaml`).

- `schemas/from_expanded/` contains custom Pydantic models derived from Clio schemas
- `adapters/from_expanded/` contains transformation stubs between Clio SDK objects and your internal models

To regenerate:

```bash
python generate_expanded_models.py
