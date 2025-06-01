from datetime import datetime

from clio_client.api.tasks import TasksApi
from clio_sdk.adapters.adapter_task import to_sdk_calendar_entry, to_sdk_task
from clio_sdk.generated_models import CalendarEntry, Task
from clio_sdk.unified_adapters import get_adapter


def get_upcoming_deadlines(within_days: int = 14) -> list[Task]:
    tasks = TasksApi().list_tasks(status="pending").data
    deadline_cutoff = datetime.utcnow().date().isoformat()
    return [
        to_sdk_task(task)
        for task in tasks
        if task.due_date and task.due_date <= deadline_cutoff
    ]

def get_conflicting_calendar_events(start_date: str, end_date: str) -> list[CalendarEntry]:
    events = CalendarEntriesApi().list_calendar_entries(start_date=start_date, end_date=end_date).data
    # Conflict resolution logic could be added here
    return [to_sdk_calendar_entry(e) for e in events]

adapter = get_adapter("matter")
return [adapter["from_clio"](m) for m in resp.parsed.matters]
