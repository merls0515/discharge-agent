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