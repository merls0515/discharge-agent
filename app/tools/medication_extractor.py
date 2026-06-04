from app.state.schemas import MedicationFact


def extract_medications(text, page_number):

    medications = []

    lines = text.split("\n")

    for line in lines:

        clean_line = line.strip()

        upper_line = clean_line.upper()

        if (
            upper_line.startswith("TAB")
            or upper_line.startswith("TAB.")
            or upper_line.startswith("TAR")
            or upper_line.startswith("TA*")
            or upper_line.startswith("TA#")
            or upper_line.startswith("INJ")
            or upper_line.startswith("CAP")
        ):

            medications.append(
                MedicationFact(
                    name=clean_line,
                    dosage="",
                    frequency="",
                    page_number=page_number
                )
            )

    return medications