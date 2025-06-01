#!/usr/bin/env python3
import hashlib
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT / "scripts"
MAKEFILE = ROOT / "Makefile"

def file_hash(path: Path) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def extract_script_references_from_makefile(makefile_path: Path):
    """Extract all .py script references from the Makefile."""
    references = set()
    if makefile_path.exists():
        with open(makefile_path) as f:
            for line in f:
                line = line.strip()
                if ".py" in line:
                    for token in line.split():
                        if token.endswith(".py") or ".py:" in token:
                            # Remove trailing ':' if present
                            references.add(token.rstrip(":"))
    return references

def find_orphans():
    referenced = extract_script_references_from_makefile(MAKEFILE)
    orphans = []
    for file in SCRIPTS_DIR.rglob("*.py"):
        if file.name == "__init__.py":
            continue
        if file.name not in referenced and not file.name.startswith("copilot_"):
            orphans.append(file)
    return orphans

def find_duplicates():
    """Find duplicate scripts by content hash."""
    hashes = {}
    duplicates = []
    for file in SCRIPTS_DIR.rglob("*.py"):
        if file.name == "__init__.py":
            continue
        h = file_hash(file)
        if h in hashes:
            duplicates.append((hashes[h], file))
        else:
            hashes[h] = file
    return duplicates

def create_github_issue(title: str, body: str):
    """Create a GitHub issue using the GitHub CLI."""
    try:
        subprocess.run([
            "gh", "issue", "create",
            "--title", title,
            "--body", body
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Failed to create GitHub issue: {e}")

def main():
    orphans = find_orphans()
    duplicates = find_duplicates()

    print("\n🧹 Unused Scripts:")
    for orphan in orphans:
        rel_path = orphan.relative_to(ROOT)
        print(f" - {rel_path}")
        # Uncomment to enable GitHub issue creation
        # create_github_issue(
        #     title=f"Cleanup: Unused script `{rel_path}`",
        #     body=f"The script `{rel_path}` appears to be unused. Consider archiving or removing it."
        # )

    print("\n🧪 Duplicate Scripts:")
    for a, b in duplicates:
        rel_a = a.relative_to(ROOT)
        rel_b = b.relative_to(ROOT)
        print(f" - {rel_a} ⭢ {rel_b}")
        # Uncomment to enable GitHub issue creation
        # create_github_issue(
        #     title=f"Refactor: Duplicate script detected `{rel_b}`",
        #     body=f"The script `{rel_b}` is structurally identical to `{rel_a}`. Consider consolidating them."
        # )

if __name__ == "__main__":
    main()
