from app.state.agent_state import PatientSummary


def build_summary(

    diagnoses,
    medications,
    pending_results

):

    return PatientSummary(
        diagnoses=diagnoses,
        medications=medications,
        pending_results=pending_results
    )