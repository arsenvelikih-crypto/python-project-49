# Makefile

install:
	uv sync

brain-games:
	uv run brain-

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

build:
	uv build