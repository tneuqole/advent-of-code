.PHONY: format
format:
	uv run isort .
	uv run ruff format
	uv run ruff check --fix

.PHONY: test
test:
	echo "1\n5\n1\n2\n" | uv run pytest 2019/ -s
