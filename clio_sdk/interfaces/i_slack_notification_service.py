from abc import ABC, abstractmethod


class ISlackNotificationService(ABC):
    @abstractmethod
    def send_message(self, channel: str, text: str) -> None: ...