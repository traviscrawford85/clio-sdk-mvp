from abc import ABC, abstractmethod
from typing import Any


class ILocalDbService(ABC):
    @abstractmethod
    def execute_query(self, query: str, params: tuple = ()) -> Any: ...
    
    @abstractmethod
    def fetch_one(self, query: str, params: tuple = ()) -> Any: ...
    
    @abstractmethod
    def fetch_all(self, query: str, params: tuple = ()) -> list: ...