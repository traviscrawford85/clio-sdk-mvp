from clio_sdk_mvp.clio_sdk.client.clio_sdk import ClioSDK
import logging

logger = logging.getLogger(__name__)


class ClioTaskService:
    def __init__(self, clio_sdk: ClioSDK):
        self.clio_sdk = clio_sdk

    def create_clio_task(self, title: str, matter_id: str | None = None) -> str:
        logger.info(f"Creating task with title: {title}, matter_id: {matter_id}")
        # Example: Use the ClioSDK's task API (adjust as needed for your SDK)
        # result = self.clio_sdk.task.create_task({"title": title, "matter_id": matter_id})
        # task_id = result["id"]
        # For now, simulate task creation for debugging
        task_id = "fake-task-id-1234"
        logger.info(f"Successfully created task with ID: {task_id}")
        return task_id