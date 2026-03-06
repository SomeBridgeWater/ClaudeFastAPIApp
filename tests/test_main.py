import pytest
from fastapi.testclient import TestClient

from my_package.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_item():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42}


def test_read_item_zero():
    response = client.get("/items/0")
    assert response.status_code == 200
    assert response.json() == {"item_id": 0}


def test_read_item_invalid():
    response = client.get("/items/abc")
    assert response.status_code == 422
