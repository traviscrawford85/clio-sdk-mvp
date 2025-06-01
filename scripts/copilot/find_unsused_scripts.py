from pathlib import Path
import re
import json

# Paths to check
base_dir = Path.cwd()
scripts_dir = base_dir / "scripts"
resources_path = base_dir / "resources.py"
copilot_config_path = base_dir / ".copilot" / "config.json"
makefile_path = base_dir / "Makefile"

# Collect all Python scripts
all_scripts = list(scripts_dir.rglob("*.py"))

# Parse resources.py for clues on script usage
resources = []
if resources_path.exists():
    with open(resources_path) as f:
        content = f.read()
        resources = re.findall(r'"(.*?)"', content)

# Parse .copilot/config.json
copilot_scripts = []
if copilot_config_path.exists():
    with open(copilot_config_path) as f:
        config = json.load(f)
        copilot_scripts = config.get("active_scripts", [])

# Parse Makefile for script mentions
makefile_scripts = []
if makefile_path.exists():
    with open(makefile_path) as f:
        makefile_content = f.read()
        makefile_scripts = re.findall(r"python\s+(scripts/[^\s]+\.py)", makefile_content)

# Classify scripts
used_scripts = set(copilot_scripts + makefile_scripts)
unused_scripts = []

for script in all_scripts:
    script_rel_path = str(script.relative_to(base_dir))
    if script_rel_path not in used_scripts:
        with open(script) as f:
            first_line = f.readline()
            if "copilot-enabled: true" not in first_line:
                unused_scripts.append(script_rel_path)

import pandas as pd
import ace_tools as tools; tools.display_dataframe_to_user(name="Unused Python Scripts", dataframe=pd.DataFrame(unused_scripts, columns=["Unused Scripts"]))
