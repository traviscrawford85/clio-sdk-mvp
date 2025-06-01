import os
from pathlib import Path

# VS Code Settings
vscode_settings = {
    "python.formatting.provider": "black",
    "editor.formatOnSave": True,
    "editor.codeActionsOnSave": {
        "source.organizeImports": True,
    },
    "python.linting.enabled": True,
    "python.linting.mypyEnabled": True,
    "python.linting.flake8Enabled": True,
    "python.linting.pylintEnabled": False,
    "python.analysis.aiCodeActions": {
    "implementAbstractClasses": True
    },
    "python.linting.mypyArgs": ["--strict"],
    "editor.defaultFormatter": "ms-python.black-formatter",
}

# .editorconfig content
editorconfig = """
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
indent_style = space
indent_size = 4
trim_trailing_whitespace = true
max_line_length = 88
"""

# GitHub Actions Workflow
workflow_content = """
name: Quality Check

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install black isort mypy flake8

      - name: Check formatting with black
        run: black --check .

      - name: Check imports with isort
        run: isort . --check-only

      - name: Type check with mypy
        run: mypy .

      - name: Lint with flake8
        run: flake8 .
"""

# Write files
Path(".vscode").mkdir(exist_ok=True)
Path(".github/workflows").mkdir(parents=True, exist_ok=True)

with open(".vscode/settings.json", "w") as f:
    import json

    json.dump(vscode_settings, f, indent=4)

with open(".editorconfig", "w") as f:
    f.write(editorconfig.strip())

with open(".github/workflows/quality.yaml", "w") as f:
    f.write(workflow_content.strip())

"✅ VS Code settings, .editorconfig, and GitHub Actions workflow have been created."
