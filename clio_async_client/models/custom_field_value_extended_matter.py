from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldValueExtendedMatter")


@_attrs_define
class CustomFieldValueExtendedMatter:
    """
    Attributes:
        id (Union[Unset, int]):
        display_number (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    display_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_number = self.display_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if display_number is not UNSET:
            field_dict["display_number"] = display_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        display_number = d.pop("display_number", UNSET)

        custom_field_value_extended_matter = cls(
            id=id,
            display_number=display_number,
        )

        custom_field_value_extended_matter.additional_properties = d
        return custom_field_value_extended_matter

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
