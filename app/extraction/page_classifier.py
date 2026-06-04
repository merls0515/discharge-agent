def classify_page(text):

    text = text.lower()

    if "diagnosis" in text:
        return "discharge_summary"

    if "medicine" in text:
        return "medication_page"

    if "tablet" in text:
        return "medication_page"

    if "haemoglobin" in text:
        return "lab_results"

    if "hemoglobin" in text:
        return "lab_results"

    if "x-ray" in text:
        return "radiology"

    if "ct scan" in text:
        return "radiology"

    return "other"