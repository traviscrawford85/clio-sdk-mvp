from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactupdate_files_body_data_phone_numbers_item_name import (
    ContactupdateFilesBodyDataPhoneNumbersItemName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactupdateFilesBodyDataPhoneNumbersItem")


@_attrs_define
class ContactupdateFilesBodyDataPhoneNumbersItem:
    """
    Attributes:
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated PhoneNumber is present, the PhoneNumber is deleted from the Contact.
        default_number (Union[Unset, bool]): Whether or not the PhoneNumber should be the default number for the
            Contact.
        id (Union[Unset, int]): The unique identifier for a single PhoneNumber associated with the Contact. The keyword
            `null` is not valid for this field.
        name (Union[Unset, ContactupdateFilesBodyDataPhoneNumbersItemName]): Name of the PhoneNumber. Default:
            ContactupdateFilesBodyDataPhoneNumbersItemName.OTHER.
        number (Union[Unset, str]): Phone number.
    """

    field_destroy: Union[Unset, bool] = UNSET
    default_number: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, ContactupdateFilesBodyDataPhoneNumbersItemName] = (
        ContactupdateFilesBodyDataPhoneNumbersItemName.OTHER
    )
    number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_destroy = self.field_destroy

        default_number = self.default_number

        id = self.id

        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if default_number is not UNSET:
            field_dict["default_number"] = default_number
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_destroy = d.pop("_destroy", UNSET)

        default_number = d.pop("default_number", UNSET)

        id = d.pop("id", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, ContactupdateFilesBodyDataPhoneNumbersItemName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ContactupdateFilesBodyDataPhoneNumbersItemName(_name)

        number = d.pop("number", UNSET)

        contactupdate_files_body_data_phone_numbers_item = cls(
            field_destroy=field_destroy,
            default_number=default_number,
            id=id,
            name=name,
            number=number,
        )

        contactupdate_files_body_data_phone_numbers_item.additional_properties = d
        return contactupdate_files_body_data_phone_numbers_item

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
