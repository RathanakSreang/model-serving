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

def test_cat_or_dog_1(client) -> None:
    file = "./images/cat.jpg"
    data = {"image": (open(file, "rb"), file)}
    response = client.post("/cat-or-dog", data=data)
    assert response.json["result"] == "cat"

def test_cat_or_dog_2(client) -> None:
    file = "./images/dog.jpeg"
    data = {"image": (open(file, "rb"), file)}
    response = client.post("/cat-or-dog", data=data)
    assert response.json["result"] == "dog"