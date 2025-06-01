import os

MODELS_DIR = "clio_sdk/models"
INIT_FILE = os.path.join(MODELS_DIR, "__init__.py")

def snake_to_camel(snake_str):
    return "".join(word.title() for word in snake_str.split("_"))

def main():
    entries = os.listdir(MODELS_DIR)
    model_files = [
        f for f in entries
        if f.endswith(".py") and f != "__init__.py"
    ]

    lines = [
        "# Auto-generated init to expose all model classes",
        "from __future__ import annotations",
        "",
    ]

    for filename in sorted(model_files):
        module = filename[:-3]
        lines.append(f"from .{module} import *")

    with open(INIT_FILE, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"✅ Wrote aggregate __init__.py with {len(model_files)} model modules.")

if __name__ == "__main__":
    main()
