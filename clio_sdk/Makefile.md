### Makefile

.PHONY: format lint test build clean update-client

format:
black .
isort .

lint:
ruff .
mypy clio_sdk

check: lint format test

test:
pytest tests

update-client:
bash scripts/update_openapi.sh
