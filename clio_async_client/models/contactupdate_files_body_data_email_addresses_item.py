from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactupdate_files_body_data_email_addresses_item_name import (
    ContactupdateFilesBodyDataEmailAddressesItemName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactupdateFilesBodyDataEmailAddressesItem")


@_attrs_define
class ContactupdateFilesBodyDataEmailAddressesItem:
    """
    Attributes:
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated EmailAddress is present, the EmailAddress is deleted from the Contact.
        address (Union[Unset, str]): Email address.
        default_email (Union[Unset, bool]): Whether or not the Contact should be the default email for the Contact.
        id (Union[Unset, int]): The unique identifier for a single EmailAddress associated with the Contact. The keyword
            `null` is not valid for this field.
        name (Union[Unset, ContactupdateFilesBodyDataEmailAddressesItemName]): Name of the EmailAddress. Default:
            ContactupdateFilesBodyDataEmailAddressesItemName.OTHER.
    """

    field_destroy: Union[Unset, bool] = UNSET
    address: Union[Unset, str] = UNSET
    default_email: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, ContactupdateFilesBodyDataEmailAddressesItemName] = (
        ContactupdateFilesBodyDataEmailAddressesItemName.OTHER
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_destroy = self.field_destroy

        address = self.address

        default_email = self.default_email

        id = self.id

        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if address is not UNSET:
            field_dict["address"] = address
        if default_email is not UNSET:
            field_dict["default_email"] = default_email
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_destroy = d.pop("_destroy", UNSET)

        address = d.pop("address", UNSET)

        default_email = d.pop("default_email", UNSET)

        id = d.pop("id", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, ContactupdateFilesBodyDataEmailAddressesItemName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ContactupdateFilesBodyDataEmailAddressesItemName(_name)

        contactupdate_files_body_data_email_addresses_item = cls(
            field_destroy=field_destroy,
            address=address,
            default_email=default_email,
            id=id,
            name=name,
        )

        contactupdate_files_body_data_email_addresses_item.additional_properties = d
        return contactupdate_files_body_data_email_addresses_item

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
