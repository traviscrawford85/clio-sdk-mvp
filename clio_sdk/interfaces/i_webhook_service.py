from abc import ABC, abstractmethod
from typing import Dict, List


class IWebhookService(ABC):
    @abstractmethod
    def register_webhook(self, callback_url: str, event_types: List[str]) -> Dict: ...
    
    @abstractmethod
    def list_webhooks(self) -> List[Dict]: ...
    
    @abstractmethod
    def delete_webhook(self, webhook_id: str) -> None: ...