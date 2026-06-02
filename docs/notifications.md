# Notifications

LabLoan sends notifications by email only. Other channels are not supported.

| Event | Who gets it | Content |
|---|---|---|
| Booking approved | The student | Equipment name, start and end time |
| Booking rejected | The student | Equipment name and the reason |

Emails are rendered in `notifications/email.py` and sent from
`notifications/dispatcher.py`.
