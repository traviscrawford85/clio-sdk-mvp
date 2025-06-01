import pandas as pd
import yaml

OPENAPI_FILE = "openapi_sdk.yaml"


def load_openapi(file_path):
    with open(file_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve_ref(ref, components):
    if not ref:
        return {}
    try:
        if ref.startswith("#/components/parameters/"):
            name = ref.split("/")[-1]
            return components.get("parameters", {}).get(name, {})
        elif ref.startswith("#/components/requestBodies/"):
            name = ref.split("/")[-1]
            return components.get("requestBodies", {}).get(name, {})
    except Exception:
        return {}
    return {}


def extract_request_schema(request_body, components):
    if not request_body:
        return None
    if "$ref" in request_body:
        resolved = resolve_ref(request_body["$ref"], components)
        return resolved.get("description", "Ref only")
    if "content" in request_body:
        return request_body.get("description", "Inline body")
    return None


def extract_query_params(params, components):
    summaries = []
    for param in params:
        if "$ref" in param:
            resolved = resolve_ref(param["$ref"], components)
            summaries.append(resolved.get("name", ""))
        elif param.get("in") == "query":
            summaries.append(param.get("name", ""))
    return ", ".join(summaries)


def parse_paths(openapi):
    components = openapi.get("components", {})
    data = []
    for path, methods in openapi.get("paths", {}).items():
        for method, details in methods.items():
            if method not in ["get", "post", "put", "patch", "delete"]:
                continue
            summary = details.get("summary", "")
            desc = details.get("description", "")
            op_id = details.get("operationId", "")
            request_body = details.get("requestBody")
            request_schema = extract_request_schema(request_body, components)
            param_list = details.get("parameters", [])
            query_params = extract_query_params(param_list, components)
            data.append(
                {
                    "Path": path,
                    "Method": method.upper(),
                    "OperationId": op_id,
                    "Summary": summary,
                    "Description": desc,
                    "Request Schema": request_schema,
                    "Query Params": query_params,
                }
            )
    return pd.DataFrame(data)


if __name__ == "__main__":
    openapi = load_openapi(OPENAPI_FILE)
    df = parse_paths(openapi)
    df.to_csv("api_call_summary.csv", index=False)
    print("✅ API call summary saved to api_call_summary.csv")
