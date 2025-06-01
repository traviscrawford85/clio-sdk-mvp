from abc import ABC, abstractmethod
from typing import Dict


class IStatuteSyncApiService(ABC):
    @abstractmethod
    async def sync_statute_to_matter(self, matter_id: int) -> Dict:
        pass

