"""
CourtRules Interface
"""
from typing import Any, Protocol

class ICourtRulesService(Protocol):
    
    def jurisdictionstotrigger_index(self, self, **kwargs) -> Any:
        ...
    
    def jurisdictionstotrigger_show(self, self, **kwargs) -> Any:
        ...
    
    def jurisdiction_index(self, self, **kwargs) -> Any:
        ...
    
    def jurisdiction_show(self, self, **kwargs) -> Any:
        ...
    
    def matterdocket_index(self, self, **kwargs) -> Any:
        ...
    
    def matterdocket_create(self, self, **kwargs) -> Any:
        ...
    
    def matterdocket_preview(self, self, **kwargs) -> Any:
        ...
    
    def matterdocket_destroy(self, self, **kwargs) -> Any:
        ...
    
    def matterdocket_show(self, self, **kwargs) -> Any:
        ...
    
    def servicetype_index(self, self, **kwargs) -> Any:
        ...
    
    def servicetype_show(self, self, **kwargs) -> Any:
        ...
    