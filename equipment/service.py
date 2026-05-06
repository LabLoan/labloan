from core.errors import BookingError, NotAllowedError
from core.roles import Role
from equipment.models import EQUIPMENT, STATUS_AVAILABLE, STATUS_IN_REPAIR, Equipment


def list_equipment() -> list[Equipment]:
    return sorted(EQUIPMENT.values(), key=lambda e: e.name)


def get_equipment(equipment_id: int) -> Equipment:
    equipment = EQUIPMENT.get(equipment_id)
    if equipment is None:
        raise BookingError(f"equipment {equipment_id} does not exist")
    return equipment


def set_status(equipment_id: int, status: str, actor_role: Role) -> Equipment:
    if actor_role not in (Role.LAB_TECHNICIAN, Role.LAB_MANAGER):
        raise NotAllowedError("only lab staff can change equipment status")
    if status not in (STATUS_AVAILABLE, STATUS_IN_REPAIR):
        raise BookingError(f"unknown status {status}")
    equipment = get_equipment(equipment_id)
    equipment.status = status
    return equipment
