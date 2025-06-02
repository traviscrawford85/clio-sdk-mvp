"""
LegalAidEngland&amp;Wales Interface
"""
from typing import Any, Protocol

class ILegalAidEngland&amp;WalesService(Protocol):
    
    def laukcivilcontrolledrate_index(self, self, **kwargs) -> Any:
        ...
    
    def laukcivilcertificatedrate_index(self, self, **kwargs) -> Any:
        ...
    
    def laukcriminalcontrolledrate_index(self, self, **kwargs) -> Any:
        ...
    
    def expensecategory_index(self, self, **kwargs) -> Any:
        ...
    
    def expensecategory_create(self, self, **kwargs) -> Any:
        ...
    
    def expensecategory_destroy(self, self, **kwargs) -> Any:
        ...
    
    def expensecategory_show(self, self, **kwargs) -> Any:
        ...
    
    def expensecategory_update(self, self, **kwargs) -> Any:
        ...
    
    def laukexpensecategory_index(self, self, **kwargs) -> Any:
        ...
    