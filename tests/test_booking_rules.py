from datetime import datetime, timedelta, timezone

import pytest

from bookings.rules import MAX_BOOKING_HOURS, overlaps
from bookings.service import create_booking
from core.errors import BookingError
from equipment.models import EQUIPMENT, Equipment

NOW = datetime(2026, 1, 12, 9, 0, tzinfo=timezone.utc)


def test_overlapping_slots_overlap():
    assert overlaps(NOW, NOW + timedelta(hours=2), NOW + timedelta(hours=1), NOW + timedelta(hours=3))


def test_back_to_back_slots_do_not_overlap():
    assert not overlaps(NOW, NOW + timedelta(hours=2), NOW + timedelta(hours=2), NOW + timedelta(hours=4))


def test_booking_longer_than_maximum_is_refused():
    EQUIPMENT[1] = Equipment(1, "Microscope", "optics", restricted=False)
    start = datetime.now(timezone.utc) + timedelta(days=2)
    with pytest.raises(BookingError):
        create_booking(1, 1, start, start + timedelta(hours=MAX_BOOKING_HOURS + 1))

