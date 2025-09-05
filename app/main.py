from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# ✅ Enable CORS for both local dev and S3-hosted frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Google Form endpoint
GOOGLE_FORM_URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSeNda3ZLK5B4FICiC6QbFLDxGFtIDGu6CqF4joaS6CyRB1Icg/formResponse"

@app.post("/submit_form")
def submit_form(
    name: str = Form(...),
    phone: str = Form(...),
    contact_name: str = Form(...),
    q1: str = Form(...),
    q2: str = Form(...)
):
    # Map fields to Google Form entry IDs
    data = {
        "entry.884484314": name,
        "entry.404637791": phone,
        "entry.1917740154": contact_name,
        "entry.2034379466": q1,
        "entry.2060749804": q2
    }

    try:
        resp = requests.post(GOOGLE_FORM_URL, data=data)
        return {
            "detail": "Form submitted successfully",
            "status_code": resp.status_code
        }
    except Exception as e:
        return {
            "detail": f"Submission failed: {str(e)}",
            "status_code": 500
        }