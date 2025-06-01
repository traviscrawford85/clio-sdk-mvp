from pydantic import BaseModel
from typing import Any

class ClioBaseModel(BaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        use_enum_values = True
        alias_generator = staticmethod(lambda s: ''.join([s[0].lower()]+[c if c.islower() else '_'+c.lower() for c in s[1:]]))
        # This alias_generator converts CamelCase to snake_case for field names

    def to_dict(self, **kwargs) -> dict[str, Any]:
        return self.dict(by_alias=True, exclude_unset=True, **kwargs)
