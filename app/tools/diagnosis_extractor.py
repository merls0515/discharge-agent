from app.state.schemas import DiagnosisFact


def extract_diagnoses(text, page_number):

    diagnoses = []

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if (
            "acute gastroenteritis" in line.lower()
            or "urinary tract infection" in line.lower()
        ):
            diagnoses.append(
                DiagnosisFact(
                    diagnosis_name=line,
                    page_number=page_number,
                    evidence=line
                )
            )

    return diagnoses