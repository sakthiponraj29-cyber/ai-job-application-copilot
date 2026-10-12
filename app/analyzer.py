
import re


SKILL_CATALOG = {
    # Programming and software development
    "python", "java", "javascript", "typescript", "c++", "c#",
    "html", "css", "react", "node.js", "fastapi", "sql",
    "rest api", "git", "docker", "aws", "azure",

    # AI and data
    "machine learning", "generative ai", "llm", "rag",
    "langchain", "langgraph", "deep learning", "data analysis",
    "data visualization", "excel", "power bi", "tableau",

    # Sales and business
    "sales", "lead generation", "customer relationship management",
    "crm", "negotiation", "salesforce", "business development",
    "market research", "marketing", "digital marketing",

    # Customer service and operations
    "customer service", "customer support", "communication",
    "email support", "voice process", "non-voice process",
    "data entry", "typing", "email writing", "problem solving",
    "time management", "multitasking", "attention to detail",
    "microsoft office", "word", "powerpoint",

    # Design
    "ui design", "ux design", "ui/ux design", "figma",
    "wireframing", "prototyping", "user research",
    "adobe photoshop", "adobe illustrator",

    # General professional skills
    "teamwork", "leadership", "project management",
    "documentation", "presentation", "analytical thinking",
}


# Alternative phrases that can represent the same skill.
SKILL_ALIASES = {
    "email support": ["email handling"],
    "typing": ["typing skills"],
    "data entry": ["data-entry"],
    "communication": ["communication skills"],
    "microsoft office": ["ms office"],
    "attention to detail": ["detail-oriented"],
    "rag": ["retrieval augmented generation"],
    "generative ai": ["genai"],
    "machine learning": ["ml"],
}


# Related terms: use these for matching, without inventing
# additional skills in the resume_skills output.
RELATED_SKILLS = {
    "customer service": {"customer support"},
    "customer support": {"customer service"},
}


def normalize_text(text: str) -> str:
    """Normalize case, whitespace, and common punctuation."""
    text = text.lower().replace("-", " ")
    return re.sub(r"\s+", " ", text).strip()


def contains_phrase(text: str, phrase: str) -> bool:
    """Match a complete phrase instead of a partial word."""
    normalized_text = normalize_text(text)
    normalized_phrase = normalize_text(phrase)

    pattern = (
        r"(?<!\w)"
        + re.escape(normalized_phrase)
        + r"(?!\w)"
    )
    return re.search(pattern, normalized_text) is not None


def extract_skills(text: str) -> set[str]:
    """Find catalogued skills and their known aliases."""
    found_skills = set()

    for skill in SKILL_CATALOG:
        phrases = [skill] + SKILL_ALIASES.get(skill, [])

        if any(contains_phrase(text, phrase) for phrase in phrases):
            found_skills.add(skill)

    return found_skills


def remove_known_job_titles(text: str) -> str:
    """
    Remove known role-title phrases before extracting job requirements.
    This prevents a job title from being counted as a required skill.
    """
    title_patterns = [
        r"\bnon[\s-]+voice\s+process\s+executive\b",
        r"\bvoice\s+process\s+executive\b",
    ]

    for pattern in title_patterns:
        text = re.sub(pattern, " ", text, flags=re.IGNORECASE)

    return text


def skills_are_equivalent(
    required_skill: str,
    resume_skills: set[str],
) -> bool:
    """Check exact skills and explicitly defined related terms."""
    if required_skill in resume_skills:
        return True

    related = RELATED_SKILLS.get(required_skill, set())
    return bool(related & resume_skills)


def analyze_resume(resume: str, job_description: str) -> dict:
    """Compare resume skills against skills detected in a job description."""
    resume_skills = extract_skills(resume)

    cleaned_job_description = remove_known_job_titles(job_description)
    required_skills = extract_skills(cleaned_job_description)

    matching_skills = sorted(
        skill
        for skill in required_skills
        if skills_are_equivalent(skill, resume_skills)
    )

    potential_gaps = sorted(
        required_skills - set(matching_skills)
    )

    return {
        "resume_skills": sorted(resume_skills),
        "required_skills_found": sorted(required_skills),
        "matching_skills": matching_skills,
        "potential_gaps": potential_gaps,
        "match_count": len(matching_skills),
        "gap_count": len(potential_gaps),
        "note": (
            "Potential gaps are skills not detected in the supplied "
            "resume text. They do not prove the candidate lacks them."
        ),
    }
