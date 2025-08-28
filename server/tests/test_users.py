import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.models import Base
from database import get_db

# Create in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)


def override_get_db():
    """Override get_db for testing"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_user():
    """Test creating a new user"""
    user_data = {"name": "John Doe"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert "id" in data
    assert "created_at" in data


def test_list_users():
    """Test listing users"""
    # Create a user first
    user_data = {"name": "Jane Doe"}
    client.post("/users/", json=user_data)
    
    # List users
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert any(user["name"] == "Jane Doe" for user in data)


def test_list_users_pagination():
    """Test users pagination"""
    # Create multiple users
    for i in range(5):
        client.post("/users/", json={"name": f"User {i}"})
    
    # Test pagination
    response = client.get("/users/?skip=0&limit=3")
    assert response.status_code == 200
    data = response.json()
    assert len(data) <= 3
