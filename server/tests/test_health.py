import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    """Test that the health endpoint returns the expected response"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_root_endpoint():
    """Test that the root endpoint returns a welcome message"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "Depi Bardzunk" in response.json()["message"]
