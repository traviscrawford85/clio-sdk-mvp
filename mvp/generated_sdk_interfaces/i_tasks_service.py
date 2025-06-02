"""
Tasks Interface
"""
from typing import Any, Protocol

class ITasksService(Protocol):
    
    def task_index(self, self, **kwargs) -> Any:
        ...
    
    def task_create(self, self, **kwargs) -> Any:
        ...
    
    def task_destroy(self, self, **kwargs) -> Any:
        ...
    
    def task_show(self, self, **kwargs) -> Any:
        ...
    
    def task_update(self, self, **kwargs) -> Any:
        ...
    
    def tasktemplate_index(self, self, **kwargs) -> Any:
        ...
    
    def tasktemplate_create(self, self, **kwargs) -> Any:
        ...
    
    def tasktemplate_destroy(self, self, **kwargs) -> Any:
        ...
    
    def tasktemplate_show(self, self, **kwargs) -> Any:
        ...
    
    def tasktemplate_update(self, self, **kwargs) -> Any:
        ...
    
    def tasktemplatelist_index(self, self, **kwargs) -> Any:
        ...
    
    def tasktemplatelist_create(self, self, **kwargs) -> Any:
        ...
    
    def tasktemplatelist_destroy(self, self, **kwargs) -> Any:
        ...
    
    def tasktemplatelist_show(self, self, **kwargs) -> Any:
        ...
    
    def tasktemplatelist_update(self, self, **kwargs) -> Any:
        ...
    
    def tasktemplatelist_copy(self, self, **kwargs) -> Any:
        ...
    
    def tasktype_index(self, self, **kwargs) -> Any:
        ...
    
    def tasktype_create(self, self, **kwargs) -> Any:
        ...
    
    def tasktype_show(self, self, **kwargs) -> Any:
        ...
    
    def tasktype_update(self, self, **kwargs) -> Any:
        ...
    