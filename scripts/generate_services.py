from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from clio_sdk.resources import RESOURCES

# Setup Jinja2 environment
env = Environment(
    loader=FileSystemLoader("templates"), trim_blocks=True, lstrip_blocks=True
)

# Load service template
template = env.get_template("service_template.j2")

# Define the directory where services will be written
services_dir = Path("clio_sdk/services")
services_dir.mkdir(parents=True, exist_ok=True)

# Generate service files from template
for resource in RESOURCES:
    class_name = resource.capitalize()
    content = template.render(resource=resource, ClassName=class_name)
    file_path = services_dir / f"{resource}_service.py"
    with open(file_path, "w") as f:
        f.write(content)

print("✅ Service files generated for:", ", ".join(RESOURCES))
