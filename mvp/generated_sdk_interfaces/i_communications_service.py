"""
Communications Interface
"""
from typing import Any, Protocol

class ICommunicationsService(Protocol):
    
    def communication_index(self, self, **kwargs) -> Any:
        ...
    
    def communication_create(self, self, **kwargs) -> Any:
        ...
    
    def communication_destroy(self, self, **kwargs) -> Any:
        ...
    
    def communication_show(self, self, **kwargs) -> Any:
        ...
    
    def communication_update(self, self, **kwargs) -> Any:
        ...
    
    def conversation_index(self, self, **kwargs) -> Any:
        ...
    
    def conversation_show(self, self, **kwargs) -> Any:
        ...
    
    def conversation_update(self, self, **kwargs) -> Any:
        ...
    
    def conversationmessage_index(self, self, **kwargs) -> Any:
        ...
    
    def conversationmessage_create(self, self, **kwargs) -> Any:
        ...
    
    def conversationmessage_show(self, self, **kwargs) -> Any:
        ...
    