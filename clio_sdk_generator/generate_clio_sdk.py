
import json
import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

def load_openapi(path: str):
    with open(path, "r") as f:
        if path.endswith(".yaml") or path.endswith(".yml"):
            return yaml.safe_load(f)
        return json.load(f)

def generate_sdk(openapi: dict, template_path: str, output_dir: str):
    env = Environment(loader=FileSystemLoader(template_path))
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    
    # Load derived groupings (if present)
    import yaml
    alias_map = {}
    grouping_file = Path(template_path) / "derived_api_groupings.yaml"
    if grouping_file.exists():
        with open(grouping_file) as f:
            groupings_data = yaml.safe_load(f)
            for group, details in groupings_data.items():
                for tag in details.get("tags", []):
                    alias_map[tag] = group

    # Wrap tag operations with alias name
    tag_to_operations = {}
    for path, methods in openapi.get("paths", {}).items():
        for method, operation in methods.items():
            tags = operation.get("tags", ["default"])
            for tag in tags:
                alias = alias_map.get(tag, tag)
                tag_to_operations.setdefault(alias, []).append({
                    "method": method.upper(),
                    "path": path,
                    "operation_id": operation.get("operationId", "unnamed_operation"),
                    "summary": operation.get("summary", ""),
                    "parameters": operation.get("parameters", []),
                    "request_body": operation.get("requestBody", {}),
                    "responses": operation.get("responses", {})
                })

    for path, methods in openapi.get("paths", {}).items():
        for method, operation in methods.items():
            tags = operation.get("tags", ["default"])
            for tag in tags:
                tag_to_operations.setdefault(tag, []).append({
                    "method": method.upper(),
                    "path": path,
                    "operation_id": operation.get("operationId", "unnamed_operation"),
                    "summary": operation.get("summary", ""),
                    "parameters": operation.get("parameters", []),
                    "request_body": operation.get("requestBody", {}),
                    "responses": operation.get("responses", {})
                })

    for tag, operations in tag_to_operations.items():
        tag_snake = tag.lower().replace(" ", "_")
        api_template = env.get_template("api_class.py.jinja")
        api_output = api_template.render(classname=tag, description=f"{tag} operations", endpoints=[])
        with open(Path(output_dir) / f"{tag_snake}_api.py", "w") as f:
            f.write(api_output)

        transformer_template = env.get_template("transformers/transformers.py.jinja")
        transformer_output = transformer_template.render(tag=tag, models=[])
        with open(Path(output_dir) / f"{tag_snake}_transformers.py", "w") as f:
            f.write(transformer_output)

    sdk_template = env.get_template("clio_sdk.py.jinja")
    sdk_output = sdk_template.render(tags=tag_to_operations.keys())
    with open(Path(output_dir) / "clio_sdk.py", "w") as f:
        f.write(sdk_output)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--openapi", required=True, help="Path to openapi.json or openapi.yaml")
    parser.add_argument("--templates", required=True, help="Path to Jinja templates")
    parser.add_argument("--output", required=True, help="Output directory for generated SDK")
    args = parser.parse_args()

    openapi = load_openapi(args.openapi)
    generate_sdk(openapi, args.templates, args.output)

    # DERIVED_OUTPUT

    # GROUPINGS_OUTPUT

    # SERVICE_INTERFACE_OUTPUT

    # SERVICE_IMPL_OUTPUT

    # INIT_AND_DOCS_OUTPUT
    init_template = env.get_template("__init__.py.jinja")
    doc_template = env.get_template("doc.md.jinja")

    export_targets = ["models", "services"]
    for folder in export_targets:
        subdir = Path(output_dir) / folder
        if subdir.exists():
            exports = [f.stem for f in subdir.glob("*.py") if not f.name.startswith("__")]
            init_output = init_template.render(exports=exports)
            with open(subdir / "__init__.py", "w") as f:
                f.write(init_output)

    # Generate docs/
    docs_dir = Path(output_dir) / "docs"
    docs_dir.mkdir(exist_ok=True)
    for tag, ops in tag_to_operations.items():
        doc_output = doc_template.render(tag=tag, operations=ops)
        with open(docs_dir / f"{tag.lower().replace(' ', '_')}.md", "w") as f:
            f.write(doc_output)
    
    service_impl_template = env.get_template("services/service_impl.py.jinja")
    for tag, ops in tag_to_operations.items():
        class_name = f"{tag.title().replace(' ', '')}"
        tag_snake = tag.lower().replace(' ', '_')
        impl_output = service_impl_template.render(classname=class_name, operations=ops, tag_snake=tag_snake)
        with open(Path(output_dir) / f"{tag_snake}_service_impl.py", "w") as f:
            f.write(impl_output)
    
    service_template = env.get_template("services/service_interface.py.jinja")
    for tag, ops in tag_to_operations.items():
        class_name = f"{tag.title().replace(' ', '')}"
        service_output = service_template.render(classname=class_name, operations=ops)
        with open(Path(output_dir) / f"{tag.lower().replace(' ', '_')}_service.py", "w") as f:
            f.write(service_output)
    
    x_tag_template = env.get_template("x_tag_groups.yaml.jinja")
    x_tag_output = x_tag_template.render(tags=tag_to_operations.keys())
    with open(Path(output_dir) / "x_tag_groups.yaml", "w") as f:
        f.write(x_tag_output)

    derived_groupings_template = env.get_template("derived_api_groupings.yaml.jinja")
    groupings = {"General": list(tag_to_operations.keys())}  # naive example grouping
    groupings_output = derived_groupings_template.render(groupings=groupings)
    with open(Path(output_dir) / "derived_api_groupings.yaml", "w") as f:
        f.write(groupings_output)
    
    derived_template = env.get_template("derived_api_calls.yaml.jinja")
    derived_yaml = derived_template.render(tag_to_operations=tag_to_operations)
    with open(Path(output_dir) / "derived_api_calls.yaml", "w") as f:
        f.write(derived_yaml)
    
