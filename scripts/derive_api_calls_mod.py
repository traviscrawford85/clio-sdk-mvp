from pathlib import Path

import pandas as pd
import yaml

OPENAPI_DIR = Path("openapi")
PATHS_DIR = OPENAPI_DIR / "paths"
COMPONENTS_DIR = OPENAPI_DIR / "components"
PARAMETERS_FILE = COMPONENTS_DIR / "parameters.yaml"
REQUEST_BODIES_FILE = COMPONENTS_DIR / "requestBodies.yaml"

def load_yaml(file_path):
    with open(file_path, encoding='utf-8') as f:
        return yaml.safe_load(f)

def resolve_ref(ref, components):
    try:
        if ref.startswith("#/components/parameters/"):
            name = ref.split("/")[-1]
            return components['parameters'].get(name, {})
        elif ref.startswith("#/components/requestBodies/"):
            name = ref.split("/")[-1]
            return components['requestBodies'].get(name, {})
    except Exception:
        return {}
    return {}

def parse_paths(components):
    data = []
    for path_file in PATHS_DIR.glob("*.yaml"):
        path_str = "/" + path_file.stem.replace("__", "/").replace("_.", ".").replace("_", "/")
        path_def = load_yaml(path_file)
        for method, details in path_def.get(path_str, path_def).items():
            if method not in ['get', 'post', 'put', 'patch', 'delete']:
                continue
            summary = details.get("summary", "")
            desc = details.get("description", "")
            op_id = details.get("operationId", "")
            request_body_ref = details.get("requestBody", {}).get("$ref")
            request_schema = resolve_ref(request_body_ref, components).get("description") if request_body_ref else None
            param_summaries = []
            for param in details.get("parameters", []):
                if isinstance(param, dict) and "$ref" in param:
                    resolved = resolve_ref(param["$ref"], components)
                    if resolved:
                        param_summaries.append(resolved.get("name", ""))
            data.append({
                "Path": path_str,
                "Method": method.upper(),
                "OperationId": op_id,
                "Summary": summary,
                "Description": desc,
                "Request Schema": request_schema,
                "Query Params": ", ".join(param_summaries)
            })
    return pd.DataFrame(data)

components = {
    "parameters": load_yaml(PARAMETERS_FILE).get("components", {}).get("parameters", {}),
    "requestBodies": load_yaml(REQUEST_BODIES_FILE).get("components", {}).get("requestBodies", {})
}

df_calls = parse_paths(components)

import ace_tools as tools; tools.display_dataframe_to_user(name="API Call Summary", dataframe=df_calls)
