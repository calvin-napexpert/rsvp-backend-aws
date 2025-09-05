from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# ✅ Enable CORS before defining routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://localhost:3000"] for your React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Correct Google Form "formResponse" URL
GOOGLE_FORM_URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSeNda3ZLK5B4FICiC6QbFLDxGFtIDGu6CqF4joaS6CyRB1Icg/formResponse"

@app.post("/submit_form")
def submit_form(
    name: str = Form("..."),
    phone: str = Form("."),
    contact_name: str = Form("..."),
    q1: str = Form("..."),
    q2: str = Form("...")
):
    # Map function arguments to Google Form entry IDs
    data = {
        "entry.884484314": name,
        "entry.404637791": phone,
        "entry.1917740154": contact_name,
        "entry.2034379466": q1,
        "entry.2060749804": q2
    }

    resp = requests.post(GOOGLE_FORM_URL, data=data)

    return {
        "detail": "Form submitted",
        "status_code": resp.status_code
    }