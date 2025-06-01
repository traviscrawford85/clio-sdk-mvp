from collections import Counter

import yaml

# Load the YAML file
file_path = "openapi_resources_patched_fixed.yaml"
with open(file_path, "r") as stream:
    openapi_spec = yaml.safe_load(stream)

# Recursive function to collect all enum values from the spec
def find_duplicate_enums(data, path=""):
    duplicates = []
    if isinstance(data, dict):
        for k, v in data.items():
            new_path = f"{path}/{k}" if path else k
            if k == "enum" and isinstance(v, list):
                enum_counts = Counter(v)
                dupes = {item for item, count in enum_counts.items() if count > 1}
                if dupes:
                    duplicates.append((new_path, list(dupes)))
            else:
                duplicates.extend(find_duplicate_enums(v, new_path))
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            duplicates.extend(find_duplicate_enums(item, f"{path}[{idx}]"))
    return duplicates

# Search for duplicate enums
duplicate_enum_paths = find_duplicate_enums(openapi_spec)
duplicate_enum_paths
