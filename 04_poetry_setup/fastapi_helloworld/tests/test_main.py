from fastapi.testclient import TestClient
from fastapi_helloworld.main import app


def test_index():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# def test_about():
#     client = TestClient(app=app)
#     response = client.get("/about")
#     assert response.status_code == 200
#     assert response.json() == {"message": "This is an about page"}