from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommunicationcreateJsonBodyDataExternalPropertiesItem")


@_attrs_define
class CommunicationcreateJsonBodyDataExternalPropertiesItem:
    """
    Attributes:
        name (Union[Unset, str]): The ExternalProperty name. Note: **there is a limit of 5 external_properties per
            Communication**
        value (Union[Unset, str]): The ExternalProperty value.
    """

    name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        communicationcreate_json_body_data_external_properties_item = cls(
            name=name,
            value=value,
        )

        communicationcreate_json_body_data_external_properties_item.additional_properties = d
        return communicationcreate_json_body_data_external_properties_item

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
