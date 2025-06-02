# app/core/task_status_enum.py

from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    IN_REVIEW = "In Review"
    COMPLETE = "Complete"