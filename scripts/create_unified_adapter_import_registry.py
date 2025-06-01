from pathlib import Path

adapter_dir = Path("clio_sdk/unified_adapters")
init_file = adapter_dir / "__init__.py"

lines = [
    "# Auto-generated import registry for unified adapters\n",
    "from adapter_factory.base import adapter_registry\n\n",
]

for file in adapter_dir.glob("adapter_*.py"):
    module_name = file.stem
    import_line = f"from .{module_name} import adapter as {module_name}_adapter\n"
    register_line = f"adapter_registry['{module_name.replace('adapter_', '')}'] = {module_name}_adapter\n"
    lines.append(import_line)
    lines.append(register_line)

with open(init_file, "w") as f:
    f.writelines(lines)

init_file.read_text()
