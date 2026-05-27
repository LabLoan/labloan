from bookings.service import approve_booking, cancel_booking, create_booking, reject_booking
from equipment.service import list_equipment

# (method, path, handler)
ROUTES = [
    ("GET", "/equipment", list_equipment),
    ("POST", "/bookings", create_booking),
    ("DELETE", "/bookings/{id}", cancel_booking),
    ("POST", "/bookings/{id}/approve", approve_booking),
    ("POST", "/bookings/{id}/reject", reject_booking),
]
