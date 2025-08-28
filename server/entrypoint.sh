#!/usr/bin/env bash
set -e

# Wait for DB (compose will wait via depends_on health, but this is harmless)
echo "Running Alembic migrations..."
alembic upgrade head

echo "Starting Uvicorn..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
