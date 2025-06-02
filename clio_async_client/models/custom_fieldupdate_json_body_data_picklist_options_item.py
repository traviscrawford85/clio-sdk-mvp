from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldupdateJsonBodyDataPicklistOptionsItem")


@_attrs_define
class CustomFieldupdateJsonBodyDataPicklistOptionsItem:
    """
    Attributes:
        field_deleted (Union[Unset, bool]): Whether or not the PicklistOption should be deleted.
        id (Union[Unset, int]): The unique identifier for a single PicklistOption associated with the CustomField. The
            keyword `null` is not valid for this field. Not required for creating new PicklistOptions, but required for
            updating or deleting existing ones.
        option (Union[Unset, str]): The option value.
    """

    field_deleted: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    option: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_deleted = self.field_deleted

        id = self.id

        option = self.option

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_deleted is not UNSET:
            field_dict["_deleted"] = field_deleted
        if id is not UNSET:
            field_dict["id"] = id
        if option is not UNSET:
            field_dict["option"] = option

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_deleted = d.pop("_deleted", UNSET)

        id = d.pop("id", UNSET)

        option = d.pop("option", UNSET)

        custom_fieldupdate_json_body_data_picklist_options_item = cls(
            field_deleted=field_deleted,
            id=id,
            option=option,
        )

        custom_fieldupdate_json_body_data_picklist_options_item.additional_properties = d
        return custom_fieldupdate_json_body_data_picklist_options_item

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
