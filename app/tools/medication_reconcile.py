def reconcile_medications(admission, discharge):

    admission_set = {
        med.name.upper()
        for med in admission
    }

    discharge_set = {
        med.name.upper()
        for med in discharge
    }

    added = discharge_set - admission_set
    stopped = admission_set - discharge_set
    continued = admission_set & discharge_set

    return {
        "added": sorted(list(added)),
        "stopped": sorted(list(stopped)),
        "continued": sorted(list(continued))
    }