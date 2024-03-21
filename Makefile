SHELL:=bash

CHECK_DIRS=./src
TOML_FILES=poetry.lock pyproject.toml
POETRY_EXEC=poetry

## help: print this help message
.PHONY: help
help:
	@echo 'Usage:'
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'

## format: run isort, black
.PHONY: format
format:
	$(POETRY_EXEC) run isort $(CHECK_DIRS)
	$(POETRY_EXEC) run black $(CHECK_DIRS) --line-length 99
	$(POETRY_EXEC) run toml-sort $(TOML_FILES) -i -a

## lint: flake8, pylint
.PHONY: lint
lint:
	$(POETRY_EXEC) run mypy $(CHECK_DIRS)
	$(POETRY_EXEC) run flake8 $(CHECK_DIRS)
	$(POETRY_EXEC) run pylint $(CHECK_DIRS)

## test: run unit tests
.PHONY: test
test:
	pytest ./tests -vv

## test-cov: run tests with coverage
.PHONY: test-cov
test-cov:
	$(POETRY_EXEC) run pytest ./tests -vv --cov

## format-check: run isort, black, toml-sort in check mode
.PHONY: format-check
format-check:
	$(POETRY_EXEC) run black $(CHECK_DIRS) --check --target-version py310
	$(POETRY_EXEC) run isort $(CHECK_DIRS) --check-only
	$(POETRY_EXEC) run toml-sort $(TOML_FILES) --check

## dev: run format, lint
.PHONY: dev
dev: format lint test-cov
