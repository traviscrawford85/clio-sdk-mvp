#!/usr/bin/env python3
import subprocess
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
OPENAPI_SPEC = BASE_DIR / "openapi_sdk.yaml"
CLIENT_CONFIG = BASE_DIR / "openapi-python-client-config.yaml"
SDK_CONFIG = BASE_DIR / "openapi-python-sdk-config.yaml"
TEMPLATE_DIR = BASE_DIR / "scripts/templates"

CLIENT_OUTPUT = BASE_DIR / "clio_client"
SDK_OUTPUT = BASE_DIR / "clio_sdk"


def validate_paths():
    missing = []
    if not OPENAPI_SPEC.exists():
        missing.append(f"Missing OpenAPI spec: {OPENAPI_SPEC}")
    if not TEMPLATE_DIR.exists():
        missing.append(f"Missing Jinja template directory: {TEMPLATE_DIR}")
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
            "--output", str(output_dir),
            "--meta", "none"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"🚨 Code generation failed for {output_dir.name}: {e}")
        sys.exit(1)


def main():
    print("🧪 Validating environment...")
    validate_paths()

    run_codegen(CLIENT_OUTPUT, CLIENT_CONFIG)
    run_codegen(SDK_OUTPUT, SDK_CONFIG)

    print("✅ Code generation complete and validated.")


if __name__ == "__main__":
    main()
