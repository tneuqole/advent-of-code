.PHONY: format
format:
	-uv run ruff check --fix
	uv run isort .
	uv run ruff format

.PHONY: test
test:
	uv run pytest 2019/
