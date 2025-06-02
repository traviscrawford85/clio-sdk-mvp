""" Tasks SDK Service Module """
from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
from clio_sdk_mvp.interfaces.i_tasks_service import ITasksService
from typing import Any

class TasksService(ITasksService):
    def __init__(self, sdk: ClioSDK):
        self.sdk = sdk

