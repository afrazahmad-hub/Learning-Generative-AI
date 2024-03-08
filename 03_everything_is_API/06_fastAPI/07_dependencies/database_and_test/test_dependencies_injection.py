from fastapi.testclient import TestClient # fastapi test client

# internal files imported dependency function
from database import app, get_db_session

testing_db = ["DB for testing"]

def get_testing_db():
    return testing_db

# overriding the dependencies imported from database.py
app.dependency_overrides[get_db_session] = get_testing_db

# creatinmg client for app imported from database.py
client = TestClient(app)

def test_read_main():
    response = client.get("/add-items/?item=sugar")

    assert response.status_code == 200
    assert response.json() == {"item": "sugar"}
    

# to run test use command: pytest -v test_dependencies_injection.py