from abc import ABC, abstractmethod
from typing import Dict, List


class ICustomFieldService(ABC):
    @abstractmethod
    def get_custom_fields(self) -> List[Dict]: ...
    
    @abstractmethod
    def get_custom_field(self, field_id: str) -> Dict: ...
    
    @abstractmethod
    def update_custom_field(self, field_id: str, value: str) -> None: ...