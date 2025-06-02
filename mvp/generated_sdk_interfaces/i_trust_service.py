"""
Trust Interface
"""
from typing import Any, Protocol

class ITrustService(Protocol):
    
    def trustlineitem_index(self, self, **kwargs) -> Any:
        ...
    
    def trustlineitem_update(self, self, **kwargs) -> Any:
        ...
    
    def trustrequest_create(self, self, **kwargs) -> Any:
        ...
    