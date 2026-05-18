from datetime import datetime

MAX_BOOKING_HOURS = 4
MAX_ACTIVE_BOOKINGS = 3


def overlaps(a_start: datetime, a_end: datetime, b_start: datetime, b_end: datetime) -> bool:
    """Two slots overlap when each starts before the other ends."""
    return a_start < b_end and b_start < a_end
