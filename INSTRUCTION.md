
# 🧠 Copilot Custom Project Guidance

## 🎯 Purpose

This project integrates Clio's OpenAPI backend into a structured Python SDK using FastAPI, Clio's OpenAPI client (`clio_client`), and a custom interface-driven architecture (`clio_sdk`). Copilot should support strongly typed, auto-refactorable, and maintainable workflows across:

- Unified models
- Adapter factories
- Transformers
- Interfaces and service implementations
- Async API integration

---
## 🗂️ Project Structure Overview
```
clio_client/ # OpenAPI-generated client (DO NOT EDIT)
clio_sdk/
├── unified_models/ # Pydantic unified models
├── adapter_factory/
│ ├── base.py # Adapter interface + factory
│ ├── adapters/ # Adapter implementations (e.g., adapter_matter.py)
│ ├── transformers/ # Transformer stubs and impls
│ ├── i_adapter_service.py # IAdapterFactory interface
├── interfaces/ # Abstract interfaces (e.g., IMatterService)
├── services/ # Service implementations (e.g., MatterService)
├── queries/ # Query use-cases
├── commands/ # Command use-cases
clio/ # FastAPI app logic, token store
tests/ # Pytest for all units (adapters, transformers, services)
.copilot/ # Copilot prompts and config (opt-in)
```
=======
from pathlib import Path

instructions_md = """

# Copilot Custom Project Guidance

## 🎯 Purpose

This is a Clio Integration backend project using FastAPI, the OpenAPI-generated Clio SDK (`clio_client`), and a custom model/adapter layer (`clio_sdk`). Copilot should assist by inferring correct types, managing imports, suggesting refactors, and validating adapter-model sync.


---

## 📦 Project Structure Overview

- `clio_client/`: auto-generated OpenAPI client with fragmented models.
- `clio_sdk/`:
  - `models/`: unified Pydantic models (one per resource).
  - `adapter_frags/`: converters between `clio_client.models.*` and `clio_sdk.models.*`.
- `clio/`: FastAPI app and utility logic (e.g., token store, builder patterns).
- `tests/`: Pytest test suite for models and adapters.

---

## ✅ Copilot Coding Style & AI Prompts

### 🧠 Typing

- Always annotate functions with return types (e.g., `-> Optional[Matter]`)
- Prefer `List`, `Optional`, `dict`, `Literal`, and `Union` when needed
- Use `BaseModel.model_dump()` and `.model_validate()` to convert between representations

### 🧱 Adapter Factories

- Implement via `make_model_adapter(source, target, name)`
- Use `adapter = get_adapter("matter")`
- Enforce `IAdapterFactory` (`from_clio`, `to_clio`) interface contract

### 🧩 Transformers

- Use `register_transformer("matter", transform_matter_fields)`
- Call transformers from inside adapter `from_clio()`
- Keep transformers pure and context-aware (e.g., `def fn(data, context)`)

---

## 🔁 Unified Adapters
```
from clio_sdk.adapter_factory import get_adapter
adapter = get_adapter("matter")
adapter.from_clio(clio_obj)
adapter.to_clio(unified_obj)
```

**Pattern:**
```python
from clio_sdk.adapter_factory.base import make_model_adapter
adapter = make_model_adapter(ClioModel, UnifiedModel, name="matter")
```
---
## 🧪 Tests

* Put each test in tests/adapter_factory/test_{resource}_adapter.py

* Validate both from_clio() and to_clio()

* Use mypy, black, and pytest in CI
=======
## ✅ Copilot Coding Style Guide

### 🚩 Imports

- Use **absolute imports**:
  - `from clio_sdk.models.matter import Matter`
  - `from clio_client.models.matter_base import MatterBase as ClioMatterBase`
- Never use `clio_client.models.*` in routes, services, or internal logic — only in adapters.

### 🧠 Typing

- Annotate return types (`-> MyModel`) everywhere.
- Use `Optional`, `List`, `Literal`, `Union` as appropriate.
- Apply `.to_dict()` or adapter conversions before JSON serialization.

---

## 🔁 Adapters and Model Conversions

**Adapters must:**

- Match the `clio_client` model name in `adapter_{fragment}.py`
- Convert to/from `clio_sdk` unified model using:
  - `clio_to_internal_from_*`
  - `internal_to_clio_to_*`
- Use other adapter functions for nested references or lists.

---

## 🌐 FastAPI Integration

```python
from clio_client.api.matters_api import MattersApi
from clio.token_store import get_access_token

def get_authenticated_api(api_cls):
    token = get_access_token()
    return api_cls(ApiClient(Configuration(token=token)))


```
## 🔍 Quality Enforcement
CI should include:

✅ black for formatting

✅ isort for import order

✅ mypy for type enforcement

✅ pytest for correctness

✅ sonarqube (optional) for deeper insights

---
## 🚀 GitHub Copilot / AI
Add prompts to .copilot/config.json for model-wide guidance

Use docstring-style prompts in services, adapters, and transformers for refactorable stubs

Enable Copilot pull request suggestions and PR audits
---
## 👤 Author
Travis Crawford  
Clio Certified Partner | Full Stack Developer | LegalTech Architect <br>
📧 solutionpartner@cfelab.com | [linkedin](https://www.linkedin.com/in/crawford-t)

=======
from clio_client.api_client import ApiClient, Configuration

def get_authenticated_api(api_cls):
    token = get_access_token()
    config = Configuration()
    config.api_key["Authorization"] = token
    config.api_key_prefix["Authorization"] = "Bearer"
    return api_cls(ApiClient(config))
```

