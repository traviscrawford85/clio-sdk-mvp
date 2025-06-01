import re
from pathlib import Path

MODELS_DIR = Path("clio_sdk/models")
TARGETS = {"state", "event", "kind", "name", "status", "category"}

for path in MODELS_DIR.glob("*.py"):
    content = path.read_text()
    matches = re.findall(r"class (\w+)\(Enum\):", content)
    for enum_name in matches:
        if any(enum_name.lower().startswith(t) for t in TARGETS):
            print(f"{path.name}: {enum_name}")