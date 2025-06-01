from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from clio_sdk.unified_models.statute import StatuteSyncResult


class IStatuteSyncDbService(ABC):
    @abstractmethod
    async def sync_statute_of_limitations_db(
        self, matter_id: int, db: Session
    ) -> StatuteSyncResult:
        pass
