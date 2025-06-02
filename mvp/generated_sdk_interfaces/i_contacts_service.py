"""
Contacts Interface
"""
from typing import Any, Protocol

class IContactsService(Protocol):
    
    def contact_index(self, self, **kwargs) -> Any:
        ...
    
    def contact_create(self, self, **kwargs) -> Any:
        ...
    
    def contact_destroy(self, self, **kwargs) -> Any:
        ...
    
    def contact_show(self, self, **kwargs) -> Any:
        ...
    
    def contact_update(self, self, **kwargs) -> Any:
        ...
    
    def note_index(self, self, **kwargs) -> Any:
        ...
    
    def note_create(self, self, **kwargs) -> Any:
        ...
    
    def note_destroy(self, self, **kwargs) -> Any:
        ...
    
    def note_show(self, self, **kwargs) -> Any:
        ...
    
    def note_update(self, self, **kwargs) -> Any:
        ...
    
    def logentry_index(self, self, **kwargs) -> Any:
        ...
    