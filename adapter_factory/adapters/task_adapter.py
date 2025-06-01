from clio_client.models.task import ClioTask
from clio_sdk.models.task import Task
from clio_sdk.adapter_factory.base import make_model_adapter

adapter = make_model_adapter(ClioTask, Task, name="task")