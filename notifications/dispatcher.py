from bookings.models import Booking
from core.config import EMAIL_DOMAIN
from equipment.service import get_equipment
from notifications.email import render_booking_confirmed, render_booking_rejected, send_email


def notify_booking_approved(booking: Booking) -> None:
    equipment = get_equipment(booking.equipment_id)
    subject, body = render_booking_confirmed(booking, equipment.name)
    send_email(f"student-{booking.student_id}@{EMAIL_DOMAIN}", subject, body)


def notify_booking_rejected(booking: Booking, reason: str) -> None:
    subject, body = render_booking_rejected(booking, reason)
    send_email(f"student-{booking.student_id}@{EMAIL_DOMAIN}", subject, body)
