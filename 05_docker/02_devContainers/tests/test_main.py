from fastapi.testclient import TestClient
from docker_helloworld.main import app


def test_index():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message" : "Hello World"}