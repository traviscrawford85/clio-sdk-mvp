import os
import re
from pathlib import Path

# Define the directory containing the models and adapters
BASE_DIRS = [Path("clio_sdk/models"), Path("clio_sdk/adapters")]

# Map of old class names to new module and class names
# Only include mappings where the class name has changed
enum_rename_map = {
    "Type3": ("timeentrytype", "TimeEntryType"),
    "Type6": ("matterbilltype", "MatterBillType"),
    "State1": ("matterstate", "MatterState"),
    "Kind1": ("contactkind", "ContactKind"),
    "Status1": ("taskstatus", "TaskStatus"),
    "Name1": ("contactnametype", "ContactNameType"),
    "Name3": ("communicationchanneltype", "CommunicationChannelType"),
    "Event1": ("matterevent", "MatterEvent"),
    "PendingEnum": ("paymentstatus", "PaymentStatus"),
    "DraftEnum": ("invoicestatus", "InvoiceStatus"),
    "InitialEnum": ("processstatus", "ProcessStatus"),
    "CreatedEnum": ("resourceevent", "ResourceEvent"),
    "NotStartedEnum": ("taskstate", "TaskState"),
    "State4": ("initializingenum", "InitializingEnum"),
    "Status3": ("pendingenum", "PendingEnum"),
    # Add more mappings as needed
}

def update_imports_and_references():
    for base_dir in BASE_DIRS:
        for file_path in base_dir.glob("**/*.py"):
            with file_path.open("r", encoding="utf-8") as f:
                content = f.read()

            original_content = content
            for old_class, (new_module, new_class) in enum_rename_map.items():
                # Update import statements
                import_pattern = rf"(from\s+\.\w+\s+import\s+){old_class}"
                import_replacement = rf"from .{new_module} import {new_class}"
                content = re.sub(import_pattern, import_replacement, content)

                # Update class references
                reference_pattern = rf"\b{old_class}\b"
                content = re.sub(reference_pattern, new_class, content)

            if content != original_content:
                with file_path.open("w", encoding="utf-8") as f:
                    f.write(content)
                print(f"✅ Updated: {file_path}")

update_imports_and_references()
