class BookingError(Exception):
    """The request breaks a booking rule."""


class NotAllowedError(Exception):
    """The caller's role may not do this."""
