
from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.analyzer import analyze_resume
from app.message_generator import generate_application_message

app = FastAPI(
    title="AI Job Application Copilot",
    description="Analyze resume skills against job requirements.",
    version="0.2.0",
)


class AnalyzeRequest(BaseModel):
    resume: str = Field(min_length=1, max_length=20000)
    job_description: str = Field(min_length=1, max_length=20000)


@app.get("/")
def home():
    return {
        "message": "AI Job Application Copilot is running!",
        "status": "success",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    return analyze_resume(
        resume=request.resume,
        job_description=request.job_description,
    )


@app.post("/generate-message")
def generate_message(request: AnalyzeRequest):
    analysis = analyze_resume(
        resume=request.resume,
        job_description=request.job_description,
    )

    message = generate_application_message(
        resume=request.resume,
        job_description=request.job_description,
        matching_skills=analysis["matching_skills"],
    )

    return {
        "application_message": message,
        "matching_skills": analysis["matching_skills"],
        "note": "Template-based draft. Review before sending.",
    }
