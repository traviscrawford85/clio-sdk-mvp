"""
ClioPayments Interface
"""
from typing import Any, Protocol

class IClioPaymentsService(Protocol):
    
    def cliopaymentslink_index(self, self, **kwargs) -> Any:
        ...
    
    def cliopaymentslink_create(self, self, **kwargs) -> Any:
        ...
    
    def cliopaymentslink_show(self, self, **kwargs) -> Any:
        ...
    
    def cliopaymentslink_update(self, self, **kwargs) -> Any:
        ...
    
    def cliopaymentspayment_index(self, self, **kwargs) -> Any:
        ...
    
    def cliopaymentspayment_show(self, self, **kwargs) -> Any:
        ...
    