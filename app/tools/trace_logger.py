import json

trace = []


def log_step(action, result):

    trace.append(
        {
            "action": action,
            "result": result
        }
    )


def save_trace():

    with open(
        "outputs/trace.json",
        "w"
    ) as f:

        json.dump(
            trace,
            f,
            indent=2
        )