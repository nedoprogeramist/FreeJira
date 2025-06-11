import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_name_existing_item():
    response = client.get("/items/1")
    assert response.json() == {"id": 1, "key": "DPO-777", "status": "todo", "owner": "user1"}
    assert response.status_code == 200

def test_read_name_non_existing_item():
    response = client.get("/items/key/DPO-778")
    assert response.json() == {"id": 2, "key": "DPO-778", "status": "todo", "owner": "user2"}
    assert response.status_code == 200

