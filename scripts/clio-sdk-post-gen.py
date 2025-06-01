#!/usr/bin/env python3
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SDK_PATHS = [BASE_DIR / "clio_client", BASE_DIR / "clio_sdk"]

def run_hook(command: list, cwd: Path):
    print(f"🔧 Running {' '.join(command)} in {cwd}...")
    try:
        subprocess.run(command, cwd=cwd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Hook failed: {' '.join(command)} - {e}")
        exit(1)

def main():
    for path in SDK_PATHS:
        print(f"🎯 Post-gen tasks for {path.name}")
        run_hook(["ruff", "check", ".", "--fix"], cwd=path)
        run_hook(["ruff", "format", "."], cwd=path)
        run_hook(["autoflake", "--in-place", "--remove-all-unused-imports", "--recursive", "."], cwd=path)
        run_hook(["isort", "."], cwd=path)

        test_path = path / "tests"
        if test_path.exists():
            run_hook(["pytest"], cwd=path)

        run_hook(["git", "add", "."], cwd=path)
        run_hook(["git", "status"], cwd=path)

    print("✅ Post-generation cleanup complete.")

if __name__ == "__main__":
    main()
