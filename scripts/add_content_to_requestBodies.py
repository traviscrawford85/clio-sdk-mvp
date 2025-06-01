import os
import re
from pathlib import Path

import yaml

OPENAPI_ROOT = Path("openapi")
COMPONENT_TYPES = ["requestBodies"]


def bundle_component(component_type):
    print(f"📦 Bundling {component_type} into components/{component_type}.yaml...")
    source_dir = OPENAPI_ROOT / "components" / component_type
    output_path = OPENAPI_ROOT / "components" / f"{component_type}.yaml"

    bundled = {"components": {component_type: {}}}
    for file in source_dir.glob("*.yaml"):
        name = file.stem
        with file.open("r", encoding="utf-8") as f:
            content = yaml.safe_load(f)
            if content:
                bundled["components"][component_type][name] = content
                print(f"✅ Added: {name}")

    with output_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(bundled, f, sort_keys=False)


def rewrite_refs(component_type):
    print(f"🔁 Rewriting $ref to #/components/{component_type}/X")
    ref_pattern = re.compile(fr"\.\/components\/{component_type}\.yaml#\/components\/{component_type}\/([\w\-]+)")

    def normalize_refs(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "$ref" and isinstance(v, str):
                    match = ref_pattern.match(v)
                    if match:
                        name = match.group(1)
                        obj[k] = f"#/components/{component_type}/{name}"
                else:
                    normalize_refs(v)
        elif isinstance(obj, list):
            for item in obj:
                normalize_refs(item)

    for root, _, files in os.walk(OPENAPI_ROOT):
        for fname in files:
            if fname.endswith(".yaml") or fname.endswith(".yml"):
                path = Path(root) / fname
                try:
                    with path.open("r", encoding="utf-8") as f:
                        content = yaml.safe_load(f)
                except Exception as e:
                    print(f"❌ Skipping {path}: {e}")
                    continue

                if not content:
                    continue

                original = yaml.dump(content)
                normalize_refs(content)
                modified = yaml.dump(content)

                if original != modified:
                    with path.open("w", encoding="utf-8") as f:
                        yaml.safe_dump(content, f, sort_keys=False)
                    print(f"✏️ Rewritten refs in: {path}")


if __name__ == "__main__":
    for comp in COMPONENT_TYPES:
        bundle_component(comp)
        rewrite_refs(comp)

    print("\n🎉 Done! Parameters, responses, and requestBodies inlined.")
