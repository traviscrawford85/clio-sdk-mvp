from abc import ABC, abstractmethod
from typing import Dict, List


class IUserService(ABC):
    @abstractmethod
    def get_users(self) -> List[Dict]: ...
    
    @abstractmethod
    def get_user(self, user_id: str) -> Dict: ...