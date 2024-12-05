.PHONY: format
format:
	uv run isort .
	uv run ruff format
	uv run ruff check --fix

.PHONY: test
test:
	uv run pytest 2019/
