from typing import Optional

from pydantic import BaseModel


class StatuteSyncResult(BaseModel):
    status: str
    statute_due_at: Optional[str] = None