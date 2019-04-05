PYTEST_ARGS = -vv
PYTEST_PATH = tests

.PHONY: format
format:
	black .

poetry.lock: pyproject.toml
	poetry lock

requirements.txt: poetry.lock
	poetry install $(POETRY_EXTRA)
	poetry show | awk '{print $$1"=="$$2}' > $@

.PHONY: tests
tests:
	py.test $(PYTEST_ARGS) $(PYTEST_PATH)
