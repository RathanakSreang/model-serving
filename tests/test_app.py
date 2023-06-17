"""Test app.py."""
import pytest
from src.app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()

def test_welcome(client) -> None:
    response = client.get("/")
    assert response.json == "Welcome to Model serving service"
