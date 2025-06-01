from abc import ABC, abstractmethod
from typing import Dict, List


class INoteService(ABC):
    @abstractmethod
    def get_notes(self, matter_id: str = None) -> List[Dict]: ...
    
    @abstractmethod
    def create_note(self, matter_id: str, content: str) -> None: ...