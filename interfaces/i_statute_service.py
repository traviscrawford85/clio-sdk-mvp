from abc import ABC, abstractmethod
from typing import Optional


class IStatuteService(ABC):
    @abstractmethod
    async def compute_statute_for_matter(self, matter_id: int) -> str:
        pass

