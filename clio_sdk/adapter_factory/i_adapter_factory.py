from abc import ABC, abstractmethod
from typing import Any, Optional


class IAdapterFactory(ABC):
    @abstractmethod
    def from_clio(self, clio_obj: Any, context: Optional[dict] = None) -> Any:
        pass

    @abstractmethod
    def to_clio(self, sdk_obj: Any) -> Any:
        pass
