def events(report, stage=None, event=None):
    """
    Return Analysis Trace events, optionally filtered by stage and/or event.
    """

    trace = report.get("Analysis Trace", [])

    results = []

    for entry in trace:

        if stage is not None and entry.get("stage") != stage:
            continue

        if event is not None and entry.get("event") != event:
            continue

        results.append(entry)

    return results


def events_for_stage(report, stage):
    """
    Return all events for a pipeline stage.
    """

    return events(report, stage=stage)


def first_event(report, event):
    """
    Return the first occurrence of an event.
    """

    matches = events(report, event=event)

    if not matches:
        return None

    return matches[0]


def last_event(report, event):
    """
    Return the most recent occurrence of an event.
    """

    matches = events(report, event=event)

    if not matches:
        return None

    return matches[-1]


def has_event(report, event):
    """
    Return True if an event exists.
    """

    return first_event(report, event) is not None


def count_events(report, event=None, stage=None):
    """
    Count events matching the given filters.
    """

    return len(events(
        report,
        stage=stage,
        event=event,
    ))


def stages(report):
    """
    Return the pipeline stages in the order they first appear.
    """

    ordered = []

    for entry in report.get("Analysis Trace", []):

        stage = entry.get("stage")

        if stage not in ordered:
            ordered.append(stage)

    return ordered

def unique_events(report):
    """
    Return event types in the order they first appear.
    """

    ordered = []

    for entry in report.get("Analysis Trace", []):

        event = entry.get("event")

        if event not in ordered:
            ordered.append(event)

    return ordered