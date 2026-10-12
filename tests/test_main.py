
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_analyze_skills():
    response = client.post(
        "/analyze",
        json={
            "resume": "Python and FastAPI developer",
            "job_description": "Python, FastAPI, and AWS required",
        },
    )

    assert response.status_code == 200

    result = response.json()
    assert "python" in result["matching_skills"]
    assert "fastapi" in result["matching_skills"]
    assert "aws" in result["potential_gaps"]


def test_empty_resume_rejected():
    response = client.post(
        "/analyze",
        json={
            "resume": "",
            "job_description": "Python developer",
        },
    )

    assert response.status_code == 422


def test_missing_resume_rejected():
    response = client.post(
        "/analyze",
        json={"job_description": "Python developer"},
    )

    assert response.status_code == 422


def test_empty_job_description_rejected():
    response = client.post(
        "/analyze",
        json={
            "resume": "Python developer",
            "job_description": "",
        },
    )

    assert response.status_code == 422


def test_generate_message():
    response = client.post(
        "/generate-message",
        json={
            "resume": "Python developer with Python experience.",
            "job_description": (
                "We are hiring a Python Developer "
                "with Python and FastAPI."
            ),
        },
    )

    assert response.status_code == 200

    result = response.json()
    assert "application_message" in result
    assert "Python Developer" in result["application_message"]
    assert "python" in result["matching_skills"]
    assert "Review before sending" in result["note"]

