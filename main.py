from app.tools.load_cached_text import load_cached_text
from app.tools.diagnosis_extractor import extract_diagnoses
from app.tools.medication_extractor import extract_medications
from app.tools.pending_results_extractor import extract_pending_results

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

# Remove duplicate pending results

unique_pending = []
seen = set()

for item in all_pending:

    if item.test_name not in seen:

        unique_pending.append(item)

        seen.add(item.test_name)

summary = build_summary(
    diagnoses=all_diagnoses,
    medications=all_medications,
    pending_results=unique_pending
)

final_summary = generate_summary(summary)

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