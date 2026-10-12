\# AI Job Application Copilot



An AI-powered application that analyzes resumes against job descriptions, identifies matching skills and potential skill gaps, and generates professional job application messages.



\## Features



\- \*\*Resume Skill Analysis:\*\* Extracts skills from resume text.

\- \*\*Job Description Analysis:\*\* Identifies skills mentioned in job requirements.

\- \*\*Skill Matching:\*\* Highlights skills found in both the resume and job description.

\- \*\*Potential Skill Gaps:\*\* Identifies job requirements not detected in the resume.

\- \*\*Application Message Generator:\*\* Creates a professional, role-specific application message using detected matching skills.

\- \*\*Input Validation:\*\* Rejects empty and excessively long inputs.

\- \*\*Automated Testing:\*\* Includes tests for API endpoints, input validation, skill analysis, and message generation.



\## Tech Stack



\- Python

\- FastAPI

\- Pydantic

\- Pytest



\## Project Structure



```text

ai-job-application-copilot/

├── app/

│   ├── main.py

│   ├── analyzer.py

│   └── message\_generator.py

├── tests/

│   ├── test\_main.py

│   └── test\_message\_generator.py

├── requirements.txt

├── ai-usage-log.md

├── intent.md

└── README.md

```



\## Setup and Installation



1\. Clone the repository:



&#x20;  ```bash

&#x20;  git clone YOUR\_GITHUB\_REPOSITORY\_URL

&#x20;  cd ai-job-application-copilot

&#x20;  ```



2\. Create a virtual environment:



&#x20;  ```bash

&#x20;  python -m venv .venv

&#x20;  ```



3\. Activate it on Windows PowerShell:



&#x20;  ```powershell

&#x20;  .\\.venv\\Scripts\\Activate.ps1

&#x20;  ```



4\. Install dependencies:



&#x20;  ```bash

&#x20;  pip install -r requirements.txt

&#x20;  ```



\## Run the Application



```bash

uvicorn app.main:app --reload

```



Open the interactive API documentation:



http://127.0.0.1:8000/docs



\## API Endpoints



| Method | Endpoint | Description |

|---|---|---|

| GET | `/` | Checks the application status |

| GET | `/health` | Health check |

| POST | `/analyze` | Analyzes resume skills against job requirements |

| POST | `/generate-message` | Generates a professional application message |



The POST endpoints accept a resume and a job description as text.



\## Run Tests



```bash

python -m pytest -q

```



The current test suite contains 9 passing tests.



\## Limitations



\- Skill detection uses a predefined skill catalog and phrase matching.

\- Potential gaps indicate skills not detected in the supplied resume; they do not prove that a candidate lacks those skills.

\- Application messages are template-based drafts and should be reviewed before sending.

\- This project does not make hiring decisions or guarantee job suitability.



\## Future Improvements



\- Add semantic skill matching.

\- Support PDF and DOCX resume uploads.

\- Add customizable application-message templates.

\- Improve skill extraction using NLP or an LLM.

\- Add a web interface for resume analysis and message generation.



\## Author



Sakthi Ponraj



AI/ML Engineer | Generative AI | LLMs | RAG | FastAPI

