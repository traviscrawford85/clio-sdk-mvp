"""
LegalAidUS Interface
"""
from typing import Any, Protocol

class ILegalAidUSService(Protocol):
    
    def grant_index(self, self, **kwargs) -> Any:
        ...
    
    def grant_create(self, self, **kwargs) -> Any:
        ...
    
    def grant_destroy(self, self, **kwargs) -> Any:
        ...
    
    def grant_show(self, self, **kwargs) -> Any:
        ...
    
    def grant_update(self, self, **kwargs) -> Any:
        ...
    
    def grantfundingsource_index(self, self, **kwargs) -> Any:
        ...
    
    def grantfundingsource_create(self, self, **kwargs) -> Any:
        ...
    
    def grantfundingsource_destroy(self, self, **kwargs) -> Any:
        ...
    
    def grantfundingsource_update(self, self, **kwargs) -> Any:
        ...
    