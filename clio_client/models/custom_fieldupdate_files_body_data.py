from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_fieldupdate_files_body_data_picklist_options_item import (
        CustomFieldupdateFilesBodyDataPicklistOptionsItem,
    )


T = TypeVar("T", bound="CustomFieldupdateFilesBodyData")


@_attrs_define
class CustomFieldupdateFilesBodyData:
    """
    Attributes:
        display_order (Union[Unset, int]): The display position of the CustomField.
        displayed (Union[Unset, bool]): Whether or not the CustomField should be displayed by default. Default: True.
        name (Union[Unset, str]): CustomField name.
        picklist_options (Union[Unset, list['CustomFieldupdateFilesBodyDataPicklistOptionsItem']]):
        required (Union[Unset, bool]): Whether or not the CustomField should require a value. Default: False.
    """

    display_order: Unset | int = UNSET
    displayed: Unset | bool = True
    name: Unset | str = UNSET
    picklist_options: (
        Unset | list["CustomFieldupdateFilesBodyDataPicklistOptionsItem"]
    ) = UNSET
    required: Unset | bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_order = self.display_order

        displayed = self.displayed

        name = self.name

        picklist_options: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.picklist_options, Unset):
            picklist_options = []
            for picklist_options_item_data in self.picklist_options:
                picklist_options_item = picklist_options_item_data.to_dict()
                picklist_options.append(picklist_options_item)

        required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_order is not UNSET:
            field_dict["display_order"] = display_order
        if displayed is not UNSET:
            field_dict["displayed"] = displayed
        if name is not UNSET:
            field_dict["name"] = name
        if picklist_options is not UNSET:
            field_dict["picklist_options"] = picklist_options
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_fieldupdate_files_body_data_picklist_options_item import (
            CustomFieldupdateFilesBodyDataPicklistOptionsItem,
        )

        d = dict(src_dict)
        display_order = d.pop("display_order", UNSET)

        displayed = d.pop("displayed", UNSET)

        name = d.pop("name", UNSET)

        picklist_options = []
        _picklist_options = d.pop("picklist_options", UNSET)
        for picklist_options_item_data in _picklist_options or []:
            picklist_options_item = (
                CustomFieldupdateFilesBodyDataPicklistOptionsItem.from_dict(
                    picklist_options_item_data
                )
            )

            picklist_options.append(picklist_options_item)

        required = d.pop("required", UNSET)

        custom_fieldupdate_files_body_data = cls(
            display_order=display_order,
            displayed=displayed,
            name=name,
            picklist_options=picklist_options,
            required=required,
        )

        custom_fieldupdate_files_body_data.additional_properties = d
        return custom_fieldupdate_files_body_data

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
