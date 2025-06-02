import asyncio
import aiofiles
import yaml
from pathlib import Path
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader, select_autoescape


async def load_yaml_async(path: Path):
    async with aiofiles.open(path, mode="r") as f:
        content = await f.read()
    return yaml.safe_load(content)


async def main():
    yaml_path = Path("/mnt/data/openapi_sdk.yaml")
    openapi_data = await load_yaml_async(yaml_path)

    env = Environment(
        loader=FileSystemLoader("/mnt/data"), autoescape=select_autoescape()
    )
    components = openapi_data.get("components", {}).get("schemas", {})
    tag_groups = openapi_data.get("x-tagGroups", [])
    paths = openapi_data.get("paths", {})

    operations_by_tag = defaultdict(list)

    def map_type(schema):
        if "$ref" in schema:
            return schema["$ref"].split("/")[-1]
        t = schema.get("type")
        return {
            "string": "str",
            "integer": "int",
            "boolean": "bool",
            "number": "float",
            "object": "dict",
            "array": f"list[{map_type(schema['items'])}]",
        }.get(t, "Any")

    for path, path_item in paths.items():
        for method, operation in path_item.items():
            if method not in ["get", "post", "put", "patch", "delete"]:
                continue
            op_id = operation.get("operationId")
            summary = operation.get("summary", "")
            description = operation.get("description", "")
            tags = operation.get("tags", [])
            params = operation.get("parameters", [])
            request_body = operation.get("requestBody", {})
            responses = operation.get("responses", {})
            response_type = "Any"

            if "200" in responses and "content" in responses["200"]:
                content = responses["200"]["content"]
                if "application/json" in content:
                    schema = content["application/json"].get("schema", {})
                    response_type = map_type(schema)

            args = []
            for param in params:
                name = param["name"]
                param_type = map_type(param.get("schema", {}))
                args.append(f"{name}: {param_type}")

            if request_body:
                content = request_body.get("content", {})
                if "application/json" in content:
                    schema = content["application/json"].get("schema", {})
                    body_type = map_type(schema)
                    args.append(f"body: {body_type}")

            signature = ", ".join(args)
            arg_forwarding = ", ".join([arg.split(":")[0] for arg in args])

            for tag in tags:
                operations_by_tag[tag].append(
                    {
                        "operation_id": op_id,
                        "summary": summary,
                        "description": description,
                        "signature": signature,
                        "arg_forwarding": arg_forwarding,
                        "response_type": response_type,
                        "method": method.upper(),
                        "path": path,
                    }
                )

    print(
        "✅ Return types and signatures now reflect Pydantic model names when available."
    )


asyncio.run(main())
