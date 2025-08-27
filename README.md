# Depi Bardzunk

A FastAPI backend application with PostgreSQL database support.

## Quick Start

### Prerequisites

- Python 3.8+
- Poetry (Python package manager)
- PostgreSQL database

### Setup

1. **Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Navigate to the server directory**:
   ```bash
   cd server
   ```

3. **Install dependencies**:
   ```bash
   poetry install
   ```

4. **Set up environment variables**:
   ```bash
   cp env.example .env
   # Edit .env with your actual database credentials
   ```

5. **Set up the database**:
   ```bash
   # Create PostgreSQL database
   createdb depi
   
   # Run migrations
   make migrate
   ```

### Development

- **Start development server**: `make dev`
- **Run tests**: `make test`
- **Create new migration**: `make makemigration`
- **Apply migrations**: `make migrate`

### API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check (returns `{"ok": true}`)

### Testing

The application includes comprehensive tests:
- Health endpoint tests
- API response validation

Run tests with: `make test`

## Project Structure

```
server/
├── app/
│   ├── __init__.py
│   └── main.py          # FastAPI application
├── alembic/             # Database migrations
├── tests/               # Test suite
├── pyproject.toml       # Poetry configuration
├── alembic.ini         # Alembic configuration
├── Makefile            # Development commands
└── env.example         # Environment variables template
```

## Database

The application uses PostgreSQL with SQLAlchemy ORM and Alembic for migrations. The database URL is configured via the `DATABASE_URL` environment variable.
