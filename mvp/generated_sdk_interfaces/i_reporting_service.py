"""
Reporting Interface
"""
from typing import Any, Protocol

class IReportingService(Protocol):
    
    def report_index(self, self, **kwargs) -> Any:
        ...
    
    def report_create(self, self, **kwargs) -> Any:
        ...
    
    def report_show(self, self, **kwargs) -> Any:
        ...
    
    def report_download(self, self, **kwargs) -> Any:
        ...
    
    def reportpreset_index(self, self, **kwargs) -> Any:
        ...
    
    def reportpreset_create(self, self, **kwargs) -> Any:
        ...
    
    def reportpreset_destroy(self, self, **kwargs) -> Any:
        ...
    
    def reportpreset_show(self, self, **kwargs) -> Any:
        ...
    
    def reportpreset_update(self, self, **kwargs) -> Any:
        ...
    
    def reportpreset_generate_report(self, self, **kwargs) -> Any:
        ...
    
    def reportschedule_index(self, self, **kwargs) -> Any:
        ...
    
    def reportschedule_create(self, self, **kwargs) -> Any:
        ...
    
    def reportschedule_destroy(self, self, **kwargs) -> Any:
        ...
    
    def reportschedule_show(self, self, **kwargs) -> Any:
        ...
    
    def reportschedule_update(self, self, **kwargs) -> Any:
        ...
    