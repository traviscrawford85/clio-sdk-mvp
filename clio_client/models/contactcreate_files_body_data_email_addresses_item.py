from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactcreate_files_body_data_email_addresses_item_name import (
    ContactcreateFilesBodyDataEmailAddressesItemName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactcreateFilesBodyDataEmailAddressesItem")


@_attrs_define
class ContactcreateFilesBodyDataEmailAddressesItem:
    """
    Attributes:
        address (Union[Unset, str]): Email address.
        default_email (Union[Unset, bool]): Whether or not the Contact should be the default email for the Contact.
        name (Union[Unset, ContactcreateFilesBodyDataEmailAddressesItemName]): Name of the EmailAddress. Default:
            ContactcreateFilesBodyDataEmailAddressesItemName.OTHER.
    """

    address: Unset | str = UNSET
    default_email: Unset | bool = UNSET
    name: Unset | ContactcreateFilesBodyDataEmailAddressesItemName = (
        ContactcreateFilesBodyDataEmailAddressesItemName.OTHER
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        default_email = self.default_email

        name: Unset | str = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if default_email is not UNSET:
            field_dict["default_email"] = default_email
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        default_email = d.pop("default_email", UNSET)

        _name = d.pop("name", UNSET)
        name: Unset | ContactcreateFilesBodyDataEmailAddressesItemName
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ContactcreateFilesBodyDataEmailAddressesItemName(_name)

        contactcreate_files_body_data_email_addresses_item = cls(
            address=address,
            default_email=default_email,
            name=name,
        )

        contactcreate_files_body_data_email_addresses_item.additional_properties = d
        return contactcreate_files_body_data_email_addresses_item

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
