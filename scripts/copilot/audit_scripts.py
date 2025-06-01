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

def find_duplicates():
    seen = {}
    duplicates = []
    for file in SCRIPTS_DIR.glob("*.py"):
        try:
            tree = ast.parse(file.read_text())
            structure = ast.dump(tree, annotate_fields=False)
            digest = hashlib.sha256(structure.encode()).hexdigest()
            if digest in seen:
                duplicates.append((seen[digest], file))
            else:
                seen[digest] = file
        except Exception as e:
            print(f"❌ Failed to parse {file}: {e}")
    return duplicates

def main():
    orphans = find_orphans()
    duplicates = find_duplicates()

    print("\n🧹 Unused Scripts:")
    for orphan in orphans:
        print(f" - {orphan.relative_to(ROOT)}")

    print("\n🧪 Duplicate Scripts:")
    for a, b in duplicates:
        print(f" - {a.relative_to(ROOT)} ⭢ {b.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
