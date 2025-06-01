#!/usr/bin/env python3
import subprocess
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
OPENAPI_SPEC = BASE_DIR / "openapi_sdk.yaml"
CLIENT_CONFIG = BASE_DIR / "openapi-python-client-config.yaml"
SDK_CONFIG = BASE_DIR / "openapi-python-sdk-config.yaml"
TEMPLATE_DIR = BASE_DIR / "templates"

CLIENT_OUTPUT = BASE_DIR / "clio_client"
SDK_OUTPUT = BASE_DIR / "clio_sdk"


def validate_paths():
    global TEMPLATE_DIR  # Move global declaration to the top of the function
    missing = []
    if not OPENAPI_SPEC.exists():
        missing.append(f"Missing OpenAPI spec: {OPENAPI_SPEC}")
    # Patch: Accept either scripts/templates or templates as the template dir
    if not TEMPLATE_DIR.exists():
        alt_template_dir = BASE_DIR / "scripts" / "templates"
        if alt_template_dir.exists():
            TEMPLATE_DIR = alt_template_dir
        else:
            missing.append(f"Missing Jinja template directory: {TEMPLATE_DIR} (also checked {alt_template_dir})")
    if not CLIENT_CONFIG.exists():
        missing.append(f"Missing client config: {CLIENT_CONFIG}")
    if not SDK_CONFIG.exists():
        missing.append(f"Missing SDK config: {SDK_CONFIG}")

    if missing:
        for err in missing:
            print(f"❌ {err}")
        sys.exit(1)


def run_codegen(output_dir: Path, config_path: Path):
    print(f"🚀 Generating {output_dir.name}...")
    try:
        subprocess.run([
            "openapi-python-client", "generate",
            "--path", str(OPENAPI_SPEC),
            "--config", str(config_path),
            "--custom-template-path", str(TEMPLATE_DIR),
            "--output-path", str(output_dir),  # PATCH: use --output-path
            "--meta", "none"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"🚨 Code generation failed for {output_dir.name}: {e}")
        sys.exit(1)


def main():
    print("🧪 Validating environment...")
    validate_paths()

    # Ask user if they want to overwrite client output if it exists
    if CLIENT_OUTPUT.exists():
        response = input(f"{CLIENT_OUTPUT} already exists. Overwrite? [y/N]: ").strip().lower()
        if response == "y":
            import shutil
            shutil.rmtree(CLIENT_OUTPUT)
            run_codegen(CLIENT_OUTPUT, CLIENT_CONFIG)
        else:
            print(f"Skipping client generation: {CLIENT_OUTPUT} already exists.")
    else:
        run_codegen(CLIENT_OUTPUT, CLIENT_CONFIG)

    # Ask user if they want to overwrite SDK output if it exists
    if SDK_OUTPUT.exists():
        response = input(f"{SDK_OUTPUT} already exists. Overwrite? [y/N]: ").strip().lower()
        if response == "y":
            import shutil
            shutil.rmtree(SDK_OUTPUT)
            run_codegen(SDK_OUTPUT, SDK_CONFIG)
        else:
            print(f"Skipping SDK generation: {SDK_OUTPUT} already exists.")
    else:
        run_codegen(SDK_OUTPUT, SDK_CONFIG)

    print("✅ Code generation complete and validated.")


if __name__ == "__main__":
    main()
