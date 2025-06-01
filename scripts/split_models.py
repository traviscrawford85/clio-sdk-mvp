import os
import re
from pathlib import Path

INPUT_PATH = Path("clio_sdk/models/models.py")
OUTPUT_DIR = Path("clio_sdk/models")
INIT_FILE = OUTPUT_DIR / "__init__.py"

def extract_classes(source: str):
    imports = []
    classes = {}
    current_class = []
    current_name = None
    capture = False

    for line in source.splitlines(keepends=True):
        if line.startswith("class ") or line.startswith("class\n") or line.strip().startswith("class "):
            if current_name:
                classes[current_name] = "".join(current_class)
            match = re.match(r"class (\w+)\(", line)
            current_name = match.group(1) if match else None
            current_class = [line]
            capture = True
        elif capture and line.startswith(("class ", "def ", "from ", "import ")):
            current_class.append(line)
        elif capture:
            current_class.append(line)
        elif line.startswith(("from ", "import ", "class ", "class\n")):
            imports.append(line)

    if current_name and current_class:
        classes[current_name] = "".join(current_class)

    return "".join(imports), classes

def write_model_files(imports, classes):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    model_names = []

    for name, body in classes.items():
        path = OUTPUT_DIR / f"{name.lower()}.py"
        with open(path, "w", encoding="utf-8") as f:
            f.write(imports + "\n" + body)
        model_names.append(name)

    with open(INIT_FILE, "w", encoding="utf-8") as f:
        for name in model_names:
            f.write(f"from .{name.lower()} import {name}\n")
        f.write("\n__all__ = [\n")
        for name in model_names:
            f.write(f"    \"{name}\",\n")
        f.write("]\n")

if __name__ == "__main__":
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        source = f.read()

    imports, classes = extract_classes(source)
    write_model_files(imports, classes)
