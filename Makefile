.PHONY format
format:
	uv run isort .
	uv run ruff format
	uv run ruff check --fix
