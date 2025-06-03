.PHONY: test lint build clean

install:
	pip install -e .[dev]

test:
	pytest

lint:
	ruff .

build:
	python -m build

clean:
	rm -rf dist/ build/ *.egg-info