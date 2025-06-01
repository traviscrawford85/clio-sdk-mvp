from abc import ABC, abstractmethod
from typing import Dict, List


class IContactService(ABC):
    @abstractmethod
    def get_contacts(self) -> List[Dict]: ...
    
    @abstractmethod
    def get_contact(self, contact_id: str) -> Dict: ...
    
    @abstractmethod
    def create_contact(self, data: Dict) -> Dict: ...