#!/usr/bin/env python3
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OPENAPI_SPEC = BASE_DIR / "openapi_sdk.yaml"
CLIENT_CONFIG = BASE_DIR / "openapi-python-client-config.yaml"
SDK_CONFIG = BASE_DIR / "openapi-python-sdk-config.yaml"
TEMPLATE_DIR = BASE_DIR / "scripts/templates"

CLIENT_OUTPUT = BASE_DIR / "clio_client"
SDK_OUTPUT = BASE_DIR / "clio_sdk"

def run_codegen(output_dir: Path, config_path: Path):
    subprocess.run([
        "openapi-python-client", "generate",
        "--path", str(OPENAPI_SPEC),
        "--config", str(config_path),
        "--custom-template-path", str(TEMPLATE_DIR),
        "--output", str(output_dir),
        "--meta", "none"
    ], check=True)

def main():
    print("🔧 Generating clio_client...")
    run_codegen(CLIENT_OUTPUT, CLIENT_CONFIG)

    print("🔧 Generating clio_sdk...")
    run_codegen(SDK_OUTPUT, SDK_CONFIG)

    print("✅ Code generation complete.")

if __name__ == "__main__":
    main()
