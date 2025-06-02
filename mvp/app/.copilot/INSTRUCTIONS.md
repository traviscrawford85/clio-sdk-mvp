"""
GitHub Copilot Task Generation Guide for Celery + Jinja Integration

You're working inside the `celery/` module of a Clio-integrated legal automation project.

GOAL:
- Build a modular Celery task queue system that interacts with the `clio_sdk` and `clio_client`.
- Support document generation, task orchestration, record processing, and Slack notifications.

PROJECT CONTEXT:
- Long-running tasks should be handled using Celery and `@shared_task`.
- Task inputs may come from YAML schemas and include fields like `title`, `client`, `matter_id`, `tasks`, etc.
- Generated documents should be rendered via Jinja2 templates stored in `templates/documents/*.j2`.

TEMPLATES:
- Use Jinja2 to render dynamic documents like `matter_summary.j2`.
- Templates should accept context variables and loop over nested lists (e.g. tasks).

INTERFACE CONTRACT:
- Implement an abstract interface `ICeleryTaskQueue` with methods `enqueue()` and `chain()`.
- Provide a concrete implementation in `queues/task_queue.py`.

TASK ORGANIZATION:
- Group all Celery jobs in `jobs/` subfolder by domain (e.g. `document_tasks.py`, `matter_tasks.py`).
- Enable chaining of jobs using `celery.chain()` or via reusable pipelines (e.g. `chains/document_pipeline.py`).

EXAMPLE TASK:
- Load a YAML string and a Jinja template filename
- Render the YAML as a document using the template
- Return the rendered output or write to disk as part of a later chained task

SUGGESTED FILES TO GENERATE:
- `jobs/document_tasks.py`: includes `generate_document_from_yaml`
- `templates/documents/matter_summary.j2`: sample template for rendering
- `queues/task_queue.py`: connects task queue to job dispatching
- `chains/document_pipeline.py`: orchestrates chained execution

Ensure that each function includes docstrings and is unit-testable. Use only relative imports inside this package.
"""
