import os

import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_summary(summary):

    prompt = f"""
You are a clinical discharge assistant.

Generate a concise discharge summary.

Diagnoses:
{summary.diagnoses}

Medications:
{summary.medications}

Pending Results:
{summary.pending_results}

Return:
1. Diagnoses
2. Discharge Medications
3. Pending Follow Up Items
4. Patient Instructions
"""

    response = model.generate_content(prompt)

    return response.text