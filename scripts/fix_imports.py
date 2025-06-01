import os

ADAPTER_DIR = "clio_sdk/adapters"
MODEL_DIR = "clio_sdk/models"
CLIO_CLIENT_MODEL_DIR = "clio_client/models"

def snake_to_pascal(name):
    return ''.join(word.capitalize() for word in name.split('_'))

def fix_adapter_imports():
    for fname in os.listdir(ADAPTER_DIR):
        if not fname.startswith("adapter_") or not fname.endswith(".py"):
            continue
        fragment = fname[len("adapter_"):-3]  # e.g., 'user_base'
        adapter_path = os.path.join(ADAPTER_DIR, fname)
        with open(adapter_path, encoding="utf-8") as f:
            lines = f.readlines()

        # Determine correct imports
        resource = fragment.split('_')[0]
        unified_model_import = f"from clio_sdk.models.{resource} import {snake_to_pascal(resource)}\n"
        clio_model_import = f"from clio_client.models.{fragment} import {snake_to_pascal(fragment)} as Clio{snake_to_pascal(fragment)}\n"

        # Remove old model imports
        new_lines = []
        for line in lines:
            if (
                line.startswith("from clio_sdk.models.")
                or line.startswith("from clio_client.models.")
            ):
                continue  # skip old imports
            new_lines.append(line)

        # Insert correct imports at the top (after docstring/comments)
        insert_at = 0
        for i, line in enumerate(new_lines):
            if not line.strip().startswith("#") and not line.strip().startswith("\"\"\""):
                insert_at = i
                break
        new_lines = (
            new_lines[:insert_at]
            + [clio_model_import, unified_model_import]
            + new_lines[insert_at:]
        )

        # Write back the fixed file
        with open(adapter_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

    print("✅ Adapter imports have been audited and corrected.")

if __name__ == "__main__":
    fix_adapter_imports()