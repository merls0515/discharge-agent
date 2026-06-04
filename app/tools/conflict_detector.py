from pydantic import BaseModel


class Conflict(BaseModel):

    category: str

    details: str


def detect_conflicts(diagnoses):

    unique_dx = {
        dx.diagnosis_name
        for dx in diagnoses
    }

    if len(unique_dx) > 1:

        return [
            Conflict(
                category="diagnosis",
                details=", ".join(unique_dx)
            )
        ]

    return []