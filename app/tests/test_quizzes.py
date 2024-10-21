from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_fetch_quiz():
    response = client.get(
        "/api/v1/quizzes/quiz", params={"subject": "Mathematics", "topic": "Calculus"}
    )
    assert response.status_code == 200
    assert "questions" in response.json()


def test_fetch_quiz_not_found():
    response = client.get(
        "/api/v1/quizzes/quiz", params={"subject": "Biology", "topic": "Genetics"}
    )
    assert response.status_code == 404
