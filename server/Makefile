.PHONY: dev migrate makemigration test

dev:
	poetry run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

migrate:
	poetry run alembic upgrade head

makemigration:
	poetry run alembic revision --autogenerate -m "init"

test:
	poetry run pytest
