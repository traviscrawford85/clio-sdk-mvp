"""
This file implements the queries interface for reading and listing task-related data from Clio.

It wraps clio_client GET operations (e.g., taskindex.sync_detailed), processes the results,
and converts them into high-level SDK models that are easier to work with.

Copilot Prompt:
- Call the raw list/read endpoint from clio_client.
- Parse the response and filter it (e.g., status == "pending").
- Use the appropriate adapter to return a list of SDK Task models.
- Provide additional query functions (e.g., get_tasks_due_this_week) to encapsulate common filtering logic.
- This module should only contain "read-only" operations (GET).
"""

from clio_client import get_client
from clio_client.api.tasks.taskindex import sync_detailed as raw_list_tasks
from clio_sdk.adapters.task import from_taskshow
from clio_sdk.generated_models.task import Task


def get_pending_tasks() -> list[Task]:
    resp = raw_list_tasks(client=get_client())
    if resp.status_code == 200 and resp.parsed:
        return [
            from_taskshow(t)
            for t in resp.parsed.tasks
            if t.status and t.status.value == "pending"
        ]
    return []
