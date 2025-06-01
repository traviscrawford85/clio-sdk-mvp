from abc import ABC, abstractmethod
from typing import Any, Dict


class ILlmAgentService(ABC):
    @abstractmethod
    def run_agent(self, prompt: str, context: Dict = None) -> Any: ...