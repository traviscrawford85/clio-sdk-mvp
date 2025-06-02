"""
Users Interface
"""
from typing import Any, Protocol

class IUsersService(Protocol):
    
    def user_index(self, self, **kwargs) -> Any:
        ...
    
    def user_who_am_i(self, self, **kwargs) -> Any:
        ...
    
    def user_show(self, self, **kwargs) -> Any:
        ...
    
    def group_index(self, self, **kwargs) -> Any:
        ...
    
    def group_create(self, self, **kwargs) -> Any:
        ...
    
    def group_destroy(self, self, **kwargs) -> Any:
        ...
    
    def group_show(self, self, **kwargs) -> Any:
        ...
    
    def group_update(self, self, **kwargs) -> Any:
        ...
    