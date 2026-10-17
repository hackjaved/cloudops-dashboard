
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_homepage(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"CloudOps Dashboard" in response.data


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"
    assert data["application"] == "CloudOps Dashboard"
    assert data["version"] == "1.0.0"


def test_info_endpoint(client):
    response = client.get("/api/info")

    assert response.status_code == 200

    data = response.get_json()

    assert data["platform"] == "Python Flask"
    assert data["version"] == "1.0.0"


def test_unknown_endpoint(client):
    response = client.get("/does-not-exist")

    assert response.status_code == 404
