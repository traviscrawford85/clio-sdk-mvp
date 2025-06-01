import os

# Define directory structure for pytest suite
base_dir = "tests"
subdirs = ["test_models", "test_adapters"]

# Create directories and __init__.py
for sub in subdirs:
    path = os.path.join(base_dir, sub)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "__init__.py"), "w") as f:
        f.write("")

# Create conftest.py for shared fixtures later
with open(os.path.join(base_dir, "conftest.py"), "w") as f:
    f.write("# Shared fixtures can go here\n")

# Create placeholder test examples
example_model_test = """from clio_sdk.models.client import Client

def test_client_model_instantiation():
    model = Client(id=123, name="Test Client", data={})
    assert model.id == 123
    assert model.name == "Test Client"
"""

example_adapter_test = """from clio_client.models.client_base import ClientBase as ClioClientBase
from clio_sdk.models.client import Client
from clio_sdk.adapter_frags.adapter_client_base import (
    clio_to_internal_from_client_base,
    internal_to_clio_to_client_base
)

def test_adapter_roundtrip_client_base():
    clio = ClioClientBase(id=42, name="Alpha")
    sdk = clio_to_internal_from_client_base(clio)
    assert isinstance(sdk, Client)
    roundtrip = internal_to_clio_to_client_base(sdk)
    assert roundtrip.id == clio.id
"""

# Write example test files
with open(os.path.join(base_dir, "test_models", "test_client.py"), "w") as f:
    f.write(example_model_test)

with open(os.path.join(base_dir, "test_adapters", "test_adapter_client_base.py"), "w") as f:
    f.write(example_adapter_test)

print("✅ Pytest suite scaffolded under `tests/` with starter test files.")
