
from app.message_generator import (
    extract_job_title,
    generate_application_message,
)


def test_extract_job_title():
    job_description = (
        "We are hiring a Non-Voice Process Executive "
        "with typing and email support."
    )

    assert (
        extract_job_title(job_description)
        == "Non-Voice Process Executive"
    )


def test_message_uses_only_provided_matching_skills():
    message = generate_application_message(
        resume="Typing and email support experience.",
        job_description=(
            "We are hiring a Non-Voice Process Executive."
        ),
        matching_skills=["typing", "email support"],
    )

    assert "Non-Voice Process Executive" in message
    assert "typing" in message
    assert "email support" in message
    assert "attention to detail" not in message


def test_message_without_matching_skills():
    message = generate_application_message(
        resume="Motivated candidate.",
        job_description="We are hiring a Python Developer.",
        matching_skills=[],
    )

    assert "Python Developer" in message
    assert "willingness to learn" in message
