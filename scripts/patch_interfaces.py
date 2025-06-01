import ast
from pathlib import Path
from typing import Dict, List, Set

# Constants
SERVICES_PATH = Path("clio_sdk/services")
INTERFACES_PATH = Path("clio_sdk/interfaces")
INTERFACES_PATH.mkdir(parents=True, exist_ok=True)

RESOURCES = [
    "matter",
    "contact",
    "client",
    "calendar",
    "task",
    "activity",
    "document",
    "note",
    "custom_field",
    "custom_field_value",
    "webhook",
    "user",
    "report",
]


def extract_service_methods(service_code: str):
    tree = ast.parse(service_code)
    methods = []
    all_types: Set[str] = set()

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and not item.name.startswith("_"):
                    args = []
                    for arg in item.args.args[1:]:  # Skip 'self'
                        if hasattr(arg, "annotation") and arg.annotation:
                            arg_type = ast.unparse(arg.annotation)
                            all_types.add(arg_type)
                            args.append(f"{arg.arg}: {arg_type}")
                        else:
                            args.append(arg.arg)

                    return_type = ast.unparse(item.returns) if item.returns else "None"
                    if return_type != "None":
                        all_types.add(return_type)

                    methods.append((item.name, args, return_type))

    return methods, all_types


def create_interface_code(
    class_name: str, resource: str, methods: List[tuple], used_types: Set[str]
):
    model_imports = sorted(
        t
        for t in used_types
        if t not in {"int", "str", "bool", "float", "dict", "list", "None"}
    )
    imports_block = (
        "from abc import ABC, abstractmethod\nfrom typing import List, Optional\n"
    )
    if model_imports:
        imports_block += f"from clio_sdk.unified_models.{resource} import {', '.join(model_imports)}\n\n"
    else:
        imports_block += "\n"

    method_defs = "\n".join(
        f"    @abstractmethod\n    def {name}(self, {', '.join(args)}) -> {return_type}:\n        pass"
        for name, args, return_type in methods
    )
    return f"{imports_block}class I{class_name}Service(ABC):\n{method_defs if method_defs else '    pass'}\n"


def patch_interfaces():
    for resource in RESOURCES:
        service_file = SERVICES_PATH / f"{resource}_service.py"
        if not service_file.exists():
            continue

        class_name = resource.capitalize()

        with service_file.open("r", encoding="utf-8") as f:
            service_code = f.read()

        methods, types = extract_service_methods(service_code)
        interface_code = create_interface_code(class_name, resource, methods, types)

        interface_path = INTERFACES_PATH / f"i_{resource}_service.py"
        with interface_path.open("w", encoding="utf-8") as f:
            f.write(interface_code)

        print(f"✅ Patched interface: {interface_path}")


patch_interfaces()
