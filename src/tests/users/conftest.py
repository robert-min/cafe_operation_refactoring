import pytest
from fastapi.testclient import TestClient
from apps import create_app

@pytest.fixture
def fastapi_app():
    app = create_app()
    yield app

@pytest.fixture
def client(fastapi_app):
    client = TestClient(fastapi_app)
    client.headers.update({"Content-Type": "application/json"})
    yield client
