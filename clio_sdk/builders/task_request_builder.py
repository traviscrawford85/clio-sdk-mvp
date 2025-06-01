# builders/task_calendar_document_builders.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from clio_client.models.task_create_request import TaskCreateRequest
from clio_client.models.task_create_request_data import TaskCreateRequestData
from clio_client.models.task_create_request_data_assignee import (
    TaskCreateRequestDataAssignee,
)
from clio_client.models.task_create_request_data_matter import (
    TaskCreateRequestDataMatter,
)
from clio_client.models.task_create_request_data_task_type import (
    TaskCreateRequestDataTaskType,
)


# Input model for creating/updating tasks
class TaskInputModel(BaseModel):
    name: str
    description: str
    due_at: Optional[str] = None
    assignee_id: Optional[int] = None
    matter_id: Optional[int] = None
    task_type_id: Optional[int] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    notify_assignee: Optional[bool] = None
    notify_completion: Optional[bool] = None
    permission: Optional[str] = None
    time_estimated: Optional[int] = None
    statute_of_limitations: Optional[bool] = None


def build_task_create_request(input: TaskInputModel) -> TaskCreateRequest:
    data_kwargs = input.model_dump(exclude_unset=True)

    if input.assignee_id:
        data_kwargs["assignee"] = TaskCreateRequestDataAssignee(id=input.assignee_id)
    if input.matter_id:
        data_kwargs["matter"] = TaskCreateRequestDataMatter(id=input.matter_id)
    if input.task_type_id:
        data_kwargs["task_type"] = TaskCreateRequestDataTaskType(id=input.task_type_id)

    return TaskCreateRequest(data=TaskCreateRequestData(**data_kwargs))

