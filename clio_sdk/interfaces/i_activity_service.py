from abc import ABC, abstractmethod
from typing import Dict, List


class IActivityService(ABC):
    @abstractmethod
    def get_activities(self, matter_id: str = None) -> List[Dict]: ...
    
    @abstractmethod
    def create_activity(self, data: Dict) -> Dict: ...