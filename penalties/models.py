from dataclasses import dataclass


@dataclass
class Penalty:
    id: int
    student_id: int
    points: int
    reason: str


PENALTIES: list[Penalty] = []
