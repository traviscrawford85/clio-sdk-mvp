"""
Unified ClioSDK class that aggregates all tag group modules for discoverable, ergonomic API access.
Supports both static and dynamic loading of API modules for maximum flexibility and forward compatibility.
"""
import importlib
import os
from pathlib import Path
from typing import Any


class ClioSDK:
    def __init__(self, **client_kwargs: Any):
        """
        Loads all tag group API modules as attributes.
        Example: sdk.users.user_index(), sdk.matters.matter_create(), etc.
        """
        api_modules_dir = Path(__file__).parent.parent / "api_modules"
        # Try static import for known modules, fallback to dynamic for new/unknown
        static_modules = [
            "activity", "calendar", "client", "contact", "custom_field", "custom_field_value",
            "document", "matter", "note", "report", "statute", "task", "user", "webhook"
        ]
        for mod in static_modules:
            try:
                module = importlib.import_module(f"clio_sdk.api_modules.api_{mod}")
                setattr(self, mod, module)
            except ModuleNotFoundError:
                pass  # Not all modules may exist yet
        # Dynamically load any other modules in the directory
        for fname in os.listdir(api_modules_dir):
            if fname.endswith(".py") and not fname.startswith("__"):
                mod_name = fname[:-3]
                attr_name = mod_name.lower().replace("api_", "").replace("_", "")
                if not hasattr(self, attr_name):
                    module = importlib.import_module(f"clio_sdk.api_modules.{mod_name}")
                    setattr(self, attr_name, module)
        self._client_kwargs = client_kwargs

    def __getattr__(self, item):
        # This allows for dynamic attribute access
        return getattr(self, item)

# Usage example:
# from clio_sdk.client.clio_sdk import ClioSDK
# sdk = ClioSDK(token="...")
# sdk.users.user_index()
# sdk.matters.matter_create(data={...})
