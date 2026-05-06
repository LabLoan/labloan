from dataclasses import dataclass

STATUS_AVAILABLE = "AVAILABLE"
STATUS_IN_REPAIR = "IN_REPAIR"


@dataclass
class Equipment:
    id: int
    name: str
    category: str
    restricted: bool
    status: str = STATUS_AVAILABLE


EQUIPMENT: dict[int, Equipment] = {}
