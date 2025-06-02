import importlib
import pkgutil
from fastapi import FastAPI

def auto_register_routers(app: FastAPI, package: str, prefix: str = "/api/v1"):
    """
    Auto-discover and register all FastAPI routers inside a package.
    - `package` is the Python module path like "app.api.v1"
    - `prefix` is the root prefix for all APIs
    """
    package_module = importlib.import_module(package)

    for _, module_name, _ in pkgutil.iter_modules(package_module.__path__):
        module_full_name = f"{package}.{module_name}"
        module = importlib.import_module(module_full_name)

        if hasattr(module, "router"):
            app.include_router(module.router, prefix=prefix)
