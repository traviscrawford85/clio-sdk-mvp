"""
In-appNotifications Interface
"""
from typing import Any, Protocol

class IIn-appNotificationsService(Protocol):
    
    def myevent_index(self, self, **kwargs) -> Any:
        ...
    
    def myevent_destroy(self, self, **kwargs) -> Any:
        ...
    
    def myevent_update(self, self, **kwargs) -> Any:
        ...
    
    def eventmetrics_index(self, self, **kwargs) -> Any:
        ...
    