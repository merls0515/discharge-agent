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

Medication Changes:
{summary.medication_changes}

Pending Results:
{summary.pending_results}

Admission Date:
{summary.admission_date}

Discharge Date:
{summary.discharge_date}

Allergies:
{summary.allergies}

Hospital Course:
{summary.hospital_course}

Discharge Condition:
{summary.discharge_condition}

Potential Conflicts:
{summary.conflicts}

Return the summary using EXACTLY these sections:

1. Diagnoses
2. Discharge Medications
3. Medication Changes
   - Added
   - Stopped
   - Continued
4. Potential Conflicts
5. Admission Date
6. Discharge Date
7. Allergies
8. Hospital Course
9. Discharge Condition
10. Pending Follow Up Items
11. Patient Instructions

Rules:
- Include ALL sections even if information is missing.
- If a value is unavailable, write "MISSING".
- Use bullet points where appropriate.
- Do not skip any section.
- Do not merge sections.
"""

    response = model.generate_content(prompt)

    return response.text