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
- `POST /users` - Create a new user (requires `{"name": "string"}`)
- `GET /users` - List all users (supports pagination with `?skip=0&limit=100`)

### Database Models

- **User**: `id` (PK), `name`, `created_at`

### Testing

The application includes comprehensive tests:
- Health endpoint tests
- User CRUD operations tests
- API response validation

Run tests with: `make test`

## Project Structure

```
server/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── models.py        # SQLAlchemy models
│   ├── deps.py          # Dependencies
│   └── routes_users.py  # User endpoints
├── alembic/             # Database migrations
├── tests/               # Test suite
├── database.py          # Database configuration
├── pyproject.toml       # Poetry configuration
├── alembic.ini         # Alembic configuration
├── Makefile            # Development commands
└── env.example         # Environment variables template
```

## Database

The application uses PostgreSQL with SQLAlchemy ORM and Alembic for migrations. The database URL is configured via the `DATABASE_URL` environment variable.

### Database Setup

1. Create a PostgreSQL database named `depi`
2. Copy `env.example` to `.env` and update the `DATABASE_URL`
3. Run `make migrate` to apply migrations
4. Use `make makemigration` to create new migrations when models change
