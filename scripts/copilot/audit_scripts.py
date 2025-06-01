#!/usr/bin/env python3
import hashlib
import os
import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT / "scripts"
MAKEFILE = ROOT / "Makefile"
RESOURCES = ROOT / "resources.py"

def file_hash(path: Path) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def extract_references(*paths):
    references = set()
    for path in paths:
        if path.exists():
            with open(path) as f:
                for line in f:
                    for token in line.split():
                        if token.endswith(".py"):
                            references.add(token.strip())
    return references

def find_orphans():
    referenced = extract_references(MAKEFILE, RESOURCES)
    orphans = []
    for file in SCRIPTS_DIR.glob("*.py"):
        if file.name not in referenced and not file.name.startswith("copilot_"):
            orphans.append(file)
    return orphans

--- a/scripts/audit_scripts.py
+++ b/scripts/audit_scripts.py
@@ def find_duplicates() -> List[Tuple[Path, Path]]:
     return duplicates
 
+def create_github_issue(title: str, body: str):
+    """Create a GitHub issue using the GitHub CLI."""
+    try:
+        subprocess.run([
+            "gh", "issue", "create",
+            "--title", title,
+            "--body", body
+        ], check=True)
+    except subprocess.CalledProcessError as e:
+        print(f"⚠️ Failed to create GitHub issue: {e}")
+
 def main():
     orphans = find_orphans()
     duplicates = find_duplicates()

     print("\n🧹 Unused Scripts:")
     for orphan in orphans:
         rel_path = orphan.relative_to(ROOT)
         print(f" - {rel_path}")
+        create_github_issue(
+            title=f"Cleanup: Unused script `{rel_path}`",
+            body=f"The script `{rel_path}` appears to be unused. Consider archiving or removing it."
+        )

     print("\n🧪 Duplicate Scripts:")
     for a, b in duplicates:
         rel_a = a.relative_to(ROOT)
         rel_b = b.relative_to(ROOT)
         print(f" - {rel_a} ⭢ {rel_b}")
+        create_github_issue(
+            title=f"Refactor: Duplicate script detected `{rel_b}`",
+            body=f"The script `{rel_b}` is structurally identical to `{rel_a}`. Consider consolidating them."
+        )


if __name__ == "__main__":
    main()
