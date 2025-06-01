
# copilot-enabled: true
# purpose: Used by GitHub Copilot for code refactoring, generation, or maintenance

import os
import requests
from pathlib import Path

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("GITHUB_REPO")  # Format: "owner/repo"
ISSUE_TITLE_TEMPLATE = "[Copilot] Cleanup Task: {}"
ISSUE_BODY_TEMPLATE = """
## 📌 Objective
Standardize and clean up `{filename}` in the Clio SDK repo.

## 🧠 Context
This file appears to be:
- Not importing `resources.py`
- Not listed in the `Makefile`

## 🎯 Tasks
- [ ] Determine if `{filename}` is still needed
- [ ] Refactor or consolidate it into the main architecture
- [ ] Archive if obsolete, or add to Makefile if valid
- [ ] Annotate with `# copilot: consider` if unsure

## ⚠️ Constraints
- Follow Clio SDK naming standards
- Pass all `ruff`, `mypy`, `black` checks
"""

def create_issue(filename: str):
    url = f"https://api.github.com/repos/{REPO}/issues"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    data = {
        "title": ISSUE_TITLE_TEMPLATE.format(filename),
        "body": ISSUE_BODY_TEMPLATE.format(filename=filename),
        "labels": ["copilot", "refactor", "cleanup"]
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"✅ Created issue for {filename}")
    else:
        print(f"❌ Failed to create issue for {filename}: {response.status_code} - {response.text}")

def main():
    orphan_files = Path("orphan_results/unlinked_files.txt").read_text().splitlines()
    orphan_files += Path("orphan_results/not_in_makefile.txt").read_text().splitlines()
    unique_files = set(f.strip() for f in orphan_files if f.strip())

    for file in unique_files:
        if file.endswith(".py"):
            create_issue(file)

if __name__ == "__main__":
    main()
