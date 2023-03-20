from datetime import timedelta


def minute_interval(start, end):
    reverse = False
    if start > end:
        start, end = end, start
        reverse = True

    delta = (
        (end.hour - start.hour) * 60
        + end.minute
        - start.minute
        + (end.second - start.second) / 60.0
    )
    if reverse:
        delta = 24 * 60 - delta
    return timedelta(minutes=delta)
