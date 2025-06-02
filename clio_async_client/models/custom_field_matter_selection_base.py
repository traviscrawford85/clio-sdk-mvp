from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldMatterSelectionBase")


@_attrs_define
class CustomFieldMatterSelectionBase:
    """
    Attributes:
        display_number (Union[Unset, str]): The reference and label of the *CustomFieldMatterSelection*. Depending on
            the account's manual_matter_numbering setting, this is either read only (generated) or customizable.
        id (Union[Unset, int]): Unique identifier for the *CustomFieldMatterSelection*
    """

    display_number: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_number = self.display_number

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_number is not UNSET:
            field_dict["display_number"] = display_number
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_number = d.pop("display_number", UNSET)

        id = d.pop("id", UNSET)

        custom_field_matter_selection_base = cls(
            display_number=display_number,
            id=id,
        )

        custom_field_matter_selection_base.additional_properties = d
        return custom_field_matter_selection_base

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
