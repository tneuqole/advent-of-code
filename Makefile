.PHONY: fmt
fmt:
	-uv run ruff check --fix
	uv run isort .
	uv run ruff format

.PHONY: test
test:
	uv run pytest 2019/

.PHONY: new
new:
	cp templates/template.py $(y)/day$(d).py

