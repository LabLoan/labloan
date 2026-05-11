from core.config import PENALTIES_ENABLED
from penalties.models import PENALTIES, Penalty

LATE_CANCEL_WINDOW_HOURS = 24
LATE_CANCEL_POINTS = 2
LATE_RETURN_POINTS_PER_DAY = 1


def apply_late_cancel_penalty(student_id: int, booking_id: int) -> Penalty | None:
    if not PENALTIES_ENABLED:
        return None
    penalty = Penalty(len(PENALTIES) + 1, student_id, LATE_CANCEL_POINTS, f"late cancel of booking {booking_id}")
    PENALTIES.append(penalty)
    return penalty


def apply_late_return_penalty(student_id: int, booking_id: int, days_late: int) -> Penalty | None:
    if not PENALTIES_ENABLED or days_late <= 0:
        return None
    points = days_late * LATE_RETURN_POINTS_PER_DAY
    penalty = Penalty(len(PENALTIES) + 1, student_id, points, f"late return of booking {booking_id}")
    PENALTIES.append(penalty)
    return penalty
