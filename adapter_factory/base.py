# adapter_factory/base.py
from typing import Callable, Dict, Type

from adapter_factory.transformer import get_transformer
from pydantic import BaseModel
from clio_sdk.adapter_factory.i_adapter_factory import IAdapterFactory

AdapterFn = Callable[[BaseModel, dict], BaseModel]

adapter_registry: Dict[str, "ModelAdapter"] = {}


class ModelAdapter(IAdapterFactory):
    def __init__(self, source_model, target_model, name):
        self.source_model = source_model
        self.target_model = target_model
        self.name = name

    def from_clio(self, clio_obj, context=None):
        raw = clio_obj.model_dump()
        transformer = get_transformer(self.name)
        ctx = context if context is not None else {}
        transformed = transformer(raw, ctx) if transformer else raw
        return self.target_model(**transformed)

    def to_clio(self, sdk_obj):
        return self.source_model(**sdk_obj.model_dump())


def make_model_adapter(
    source_model: Type[BaseModel], target_model: Type[BaseModel], name: str
) -> "ModelAdapter":
    adapter = ModelAdapter(source_model, target_model, name)
    adapter_registry[name] = adapter
    return adapter


def get_adapter(name: str) -> "ModelAdapter":
    return adapter_registry[name]
