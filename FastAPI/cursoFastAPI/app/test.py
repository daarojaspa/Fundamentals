from fastapi.testclient import TestClient
import test_user
def test_client(client):
    assert type(client).__name__ == TestClient.__name__
    