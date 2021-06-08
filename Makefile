.PHONY: install test lint

default: test

install:
	poetry install && poetry update

lint:
	poetry run pre-commit install && poetry run pre-commit run -a -v

test:
	PYTHONPATH=. pytest