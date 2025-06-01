import os
import re
from pathlib import Path

MODELS_DIR = Path("clio_sdk/models")

# Map (class_name, tuple_of_enum_keys) to (NewClassName, new_file_stub)
rename_map = {
    # Type enums (unique)
    "Type": ("DocumentType", "documenttype"),
    "Type1": ("FolderType", "foldertype"),
    "Type2": ("DocumentOrFolderType", "documentorfoldertype"),
    "Type3": ("TimeEntryType", "timeentrytype"),
    "Type4": ("MatterType", "mattertype"),
    "Type5": ("OperatingType", "operatingtype"),
    "Type6": ("MatterBillType", "matterbilltype"),
    "Type7": ("AccountCalendarType", "accountcalendartype"),
    "Type8": ("EmailCommunicationType", "emailcommunicationtype"),
    "Type9": ("CompanyType", "companytype"),
    "Type10": ("UserGroupType", "usergrouptype"),
    "Type11": ("SimpleType", "simpletype"),
    "Type12": ("ActivityLineItemType", "activitylineitemtype"),
    "Type13": ("MatterLogEntryType", "matterlogentrytype"),
    "Type14": ("ContactType", "contacttype"),
    "Type17": ("MatterType", "mattertype"),
    "Type18": ("UtbmsTaskType", "utbmstasktype"),
    "Type19": ("FolderType", "foldertype"),
    "Type20": ("UserType", "usertype"),
    "Type21": ("ContactType", "contacttype"),
    "Type22": ("ManageUserType", "manageusertype"),
    "Type23": ("PercentageType", "percentagetype"),
    "Type24": ("FlatRateType", "flatratetype"),
    "Type25": ("EmailType", "emailtype"),
    "Type26": ("PersonType", "persontype"),
    "Type27": ("ActivityRelatedType", "activityrelatedtype"),
    # Disambiguated enums (use tuple of keys)
    ("TaskState", ("not_started", "queued", "in_progress", "empty", "failed", "completed")): ("TaskState", "taskstate"),
    ("DraftEnum", ("draft", "awaiting_approval", "awaiting_payment", "paid", "void", "deleted")): ("InvoiceStatus", "invoicestatus"),
    ("PendingEnum", ("pending", "authorized", "completed", "voided", "failed", "canceled", "requires_confirmation", "completed_requiring_allocation")): ("PaymentStatus", "paymentstatus"),
    ("InitializingEnum", ("initializing", "scheduling", "rescheduling", "scheduled", "attempting_delivery", "delivery_failed", "delivered", "delivery_skipped", "invalid_user")): ("DeliveryStatus", "deliverystatus"),
    ("NotStartedEnum", ("not_started", "queued", "in_progress", "failed", "completed", "empty")): ("TaskState", "taskstate"),
    ("PendingEnum", ("Pending", "Open", "Closed")): ("CaseStatus", "casestatus"),
    ("InitialEnum", ("initial", "queued", "processing", "failed", "completed")): ("ProcessStatus", "processstatus"),
    ("PendingEnum", ("pending", "in_progress", "in_review", "complete")): ("ReviewStatus", "reviewstatus"),
    ("PendingEnum", ("pending", "enabled", "suspended")): ("ActivationStatus", "activationstatus"),
    ("CreatedEnum", ("created", "updated", "deleted", "matter_opened", "matter_pended", "matter_closed")): ("ResourceEvent", "resourceevent"),
    ("MatterEvent", ("matter_created",)): ("MatterEvent", "matterevent"),
    # Kind enums
    "Kind": ("ResourceKind", "resourcekind"),
    "Kind1": ("ContactKind", "contactkind"),
    # Status enums
    "Status": ("ResourceStatus", "resourcestatus"),
    "Status1": ("TaskStatus", "taskstatus"),
    # Category enums
    "Category": ("ResourceCategory", "resourcecategory"),
    "Category1": ("DocumentCategory", "documentcategory"),
    # Name enums
    "Name": ("AddressType", "addresstype"),
    "Name1": ("ContactNameType", "contactnametype"),
    "Name3": ("CommunicationChannelType", "communicationchanneltype"),
    # Other specific enums
    "ProcessStatus": ("ProcessStatus", "processstatus"),
    "CaseStatus": ("CaseStatus", "casestatus"),
    "PaymentStatus": ("PaymentStatus", "paymentstatus"),
    "DeliveryStatus": ("DeliveryStatus", "deliverystatus"),
    "InvoiceStatus": ("InvoiceStatus", "invoicestatus"),
    "ReviewStatus": ("ReviewStatus", "reviewstatus"),
    "ActivationStatus": ("ActivationStatus", "activationstatus"),
}

def extract_enum_name(file_path: Path) -> str:
    """Extract the first Enum class name from a file."""
    content = file_path.read_text()
    match = re.search(r"class (\w+)\(Enum\):", content)
    return match.group(1) if match else ""

def extract_enum_values(file_path: Path) -> list:
    """Extract enum values from the first Enum class in a file."""
    content = file_path.read_text()
    match = re.search(r"class \w+\(Enum\):\s+((?:\s+\w+\s*=\s*\"[^\"]+\"\s*)+)", content, re.MULTILINE)
    if not match:
        return []
    body = match.group(1)
    values = re.findall(r'(\w+)\s*=\s*"([^"]+)"', body)
    return [v[1] for v in values]

def rename_enum_class_and_file(file_path: Path, new_class_name: str, new_file_name: str):
    """Rename the Enum class and its file with logging."""
    old_class_name = extract_enum_name(file_path)
    if not old_class_name:
        print(f"❌ No Enum class found in {file_path.name}")
        return

    content = file_path.read_text()
    updated_content = content.replace(f"class {old_class_name}(Enum):", f"class {new_class_name}(Enum):")
    file_path.write_text(updated_content)

    new_path = file_path.with_name(f"{new_file_name}.py")
    file_path.rename(new_path)
    print(f"✅ Renamed {file_path.name} -> {new_path.name}")
    print(f"   ↳ class {old_class_name} -> {new_class_name}")

def suggest_enum_name(values):
    """Suggest a new enum class name based on its values."""
    if not values:
        return "UnknownEnum", "unknownenum"
    # Use the first value + 'Type'
    base = values[0]
    sanitized = (
        base.replace("/", "_")
            .replace(" ", "_")
            .replace("-", "_")
            .replace("\\", "_")
            .replace(".", "_")
            .replace(":", "_")
            .replace("?", "_")
            .replace("*", "_")
            .replace("\"", "_")
            .replace("<", "_")
            .replace(">", "_")
            .replace("|", "_")
    )
    name = f"{sanitized.capitalize()}Type"
    return name, name.lower()

def extract_enum_name_and_values(file_path: Path):
    """Extract the first Enum class name and its keys from a file."""
    content = file_path.read_text()
    match = re.search(r"class (\w+)\(Enum\):\s+((?:\s+\w+\s*=\s*\"[^\"]+\"\s*)+)", content, re.MULTILINE)
    if not match:
        return None, ()
    class_name = match.group(1)
    body = match.group(2)
    keys = tuple(v[0] for v in re.findall(r'(\w+)\s*=', body))
    return class_name, keys

def run_enum_renamer():
    print("🔍 Scanning for Enum files in clio_sdk/models...")
    for path in MODELS_DIR.glob("*.py"):
        class_name, keys = extract_enum_name_and_values(path)
        if not class_name:
            continue
        key = (class_name, keys)
        if key in rename_map:
            new_class, stub = rename_map[key]
            rename_enum_class_and_file(path, new_class, stub)
        else:
            # fallback: try by class name only (legacy)
            if class_name in rename_map:
                new_class, stub = rename_map[class_name]
                rename_enum_class_and_file(path, new_class, stub)
            else:
                # fallback: suggest a name
                values = extract_enum_values(path)
                new_class, stub = suggest_enum_name(values)
                rename_enum_class_and_file(path, new_class, stub)

if __name__ == "__main__":
    run_enum_renamer()

# Ensure only correct imports from clio_sdk.models and clio_client.models are present, and remove any redefinitions of models in builder scripts. Only import the custom model where needed.
