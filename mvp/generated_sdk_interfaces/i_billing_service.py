"""
Billing Interface
"""
from typing import Any, Protocol

class IBillingService(Protocol):
    
    def bill_index(self, self, **kwargs) -> Any:
        ...
    
    def bill_destroy(self, self, **kwargs) -> Any:
        ...
    
    def bill_show(self, self, **kwargs) -> Any:
        ...
    
    def bill_update(self, self, **kwargs) -> Any:
        ...
    
    def bill_preview(self, self, **kwargs) -> Any:
        ...
    
    def billableclient_index(self, self, **kwargs) -> Any:
        ...
    
    def billablematter_index(self, self, **kwargs) -> Any:
        ...
    
    def billablematter_ids(self, self, **kwargs) -> Any:
        ...
    
    def billtheme_index(self, self, **kwargs) -> Any:
        ...
    
    def billtheme_update(self, self, **kwargs) -> Any:
        ...
    
    def interestcharge_index(self, self, **kwargs) -> Any:
        ...
    
    def interestcharge_destroy(self, self, **kwargs) -> Any:
        ...
    
    def lineitem_index(self, self, **kwargs) -> Any:
        ...
    
    def lineitem_destroy(self, self, **kwargs) -> Any:
        ...
    
    def lineitem_update(self, self, **kwargs) -> Any:
        ...
    
    def outstandingclientbalance_index(self, self, **kwargs) -> Any:
        ...
    