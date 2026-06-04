# discharge-agent
<div align="center">

<br/>
█████╗  ██████╗██████╗     ██████╗ ██╗███████╗ ██████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██║██╔════╝██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝ ██╔════╝
███████║██║     ██║  ██║    ██║  ██║██║███████╗██║     ███████║███████║██████╔╝██║  ███╗█████╗
██╔══██║██║     ██║  ██║    ██║  ██║██║╚════██║██║     ██╔══██║██╔══██║██╔══██╗██║   ██║██╔══╝
██║  ██║╚██████╗██████╔╝    ██████╔╝██║███████║╚██████╗██║  ██║██║  ██║██║  ██║╚██████╔╝███████╗
╚═╝  ╚═╝ ╚═════╝╚═════╝     ╚═════╝ ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝

### **AI Clinical Discharge Summary Agent**
*Transforming unstructured clinical notes into safe, traceable, evidence-backed discharge summaries*

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_2.5_Flash-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![Clinical AI](https://img.shields.io/badge/Clinical_AI-Safety_First-E53935?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-00C853?style=for-the-badge)

</div>

---

## ⚕️ What is this?

> **A production-grade agentic AI system** that converts messy, noisy clinical source notes into structured, auditable discharge summaries — without hallucinating a single clinical fact.

Clinical notes are chaotic. They're incomplete, contradictory, and difficult to summarize manually. This system automates that process while keeping **patient safety non-negotiable**.
Clinical safety > Completeness. Always.
A MISSING field is safer than a hallucinated one.

---

## 🏗️ System Architecture
┌──────────────────────────────┐
│     Clinical Source Notes    │
└──────────────┬───────────────┘
│
▼
┌──────────────────────────────┐
│         Text Loader          │
└──────────────┬───────────────┘
│
▼
┌──────────────────────────────────────────────────┐
│              Information Extraction              │
│                                                  │
│   🔬 Diagnoses       💊 Medications              │
│   📋 Pending Results  📅 Dates                   │
│   ⚠️  Allergies       🏥 Hospital Course          │
└──────────────────────┬───────────────────────────┘
│
▼
┌──────────────────────────────────────────────────┐
│               Validation Layer                   │
│                                                  │
│   ✅ Evidence Tracking  ⚡ Conflict Detection     │
│   🔄 Medication Reconciliation                   │
│   🚨 Missing Field Detection                     │
└──────────────────────┬───────────────────────────┘
│
▼
┌──────────────────────────────┐
│      Patient Summary State   │
└──────────────┬───────────────┘
│
▼
┌──────────────────────────────┐
│   Gemini 2.5 Flash Summary   │
│         Generator            │
└──────────────┬───────────────┘
│
┌────────┴─────────┐
▼                  ▼
📄 discharge_summary   🔍 trace.json

---

## 📁 Project Structure
discharge-agent/
│
├── app/
│   ├── agents/
│   │   ├── gemini_summary.py        ← Gemini integration
│   │   └── summary_generator.py     ← Summary orchestration
│   │
│   ├── state/
│   │   ├── schemas.py               ← Pydantic data models
│   │   └── agent_state.py           ← Runtime state manager
│   │
│   └── tools/
│       ├── diagnosis_extractor.py
│       ├── medication_extractor.py
│       ├── pending_results_extractor.py
│       ├── medication_reconcile.py
│       ├── conflict_detector.py
│       ├── date_extractor.py
│       ├── allergy_extractor.py
│       ├── course_extractor.py
│       ├── trace_logger.py
│       └── load_cached_text.py
│
├── outputs/
│   ├── final_discharge_summary.txt  ← Generated summary
│   └── trace.json                   ← Execution trace
│
├── main.py
├── requirements.txt
└── README.md

---

## ✨ Core Features

<table>
<tr>
<td width="50%">

### 🔍 Evidence Tracking
Every extracted clinical fact is tied to its source — page number + raw evidence text. Nothing is assumed. Nothing is invented.

```python
DiagnosisFact(
    diagnosis_name="Urinary Tract Infection",
    page_number=1,
    evidence="2) URINARY TRACT INFECTION"
)
```

</td>
<td width="50%">

### 🔄 Medication Reconciliation
Compares admission vs discharge medications and flags what was added, stopped, or continued.

```python
{
  "added":     ["TAR RACIPER", "TAR OFLOXTZ"],
  "stopped":   [],
  "continued": []
}
```

</td>
</tr>
<tr>
<td width="50%">

### ⚡ Conflict Detection
Contradictory clinical information is surfaced — never silently ignored.

```python
Conflict(
    category="diagnosis",
    details="Multiple competing diagnoses found"
)
```

</td>
<td width="50%">

### 🚨 Missing Field Detection
No guessing. If a field can't be found, it's explicitly labeled:
Admission Date:   MISSING
Discharge Date:   MISSING
Allergies:        MISSING

</td>
</tr>
</table>

---

## 🛡️ The No-Fabrication Guarantee

This system is built around one inviolable rule:

> **If it's not in the source notes, it doesn't go in the summary.**

| Rule | Enforcement |
|------|------------|
| Facts must originate from source notes | Evidence field required on every extraction |
| Missing information is never guessed | Explicit `MISSING` label |
| Contradictions are never hidden | Surfaced as `Conflict` objects |
| Unknown values are never assumed | Empty sections preserved as-is |

---

## 📊 Trace Logging

Every processing step is logged to `outputs/trace.json` for full auditability:

```json
[
  { "action": "extract_diagnoses",      "result": "2 diagnoses found"       },
  { "action": "extract_medications",    "result": "13 medications found"     },
  { "action": "extract_pending_results","result": "1 pending results found"  },
  { "action": "detect_conflicts",       "result": "1 conflicts found"        },
  { "action": "generate_summary",       "result": "summary generated ✓"      }
]
```

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Create a .env file
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

### 3. Run

```bash
python main.py
```

### 4. View Outputs
outputs/
├── final_discharge_summary.txt   ← Your structured discharge summary
└── trace.json                    ← Full execution audit trail

---

## ✅ Implementation Status

| Feature | Status |
|---|---|
| Evidence Tracking | ✅ Implemented |
| Medication Reconciliation | ✅ Implemented |
| Conflict Detection | ✅ Implemented |
| Missing Field Detection | ✅ Implemented |
| Trace Logging | ✅ Implemented |
| Gemini-Based Summary Generation | ✅ Implemented |

---

## ⚠️ Known Limitations

- Medication extraction is **rule-based** — OCR noise can cause false positives
- Date extraction is **pattern-based** — complex formats may be missed
- Conflict detection currently checks **diagnosis diversity only**
- Allergy extraction uses **keyword matching**
- Medication reconciliation uses an **empty admission list** (baseline comparison)
- No **clinician review loop** is implemented

---

## 🔭 Roadmap
[ ] LLM-assisted evidence extraction
[ ] Advanced medication normalization
[ ] True admission/discharge medication reconciliation
[ ] Multi-pass verification agent
[ ] Reviewer agent with feedback loop
[ ] Confidence scoring per extracted fact
[ ] Clinical ontology mapping (SNOMED, ICD-10)
[ ] LangGraph-based orchestration
[ ] Automated evaluation metrics
[ ] Continuous learning loop

---

## 🧭 Engineering Priorities

This system was designed with an explicit priority order — no ambiguity:

🔴  Clinical Safety
🔴  Non-Fabrication
🟠  Traceability
🟠  Explainability
🟡  Robustness
🟢  Summary Quality


> Quality is a goal. Safety is a constraint.

---

<div align="center">

*Built with clinical safety as the foundation, not an afterthought.*

</div>
