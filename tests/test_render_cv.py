from fastapi.testclient import TestClient
from app.main import app


def test_render_cv():
    client = TestClient(app)
    payload = {
        "name": "John Doe",
        "title": "Software Engineer",
        "work_experience": [
            {"position": "Developer", "company": "Acme", "years": "2018-2021"}
        ],
        "skills": ["Python", "FastAPI"],
        "education": [
            {"degree": "BSc Computer Science", "school": "Uni", "year": "2017"}
        ],
    }
    response = client.post("/render-cv", json=payload)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
