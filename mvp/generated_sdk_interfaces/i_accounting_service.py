"""
Accounting Interface
"""
from typing import Any, Protocol

class IAccountingService(Protocol):
    
    def bankaccount_index(self, self, **kwargs) -> Any:
        ...
    
    def bankaccount_create(self, self, **kwargs) -> Any:
        ...
    
    def bankaccount_destroy(self, self, **kwargs) -> Any:
        ...
    
    def bankaccount_show(self, self, **kwargs) -> Any:
        ...
    
    def bankaccount_update(self, self, **kwargs) -> Any:
        ...
    
    def banktransaction_index(self, self, **kwargs) -> Any:
        ...
    
    def banktransaction_show(self, self, **kwargs) -> Any:
        ...
    
    def banktransfer_show(self, self, **kwargs) -> Any:
        ...
    