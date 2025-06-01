from abc import ABC, abstractmethod
from typing import Dict, List


class ICalendarService(ABC):
    @abstractmethod
    def get_events(self, calendar_id: str = None) -> List[Dict]: ...
    
    @abstractmethod
    def create_event(self, data: Dict) -> Dict: ...