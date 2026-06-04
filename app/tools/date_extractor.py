import re


def extract_dates(pages):

    pattern = r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b"

    matches = []

    for page in pages[:5]:

        dates = re.findall(
            pattern,
            page["text"]
        )

        matches.extend(dates)

    return matches