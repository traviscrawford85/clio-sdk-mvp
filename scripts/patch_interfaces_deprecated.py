"""
This script regenerate Pythonic interfaces from your service implementations with proper type hints, ABC base class, and @abstractmethod decorators
"""

from pathlib import Path
import ast
import logging

logging.basicConfig(level=logging.INFO, format="🔧 %(message)s")

services_path = Path("clio_sdk/services")
interfaces_path = Path("clio_sdk/interfaces")
interfaces_path.mkdir(parents=True, exist_ok=True)

# Hardcoded method signatures for known services
METHOD_SIGNATURES = {
    "matter": {
        "get_matter": "self, matter_id: int) -> Optional[Matter]",
        "update_matter": "self, matter_id: int, update: MatterUpdateInputModel) -> bool",
        "list_matters": "self) -> List[Matter]",
        "get_blank_custom_fields": "self, matter_id: int) -> List[dict]",
        "delete_blank_custom_fields": "self, matter_id: int) -> bool",
        "batch_update_status": "self, matter_ids: List[int], status: str) -> List[bool]",
        "batch_update_responsible_staff": "self, matter_ids: List[int], user_id: int) -> List[bool]",
    },
    # Add more resource method signatures here as needed
}


def extract_service_methods(service_code: str):
    tree = ast.parse(service_code)
    method_defs = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and not item.name.startswith("_"):
                    method_defs.append(item.name)
    return method_defs


def create_interface_content(class_name: str, methods: list):
    resource = class_name.lower()
    interface_name = f"I{class_name}Service"
    imports = [
        "from abc import ABC, abstractmethod",
        "from typing import List, Optional",
        f"from clio_sdk.unified_models.{resource} import {class_name}, {class_name}UpdateInputModel",
    ]
    header = "\n".join(imports) + "\n\n"
    class_def = f"class {interface_name}(ABC):"
    if resource in METHOD_SIGNATURES:
        method_defs = "\n".join(
            f"    @abstractmethod\n"
            f"    def {name}({METHOD_SIGNATURES[resource][name]}:\n"
            f"        pass"
            for name in methods
            if name in METHOD_SIGNATURES[resource]
        )
    else:
        # Fallback: no type hints
        method_defs = "\n".join(
            f"    @abstractmethod\n"
            f"    def {name}(self, *args, **kwargs):\n"
            f"        pass"
            for name in methods
        )
    return f"{header}{class_def}\n{method_defs}\n"


def patch_interfaces():
    logging.info("🔍 Scanning for service implementations...")
    for service_file in services_path.glob("*_service.py"):
        resource = service_file.stem.replace("_service", "")
        class_name = resource.capitalize()

        with service_file.open("r") as f:
            service_code = f.read()

        methods = extract_service_methods(service_code)
        interface_code = create_interface_content(class_name, methods)

        interface_file = interfaces_path / f"i_{resource}_service.py"
        with interface_file.open("w") as f:
            f.write(interface_code)

        logging.info(f"✅ Interface patched: {interface_file.name}")

    logging.info("🎉 All interfaces updated.")


if __name__ == "__main__":
    patch_interfaces()
