#!/usr/bin/env python
# copilot-enabled: true
# purpose: Used by GitHub Copilot for code refactoring, generation, or maintenance
3
import os
import subprocess
from pathlib import Path

# Define the base directory of your repository
BASE_DIR = Path(__file__).resolve().parent.parent

# Define the paths to the files containing lists of orphaned scripts
UNLINKED_FILES_PATH = BASE_DIR / "orphan_results" / "unlinked_files.txt"
NOT_IN_MAKEFILE_PATH = BASE_DIR / "orphan_results" / "not_in_makefile.txt"

# Read the lists of orphaned scripts
def read_orphaned_files(file_path):
    if file_path.exists():
        with open(file_path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    return []

unlinked_files = read_orphaned_files(UNLINKED_FILES_PATH)
not_in_makefile_files = read_orphaned_files(NOT_IN_MAKEFILE_PATH)

# Combine and deduplicate the lists
orphaned_files = set(unlinked_files + not_in_makefile_files)

# Create GitHub issues for each orphaned script
for file_path in orphaned_files:
    issue_title = f"[Copilot] Cleanup Task: {file_path}"
    issue_body = f"""
## 📌 Objective
Standardize and clean up `{file_path}` in the Clio SDK repository.

## 🧠 Context
This file appears to be:
- Not importing `resources.py`
- Not listed in the `Makefile`

## 🎯 Tasks
- [ ] Determine if `{file_path}` is still needed
- [ ] Refactor or consolidate it into the main architecture
- [ ] Archive if obsolete, or add to Makefile if valid
- [ ] Annotate with `# copilot: consider` if unsure

## ⚠️ Constraints
- Follow Clio SDK naming standards
- Pass all `ruff`, `mypy`, `black` checks
"""

    # Use GitHub CLI to create the issue
    subprocess.run([
        "gh", "issue", "create",
        "--title", issue_title,
        "--body", issue_body,
        "--label", "copilot,refactor,cleanup"
    ])
