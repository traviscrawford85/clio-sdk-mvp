from collections import defaultdict
import yaml
import pandas as pd

# --- BEGIN: Extract records from OpenAPI spec ---
import json

# Load your OpenAPI spec (adjust path as needed)
with open("clio_sdk/openapi_sdk.yaml", "r") as f:
    import yaml as yamllib
    openapi_spec = yamllib.safe_load(f)

records = []
for path, methods in openapi_spec.get("paths", {}).items():
    for method, op in methods.items():
        if method.lower() not in {"get", "post", "put", "delete", "patch"}:
            continue
        tags = ", ".join(op.get("tags", []))
        operation_id = op.get("operationId", "")
        summary = op.get("summary", "")
        description = op.get("description", "")
        records.append({
            "Path": path,
            "Method": method.upper(),
            "Tags": tags,
            "OperationId": operation_id,
            "Summary": summary,
            "Description": description,
        })

# Optional: Display DataFrame for review
df_spec_grouping = pd.DataFrame(records)
try:
    import ace_tools as tools; tools.display_dataframe_to_user(name="Derived API Groupings", dataframe=df_spec_grouping)
except ImportError:
    pass
# --- END: Extract records ---

# --- BEGIN: Group tags and output x-tagGroups YAML ---
group_map = defaultdict(set)
for row in records:
    if row["Tags"]:
        for tag in [t.strip() for t in row["Tags"].split(",")]:
            op = row["OperationId"].split("#")[0] if "#" in row["OperationId"] else row["OperationId"]
            group_map[tag].add(op)

suggested_tag_groups = [{"name": tag, "tags": sorted(list(ops))} for tag, ops in group_map.items()]

output_path = "clio_sdk/suggested_x_tagGroups.yaml"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(yaml.dump({"x-tagGroups": suggested_tag_groups}, sort_keys=False, allow_unicode=True))
print(f"✅ Saved suggested x-tagGroups to {output_path}")
# --- END: Group tags and output ---
