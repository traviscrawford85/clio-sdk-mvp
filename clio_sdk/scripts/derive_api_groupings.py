# Extract key path-level metadata from the unified OpenAPI spec to suggest groupings

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

df_spec_grouping = pd.DataFrame(records)
import ace_tools as tools; tools.display_dataframe_to_user(name="Derived API Groupings", dataframe=df_spec_grouping)
