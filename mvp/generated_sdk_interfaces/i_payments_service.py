"""
Payments Interface
"""
from typing import Any, Protocol

class IPaymentsService(Protocol):
    
    def allocation_index(self, self, **kwargs) -> Any:
        ...
    
    def allocation_show(self, self, **kwargs) -> Any:
        ...
    
    def creditmemo_index(self, self, **kwargs) -> Any:
        ...
    
    def creditmemo_show(self, self, **kwargs) -> Any:
        ...
    