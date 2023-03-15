.PHONY: install ruff mypy black isort test self-test

all: ruff mypy black isort test self-test

install:
	pip install .
	pip install -r dev-requirements.txt

ruff:
	ruff refurb_json_minify test

mypy:
	mypy -p refurb_json_minify
	mypy -p test --exclude "test/data/*"

black:
	black refurb_json_minify test

isort:
	isort . --diff --check

test:
	pytest

self-test:
	refurb refurb_json_minify
