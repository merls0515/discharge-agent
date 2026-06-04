def extract_hospital_course(pages):

    keywords = [
        "hospital course",
        "course in hospital",
        "course of treatment"
    ]

    for page in pages:

        text = page["text"]

        lower_text = text.lower()

        for keyword in keywords:

            if keyword in lower_text:

                return text[:1000]

    return "MISSING"