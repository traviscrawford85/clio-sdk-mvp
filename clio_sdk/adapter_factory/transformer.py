# A script that registers the transformers adapter factory.
# adapter_factory/transformers.py

from typing import Callable, Dict, Optional

TransformerFn = Callable[[dict, Optional[dict]], dict]

_registry: Dict[str, TransformerFn] = {}


def register_transformer(name: str, fn: TransformerFn):
    """Register a transformer by name."""
    _registry[name] = fn


def get_transformer(name: str) -> Optional[TransformerFn]:
    """Retrieve a registered transformer by name."""
    return _registry.get(name)
