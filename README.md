# LabLoan

LabLoan lets students of a university lab borrow equipment such as microscopes,
3D printers and oscilloscopes. Students book a time slot, a Lab Technician
approves bookings for restricted equipment, and people get an email about the
outcome.

## Roles

| Role | What they do |
|---|---|
| Student | Books equipment, cancels bookings, joins the waitlist |
| Lab Technician | Approves or rejects bookings for restricted equipment, marks equipment as in repair |
| Lab Manager | Oversees the lab and its equipment list |
| Admin | Manages accounts |

## How a booking works

1. A student picks equipment and a start and end time.
2. The booking is refused if the equipment is in repair, the slot overlaps another
   booking, or the student already has the maximum number of active bookings.
3. Bookings for unrestricted equipment are approved at once. Bookings for restricted
   equipment wait for a Lab Technician.
4. A student who cancels late, or returns equipment late, gets penalty points.
5. If the equipment is fully booked, a student can join the waitlist.

See `docs/` for the booking rules, the approval flow and notifications.

## Layout

```
core/            roles, settings, errors
equipment/       equipment records and status
bookings/        booking rules, booking service, waitlist
penalties/       penalty points
notifications/   email rendering and sending
api/             route table
tests/           unit tests
```

## Running the tests

```
python -m pytest
```
