from abc import ABC, abstractmethod
from typing import Dict, List


class IDocumentService(ABC):
    @abstractmethod
    def get_documents(self, matter_id: str = None) -> List[Dict]: ...
    
    @abstractmethod
    def upload_document(self, data: Dict) -> Dict: ...