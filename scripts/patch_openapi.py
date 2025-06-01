from pathlib import Path

import yaml

UNIFIED_RESOURCES = {
    "Matter": ["MatterBase", "MatterExpanded"],
    "Contact": ["ContactBase", "ContactExpanded"],
    "Client": ["ClientBase", "ClientExpanded"],
    "Calendar": ["CalendarBase"],
    "Task": ["TaskBase", "TaskExpanded"],
    "Activity": ["ActivityBase", "ActivityExpanded"],
    "Document": ["DocumentBase", "DocumentExpanded"],
    "Note": ["NoteBase"],
    "CustomField": ["CustomFieldBase", "CustomFieldExtended"],
    "CustomFieldValue": ["CustomFieldValueBase", "CustomFieldValueExtended"],
    "Webhook": ["WebhookBase"],
    "User": ["UserBase", "UserExpanded"],
    "Report": ["ReportBase"],
}

INPUT_FILE = "openapi_final_cleaned.yaml"
OUTPUT_FILE = "openapi_resources_patched_allof.yaml"

with open(INPUT_FILE, "r") as f:
    spec = yaml.safe_load(f)

components = spec.setdefault("components", {}).setdefault("schemas", {})

for unified_name, parts in UNIFIED_RESOURCES.items():
    components[unified_name] = {
        "allOf": [{"$ref": f"#/components/schemas/{part}"} for part in parts]
    }

with open(OUTPUT_FILE, "w") as f:
    yaml.dump(spec, f, sort_keys=False)

print(f"✅ Patched spec saved to: {OUTPUT_FILE}")
