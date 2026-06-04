from app.tools.load_cached_text import load_cached_text
from app.tools.diagnosis_extractor import extract_diagnoses
from app.tools.medication_extractor import extract_medications
from app.tools.pending_results_extractor import extract_pending_results
from app.tools.medication_reconcile import reconcile_medications
from app.tools.conflict_detector import detect_conflicts

from app.tools.date_extractor import extract_dates
from app.tools.allergy_extractor import extract_allergies
from app.tools.course_extractor import extract_hospital_course

from app.tools.trace_logger import (
    log_step,
    save_trace
)

from app.agents.summary_generator import build_summary
from app.agents.gemini_summary import generate_summary

pages = load_cached_text()

all_diagnoses = []
all_medications = []
all_pending = []

for page in pages:

    all_diagnoses.extend(
        extract_diagnoses(
            page["text"],
            page["page_number"]
        )
    )

    all_medications.extend(
        extract_medications(
            page["text"],
            page["page_number"]
        )
    )

    all_pending.extend(
        extract_pending_results(
            page["text"],
            page["page_number"]
        )
    )

# Trace logging

log_step(
    "extract_diagnoses",
    f"{len(all_diagnoses)} diagnoses found"
)

log_step(
    "extract_medications",
    f"{len(all_medications)} medications found"
)

# Extract additional fields

dates = extract_dates(pages)

allergies = extract_allergies(pages)

hospital_course = extract_hospital_course(pages)

# Remove duplicate pending results

unique_pending = []
seen = set()

for item in all_pending:

    if item.test_name not in seen:

        unique_pending.append(item)

        seen.add(item.test_name)

log_step(
    "extract_pending_results",
    f"{len(unique_pending)} pending results found"
)

summary = build_summary(
    diagnoses=all_diagnoses,
    medications=all_medications,
    pending_results=unique_pending
)

# Conflict detection

conflicts = detect_conflicts(all_diagnoses)

summary.conflicts = conflicts

log_step(
    "detect_conflicts",
    f"{len(conflicts)} conflicts found"
)

# Medication reconciliation

medication_changes = reconcile_medications(
    admission=[],
    discharge=all_medications
)

summary.medication_changes = medication_changes

# Additional metadata

if len(dates) >= 1:
    summary.admission_date = dates[0]

if len(dates) >= 2:
    summary.discharge_date = dates[1]

summary.allergies = allergies

summary.hospital_course = hospital_course

summary.discharge_condition = "MISSING"

final_summary = generate_summary(summary)

log_step(
    "generate_summary",
    "summary generated successfully"
)

print("\n")
print("=" * 80)
print("FINAL DISCHARGE SUMMARY")
print("=" * 80)
print("\n")

with open(
    "outputs/final_discharge_summary.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(final_summary)

print("Summary saved to outputs/final_discharge_summary.txt")

save_trace()