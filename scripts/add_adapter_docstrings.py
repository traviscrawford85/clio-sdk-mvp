from pathlib import Path

ADAPTER_DIR = Path("clio_sdk/adapters")

def insert_docstring(file_path: Path):
    with open(file_path) as f:
        lines = f.readlines()

    new_lines = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("def convert_sdk_to_") or stripped.startswith("def convert_"):
            indent = " " * (len(line) - len(line.lstrip()))
            docstring = f'{indent}"""\n'
            if "sdk_to_" in stripped:
                docstring += f"{indent}Converts a Pydantic model from clio_client to clio_sdk format.\n"
                docstring += f"{indent}Assumes the source model is Pydantic v2 and uses .model_dump().\n"
            else:
                docstring += f"{indent}Converts a Pydantic model from clio_sdk to clio_client format.\n"
                docstring += f"{indent}Assumes the target model is Pydantic v2 and can be instantiated from dict.\n"
            docstring += f'{indent}"""\n'
            new_lines.append(line)
            new_lines.append(docstring)
        else:
            new_lines.append(line)

    with open(file_path, "w") as f:
        f.writelines(new_lines)

# Apply to all adapter files
for file in ADAPTER_DIR.glob("adapter_*.py"):
    insert_docstring(file)

"✅ Adapter docstrings updated for Pydantic v2 usage (.model_dump())"
