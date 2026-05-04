from enum import Enum


class Role(str, Enum):
    STUDENT = "student"
    LAB_TECHNICIAN = "lab_technician"
    LAB_MANAGER = "lab_manager"
    ADMIN = "admin"
