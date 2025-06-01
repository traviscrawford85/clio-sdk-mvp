import ast
from pathlib import Path

SERVICES_DIR = Path("clio_sdk/services")
INTERFACES_DIR = Path("clio_sdk/interfaces")


def get_interface_name(service_filename: str) -> str:
    return f"I{service_filename.replace('_service.py', '').capitalize()}Service"


def get_service_class_name(service_filename: str) -> str:
    return f"{service_filename.replace('_service.py', '').capitalize()}Service"


def check_interface_compliance(service_path: Path, expected_interface: str) -> bool:
    with open(service_path, "r") as file:
        tree = ast.parse(file.read(), filename=str(service_path))

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for base in node.bases:
                if isinstance(base, ast.Name) and base.id == expected_interface:
                    return True
    return False


results = []
for service_file in SERVICES_DIR.glob("*_service.py"):
    expected_interface = get_interface_name(service_file.name)
    class_name = get_service_class_name(service_file.name)
    interface_path = INTERFACES_DIR / f"i_{service_file.name}"
    has_interface = interface_path.exists()
    implements_interface = (
        check_interface_compliance(service_file, expected_interface)
        if has_interface
        else False
    )

    results.append(
        {
            "service": service_file.name,
            "expected_interface": expected_interface,
            "interface_exists": has_interface,
            "implements_interface": implements_interface,
        }
    )

import ace_tools as tools
import pandas as pd

tools.display_dataframe_to_user(
    name="Service Interface Compliance", dataframe=pd.DataFrame(results)
)
