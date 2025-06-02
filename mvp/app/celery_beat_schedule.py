# celerybeat_schedule.py

# Placeholder for scheduled jobs

from app.celery_tasks.document_tasks import generate_lor_docx

CELERYBEAT_SCHEDULE = {
    # Example scheduled task (commented out for now)
    # "generate_test_lor_every_hour": {
    #     "task": "app.celery_tasks.document_tasks.generate_lor_docx",
    #     "schedule": 3600.0,  # every hour
    #     "args": (1234, 5678),  # example matter_id, task_id
    # }
}
