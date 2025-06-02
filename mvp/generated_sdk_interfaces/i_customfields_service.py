"""
CustomFields Interface
"""
from typing import Any, Protocol

class ICustomFieldsService(Protocol):
    
    def customfield_index(self, self, **kwargs) -> Any:
        ...
    
    def customfield_create(self, self, **kwargs) -> Any:
        ...
    
    def customfield_destroy(self, self, **kwargs) -> Any:
        ...
    
    def customfield_show(self, self, **kwargs) -> Any:
        ...
    
    def customfield_update(self, self, **kwargs) -> Any:
        ...
    
    def createcustomfieldvalue(self, self, **kwargs) -> Any:
        ...
    
    def customfieldset_index(self, self, **kwargs) -> Any:
        ...
    
    def customfieldset_create(self, self, **kwargs) -> Any:
        ...
    
    def customfieldset_destroy(self, self, **kwargs) -> Any:
        ...
    
    def customfieldset_show(self, self, **kwargs) -> Any:
        ...
    
    def customfieldset_update(self, self, **kwargs) -> Any:
        ...
    