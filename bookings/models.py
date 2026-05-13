from dataclasses import dataclass
from datetime import datetime

STATUS_PENDING = "PENDING"
STATUS_APPROVED = "APPROVED"
STATUS_REJECTED = "REJECTED"
STATUS_CANCELLED = "CANCELLED"


@dataclass
class Booking:
    id: int
    student_id: int
    equipment_id: int
    start: datetime
    end: datetime
    status: str = STATUS_PENDING


BOOKINGS: dict[int, Booking] = {}
