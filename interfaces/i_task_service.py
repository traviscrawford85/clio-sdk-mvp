from abc import ABC, abstractmethod
from typing import Any, Dict, List


class ITaskService(ABC):
    @abstractmethod
    def get_tasks(self, matter_id: str = None) -> List[Dict]: ...
    
    @abstractmethod
    def create_task(self, data: Dict) -> Dict: ...
    
    @abstractmethod
    def complete_task(self, task_id: str) -> None: ...