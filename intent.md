# Intent: AI Job Application Copilot

## 1. Problem Statement

Job seekers often spend significant time comparing their resumes with job descriptions, identifying missing skills, and preparing tailored job applications. Doing this manually for every job can be repetitive and time-consuming.

## 2. Target Users

Job seekers applying for technical roles, especially AI/ML and software engineering positions.

## 3. Proposed Solution

Build an AI-powered web application that accepts a resume and a job description, compares the candidate's skills with the role requirements, identifies potential skill gaps, and generates a tailored application message based only on the candidate's actual experience.

## 4. Core Features

1. Accept resume text and a job description.
2. Identify matching skills and missing or unverified requirements.
3. Generate a concise, personalized application message.
4. Explain the match results with evidence from the supplied information.
5. Handle incomplete inputs and AI errors safely.

## 5. Success Criteria

- The application processes a resume and job description successfully.
- The results clearly distinguish matching skills from missing or unverified skills.
- Generated messages do not invent qualifications or work experience.
- Invalid inputs and AI service failures produce useful error messages.
- The complete workflow can be demonstrated with test examples.

## 6. Initial Assumptions

I initially assume that an LLM can reliably compare resumes with job descriptions. I will test this assumption using different examples and refine the approach based on observed failures.

## 7. Five-Day Scope

The goal is to deliver a working minimum viable product, test its behavior, document failures and improvements, and provide a GitHub repository with setup instructions and a demonstration.

## 8. Out of Scope

Automated job applications, paid job-board integrations, and complex user authentication are excluded from the initial version.