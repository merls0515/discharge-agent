from pydantic import BaseModel

from app.state.schemas import (
    DiagnosisFact,
    MedicationFact,
    PendingResult
)


class PatientSummary(BaseModel):

    diagnoses: list[DiagnosisFact]

    medications: list[MedicationFact]

    pending_results: list[PendingResult]

    medication_changes: dict = {}

    conflicts: list = []

    admission_date: str = "MISSING"

    discharge_date: str = "MISSING"

    hospital_course: str = "MISSING"

    allergies: str = "MISSING"

    discharge_condition: str = "MISSING"