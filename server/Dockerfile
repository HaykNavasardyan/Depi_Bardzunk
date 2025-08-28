FROM python:3.12-slim

# System deps for psycopg2 + build
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

# Poetry (no virtualenv inside container)
ENV POETRY_HOME=/opt/poetry \
    POETRY_VERSION=1.8.3 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry && \
    poetry config virtualenvs.create false

WORKDIR /app

# Install deps first (better caching)
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --only main --no-interaction --no-ansi

# Now copy the app source
COPY . /app

# Make entrypoint executable
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000
CMD ["/app/entrypoint.sh"]
