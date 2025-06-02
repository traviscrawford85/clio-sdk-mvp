"""
Settings Interface
"""
from typing import Any, Protocol

class ISettingsService(Protocol):
    
    def textsnippet_index(self, self, **kwargs) -> Any:
        ...
    
    def textsnippet_create(self, self, **kwargs) -> Any:
        ...
    
    def textsnippet_destroy(self, self, **kwargs) -> Any:
        ...
    
    def textsnippet_show(self, self, **kwargs) -> Any:
        ...
    
    def textsnippet_update(self, self, **kwargs) -> Any:
        ...
    
    def billingsetting_show(self, self, **kwargs) -> Any:
        ...
    
    def currency_index(self, self, **kwargs) -> Any:
        ...
    