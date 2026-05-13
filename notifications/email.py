import logging

from bookings.models import Booking

logger = logging.getLogger("labloan.email")


def send_email(to: str, subject: str, body: str) -> None:
    logger.info("email to=%s subject=%s", to, subject)


def render_booking_confirmed(booking: Booking, equipment_name: str) -> tuple[str, str]:
    subject = f"Booking confirmed: {equipment_name}"
    body = (
        f"Your booking for {equipment_name} is confirmed.\n"
        f"From {booking.start:%Y-%m-%d %H:%M} to {booking.end:%Y-%m-%d %H:%M}."
    )
    return subject, body


def render_booking_rejected(booking: Booking, reason: str) -> tuple[str, str]:
    subject = "Booking rejected"
    body = f"Your booking {booking.id} was rejected.\nReason: {reason}"
    return subject, body
