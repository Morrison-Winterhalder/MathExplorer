def get_events(report, stage=None, event=None):
    """
    Return Analysis Trace events, optionally filtered by stage and/or event.
    """

    events = report.get("Analysis Trace", [])

    if stage is not None:
        events = [
            e for e in events
            if e.get("stage") == stage
        ]

    if event is not None:
        events = [
            e for e in events
            if e.get("event") == event
        ]

    return events


def first_event(report, event):
    """
    Return the first occurrence of an event, or None.
    """

    events = get_events(report, event=event)

    if events:
        return events[0]

    return None


def latest_event(report, event):
    """
    Return the most recent occurrence of an event, or None.
    """

    events = get_events(report, event=event)

    if events:
        return events[-1]

    return None


def has_event(report, event):
    """
    Return True if an event exists.
    """

    return first_event(report, event) is not None