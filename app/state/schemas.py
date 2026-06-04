from pydantic import BaseModel


class DiagnosisFact(BaseModel):
    diagnosis_name: str
    page_number: int


class MedicationFact(BaseModel):
    name: str
    dosage: str
    frequency: str
    page_number: int

class PendingResult(BaseModel):
    test_name: str
    page_number: int    