"""
Api Interface
"""
from typing import Any, Protocol

class IApiService(Protocol):
    
    def customaction_index(self, self, **kwargs) -> Any:
        ...
    
    def customaction_create(self, self, **kwargs) -> Any:
        ...
    
    def customaction_destroy(self, self, **kwargs) -> Any:
        ...
    
    def customaction_show(self, self, **kwargs) -> Any:
        ...
    
    def customaction_update(self, self, **kwargs) -> Any:
        ...
    
    def webhook_index(self, self, **kwargs) -> Any:
        ...
    
    def webhook_create(self, self, **kwargs) -> Any:
        ...
    
    def webhook_destroy(self, self, **kwargs) -> Any:
        ...
    
    def webhook_show(self, self, **kwargs) -> Any:
        ...
    
    def webhook_update(self, self, **kwargs) -> Any:
        ...
    