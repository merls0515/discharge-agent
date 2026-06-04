import json


def load_cached_text():

    with open(
        "outputs/extracted_text.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)