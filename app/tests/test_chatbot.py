from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_query_chatbot():
    response = client.post(
        "/api/v1/chatbot/query",
        json={"user_id": "test_user", "query": "What is Newton's Second Law?"},
    )
    assert response.status_code == 200
    assert "F=ma" in response.json()["response"]


def test_query_chatbot_missing_fields():
    response = client.post("/api/v1/chatbot/query", json={"user_id": "test_user"})
    assert response.status_code == 422  # Unprocessable Entity
