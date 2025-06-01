# adapter_factory/transformers/task.py
from typing import Optional


def transform_task_fields(data: dict, context: Optional[dict] = None) -> dict:
    assignee = data.get("assignee", {})
    assigner = data.get("assigner", {})
    matter = data.get("matter", {})
    task_type = data.get("task_type", {})
    reminders = data.get("reminders", [])
    time_entries = data.get("time_entries", [])

    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "description": data.get("description"),
        "status": data.get("status", "pending").lower(),
        "priority": data.get("priority", "normal").lower(),
        "due_at": data.get("due_at"),
        "completed_at": data.get("completed_at"),
        "notify_completion": data.get("notify_completion"),
        "assignee": {
            "id": assignee.get("id"),
            "name": assignee.get("name"),
            "email": assignee.get("email", None)
        },
        "assigner": {
            "id": assigner.get("id"),
            "name": assigner.get("name"),
            "email": assigner.get("email", None)
        },
        "matter": {
            "id": matter.get("id"),
            "description": matter.get("description")
        },
        "task_type": task_type.get("name"),
        "reminders": reminders,
        "time_entries": time_entries
    }
