from enum import Enum


class MatterCreatedWebhookEventEvent(str, Enum):
    MATTER_CREATED = "matter.created"

    def __str__(self) -> str:
        return str(self.value)
