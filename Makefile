.PHONY: clean
clean-w:
	powershell -NoProfile -Command "Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse"

.PHONY: format
format:
	uv run ruff format
	uv run ruff check --select I --fix

.PHONY: test e2e
test:
	uv run pytest tests/unit/
e2e:
	uv run pytest tests/e2e/