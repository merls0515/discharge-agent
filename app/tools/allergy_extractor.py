def extract_allergies(pages):

    keywords = [
        "allergy",
        "allergies",
        "drug allergy"
    ]

    for page in pages:

        text = page["text"]

        lower_text = text.lower()

        for keyword in keywords:

            if keyword in lower_text:

                return text[:300]

    return "MISSING"