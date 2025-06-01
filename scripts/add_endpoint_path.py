from pathlib import Path

import yaml

paths_dir = Path("openapi/paths")

def wrap_with_path(file_path: Path):
    try:
        with file_path.open("r", encoding="utf-8") as f:
            content = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"❌ Error in {file_path.name}: {e}")
        return

    if not isinstance(content, dict) or any(k.startswith("/") for k in content.keys()):
        return  # already wrapped or invalid

    path_key = "/" + file_path.stem.replace("__", "/").replace("_.", ".").replace("_", "/")
    wrapped_content = {path_key: content}

    with file_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(wrapped_content, f, sort_keys=False)
    print(f"✅ Wrapped: {file_path.name} under path {path_key}")

# Apply to all path files
for path_file in paths_dir.glob("*.yaml"):
    wrap_with_path(path_file)
