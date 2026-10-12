
import re


def extract_job_title(job_description: str) -> str:
    """Extract a likely job title from common job-description phrases."""

    patterns = [
        r"\b(?:hiring|looking for)\s+(?:for\s+)?(?:an?\s+)?"
        r"([A-Za-z][A-Za-z0-9/& -]{2,55}?)"
        r"(?=\s+(?:with|required|requiring|who|to join)\b|[.,\n]|$)",

        r"\b(?:position|role)\s+(?:of|for)\s+(?:an?\s+)?"
        r"([A-Za-z][A-Za-z0-9/& -]{2,55}?)"
        r"(?=\s+(?:with|required|requiring|who|to join)\b|[.,\n]|$)",
    ]

    for pattern in patterns:
        match = re.search(pattern, job_description, re.IGNORECASE)

        if match:
            title = match.group(1).strip(" .,:-")

            # Remove trailing conjunctions or other unwanted words.
            title = re.sub(
                r"\s+(?:and|for|with|the)$",
                "",
                title,
                flags=re.IGNORECASE,
            ).strip()

            if title:
                return title

    return "the advertised position"


def generate_application_message(
    resume: str,
    job_description: str,
    matching_skills: list[str],
) -> str:
    """Generate a professional message using resume-backed skills."""

    role = extract_job_title(job_description)

    # Remove duplicate skill names while preserving their order.
    skills = list(dict.fromkeys(
        skill.strip()
        for skill in matching_skills
        if skill.strip()
    ))

    if len(skills) == 1:
        skills_text = skills[0]
    elif len(skills) == 2:
        skills_text = f"{skills[0]} and {skills[1]}"
    elif skills:
        skills_text = (
            ", ".join(skills[:-1]) + f", and {skills[-1]}"
        )
    else:
        skills_text = None

    if skills_text:
        experience_sentence = (
            f"My background includes {skills_text}, "
            "which align with the requirements of this role."
        )
    else:
        experience_sentence = (
            "My background and willingness to learn would help me "
            "contribute to this role."
        )

    return (
        f"Dear Hiring Team,\n\n"
        f"I am writing to express my interest in the "
        f"{role} position. "
        f"{experience_sentence} "
        f"I would welcome the opportunity to contribute to your team "
        f"and discuss my suitability for the role.\n\n"
        f"Thank you for your time and consideration.\n\n"
        f"Best regards,\n"
        f"Sakthi Ponraj"
    )
