from app.state.schemas import PendingResult


def extract_pending_results(text, page_num):

    results = []

    lower_text = text.lower()

    if (
        "culture and sensitivity" in lower_text
        and "report awaited" in lower_text
    ):
        results.append(
            PendingResult(
                test_name="Urine Culture and Sensitivity",
                page_number=page_num,
                evidence="culture and sensitivity report awaited"
            )
        )

    return results