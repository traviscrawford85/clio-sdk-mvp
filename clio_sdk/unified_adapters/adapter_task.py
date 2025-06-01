from clio_client.models import Task as ClioTask
from clio_sdk.adapter_factory.base import make_model_adapter
from clio_sdk.unified_models.task import Task as DomainTask

adapter = make_model_adapter(ClioTask, DomainTask, name="task")
