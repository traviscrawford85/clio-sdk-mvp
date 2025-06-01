# adapter_factory/transformers/context.py
from typing import Callable, Dict, Optional


class AdapterContext:
    def __init__(
        self,
        user_lookup: Optional[Callable[[int], dict]] = None,
        matter_lookup: Optional[Callable[[int], dict]] = None,
        task_lookup_by_matter: Optional[Callable[[int], list]] = None,
    ):
        self.user_lookup = user_lookup
        self.matter_lookup = matter_lookup
        self.task_lookup_by_matter = task_lookup_by_matter

    def as_dict(self) -> Dict[str, Optional[Callable]]:
        return {
            "user_lookup": self.user_lookup,
            "matter_lookup": self.matter_lookup,
            "task_lookup_by_matter": self.task_lookup_by_matter,
        }
