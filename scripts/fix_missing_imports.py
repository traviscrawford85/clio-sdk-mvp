import re
from pathlib import Path

MODELS_DIR = Path("clio_sdk/models")
DEFINED_CLASSES = {}

def snake_to_pascal(snake: str) -> str:
    return ''.join(word.capitalize() for word in snake.split('_'))

def pascal_to_snake(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

# Step 1: Build map of class name → file stem
for path in MODELS_DIR.glob("*.py"):
    if path.name == "__init__.py":
        continue
    content = path.read_text()
    for match in re.findall(r"class (\w+)\(.*?\):", content):
        DEFINED_CLASSES[match] = path.stem

# Step 2: Scan for unresolved base classes
for path in MODELS_DIR.glob("*.py"):
    if path.name == "__init__.py":
        continue

    content = path.read_text()
    imports = set(re.findall(r"from \.([\w_]+) import (\w+)", content))
    base_classes = re.findall(r"class \w+\((\w+)\):", content)

    new_imports = []
    for base in base_classes:
        if base not in DEFINED_CLASSES:
            # Try fallback from snake_case to PascalCase
            base_pascal = snake_to_pascal(path.stem)
            if base_pascal in DEFINED_CLASSES:
                base = base_pascal

        if base in DEFINED_CLASSES:
            module = DEFINED_CLASSES[base]
            import_line = f"from .{module} import {base}"
            if not any(base in imp for _, imp in imports):
                print(f"🔧 Adding missing import in {path.name}: {import_line}")
                new_imports.append(import_line)

    if new_imports:
        lines = content.splitlines()
        insert_at = 0
        for i, line in enumerate(lines):
            if line.startswith("from __future__"):
                insert_at = i + 1
        for imp in reversed(new_imports):
            lines.insert(insert_at, imp)
        path.write_text("\n".join(lines) + "\n")

# Ensure only correct imports from clio_sdk.models and clio_client.models are present, and remove any redefinitions of models in builder scripts. Only import the custom model where needed.
