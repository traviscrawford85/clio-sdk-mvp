# app/dispatcher/dispatcher.py

from app.celery_tasks.document_tasks import generate_lor_docx

# Simple task type mappings
TASK_TYPE_DISPATCH_MAP = {
    "Send LOR to Insurance": generate_lor_docx,
}

def dispatch_task(task_type: str, matter_id: int, task_id: int):
    """Dispatch a task based on its type."""
    task_function = TASK_TYPE_DISPATCH_MAP.get(task_type)
    if not task_function:
        print(f"❗ No dispatch rule for task type: {task_type}")
        return False

    # Fire the corresponding Celery background task
    task_function.delay(matter_id, task_id)
    print(f"🚀 Dispatched {task_type} for Matter {matter_id}, Task {task_id}")
    return True
