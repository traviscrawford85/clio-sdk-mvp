from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contactupdate_files_body_data_custom_field_values_item_custom_field import (
        ContactupdateFilesBodyDataCustomFieldValuesItemCustomField,
    )


T = TypeVar("T", bound="ContactupdateFilesBodyDataCustomFieldValuesItem")


@_attrs_define
class ContactupdateFilesBodyDataCustomFieldValuesItem:
    """
    Attributes:
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated CustomFieldValue is present, the CustomFieldValue is deleted from the Contact.
        custom_field (Union[Unset, ContactupdateFilesBodyDataCustomFieldValuesItemCustomField]):
        id (Union[Unset, int]): The unique identifier for a single CustomFieldValue associated with the Contact. The
            keyword `null` is not valid for this field.
        value (Union[Unset, str]): The value of the CustomFieldValue.
    """

    field_destroy: Unset | bool = UNSET
    custom_field: Union[
        Unset, "ContactupdateFilesBodyDataCustomFieldValuesItemCustomField"
    ] = UNSET
    id: Unset | int = UNSET
    value: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_destroy = self.field_destroy

        custom_field: Unset | dict[str, Any] = UNSET
        if not isinstance(self.custom_field, Unset):
            custom_field = self.custom_field.to_dict()

        id = self.id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if custom_field is not UNSET:
            field_dict["custom_field"] = custom_field
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contactupdate_files_body_data_custom_field_values_item_custom_field import (
            ContactupdateFilesBodyDataCustomFieldValuesItemCustomField,
        )

        d = dict(src_dict)
        field_destroy = d.pop("_destroy", UNSET)

        _custom_field = d.pop("custom_field", UNSET)
        custom_field: Unset | ContactupdateFilesBodyDataCustomFieldValuesItemCustomField
        if isinstance(_custom_field, Unset):
            custom_field = UNSET
        else:
            custom_field = (
                ContactupdateFilesBodyDataCustomFieldValuesItemCustomField.from_dict(
                    _custom_field
                )
            )

        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        contactupdate_files_body_data_custom_field_values_item = cls(
            field_destroy=field_destroy,
            custom_field=custom_field,
            id=id,
            value=value,
        )

        contactupdate_files_body_data_custom_field_values_item.additional_properties = d
        return contactupdate_files_body_data_custom_field_values_item

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
