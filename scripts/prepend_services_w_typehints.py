from pathlib import Path

# Constants
SERVICES_DIR = Path("clio_sdk/services")
ANNOTATION_TEMPLATE = '''"""
@service-interface: {interface_name}
@return: {return_type}
@args: {args}
"""'''


def annotate_service_methods():
    for file_path in SERVICES_DIR.glob("*_service.py"):
        with file_path.open("r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        in_class = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("class") and "Service" in stripped:
                class_name = stripped.split()[1].split("(")[0]
                interface_name = f"I{class_name}"
                in_class = True
            elif (
                in_class
                and stripped.startswith("def ")
                and not stripped.startswith("def __")
            ):
                method_name = stripped.split()[1].split("(")[0]
                args_part = stripped[stripped.find("(") + 1 : stripped.find(")")]
                args = args_part.split(", ")
                args = [arg for arg in args if arg != "self"]
                return_type = "Unknown"  # Could parse more with ast if desired
                annotation = ANNOTATION_TEMPLATE.format(
                    interface_name=interface_name,
                    return_type=return_type,
                    args=", ".join(args),
                )
                new_lines.append(annotation + "\n")

            new_lines.append(line)

        with file_path.open("w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"🔧 Annotated methods in: {file_path.name}")


annotate_service_methods()
