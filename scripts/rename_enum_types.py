import os
import re
from pathlib import Path

# Define the directory containing the generated models
MODELS_DIR = Path("clio_sdk/models")

# Regular expression to match enum class definitions
ENUM_CLASS_REGEX = re.compile(r"class\s+(Type\d+|State\d*|Status\d*|Event\d*|Kind\d*|.*Type\d*)\s*\(Enum\):")

# Regular expression to match enum members
ENUM_MEMBER_REGEX = re.compile(r"^\s+(\w+)\s*=\s*['\"](.+?)['\"]", re.MULTILINE)

# Mapping of generic enum names to meaningful names
RENAME_MAPPING = {
    "Type9": "EntityType",
    "State1": "TaskState",
    "Event1": "MatterEvent",
    # Add more mappings as needed
}

def rename_enum_classes():
    for py_file in MODELS_DIR.glob("*.py"):
        with open(py_file, "r", encoding="utf-8") as file:
            content = file.read()

        matches = ENUM_CLASS_REGEX.findall(content)
        if not matches:
            continue

        new_content = content
        for match in matches:
            original_class_name = match
            new_class_name = RENAME_MAPPING.get(original_class_name)
            if not new_class_name:
                # Attempt to infer a new name based on enum members
                member_match = ENUM_MEMBER_REGEX.search(content)
                if member_match:
                    member_value = member_match.group(2)
                    inferred_name = f"{member_value.capitalize()}Enum"
                    new_class_name = inferred_name
                else:
                    continue  # Skip if unable to infer a name

            # Replace class definition
            new_content = re.sub(
                rf"class\s+{original_class_name}\s*\(Enum\):",
                f"class {new_class_name}(Enum):",
                new_content
            )
            # Replace references to the old class name
            new_content = re.sub(
                rf"\b{original_class_name}\b",
                new_class_name,
                new_content
            )
            print(f"Renamed {original_class_name} to {new_class_name} in {py_file.name}")

        # Write the updated content back to the file
        with open(py_file, "w", encoding="utf-8") as file:
            file.write(new_content)

if __name__ == "__main__":
    rename_enum_classes()
