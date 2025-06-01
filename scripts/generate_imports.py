import re
from pathlib import Path

MODELS_DIR = Path("clio_sdk/models")
INIT_FILE = MODELS_DIR / "__init__.py"

from typing import Optional


def extract_class_name(file_path: Path) -> Optional[str]:
    content = file_path.read_text()
    match = re.search(r"class (\w+)\(Enum\):", content)
    return match.group(1) if match else None

def generate_init_imports():
    lines = []
    for py_file in sorted(MODELS_DIR.glob("*.py")):
        if py_file.name == "__init__.py":
            continue
        class_name = extract_class_name(py_file)
        if class_name:
            module = py_file.stem
            lines.append(f"from .{module} import {class_name}")
    INIT_FILE.write_text("\n".join(lines) + "\n")
    print(f"✅ Updated {INIT_FILE} with {len(lines)} imports.")

if __name__ == "__main__":
    generate_init_imports()

# Ensure only correct imports from clio_sdk.models and clio_client.models are present, and remove any redefinitions of models in builder scripts. Only import the custom model where needed.
