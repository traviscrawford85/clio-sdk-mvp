from abc import ABC, abstractmethod
from typing import Any


class ICeleryTaskQueue(ABC):
    @abstractmethod
    def enqueue(self, task_name: str, *args, **kwargs) -> Any: ...