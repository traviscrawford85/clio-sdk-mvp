from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactupdate_files_body_data_web_sites_item_name import (
    ContactupdateFilesBodyDataWebSitesItemName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactupdateFilesBodyDataWebSitesItem")


@_attrs_define
class ContactupdateFilesBodyDataWebSitesItem:
    """
    Attributes:
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated WebSite is present, the WebSite is deleted from the Contact.
        address (Union[Unset, str]): URL of the WebSite.
        default_web_site (Union[Unset, bool]): Whether or not the Contact should be the default website for the Contact.
        id (Union[Unset, int]): The unique identifier for a single WebSite associated with the Contact. The keyword
            `null` is not valid for this field.
        name (Union[Unset, ContactupdateFilesBodyDataWebSitesItemName]): Name of the WebSite. Default:
            ContactupdateFilesBodyDataWebSitesItemName.OTHER.
    """

    field_destroy: Union[Unset, bool] = UNSET
    address: Union[Unset, str] = UNSET
    default_web_site: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, ContactupdateFilesBodyDataWebSitesItemName] = ContactupdateFilesBodyDataWebSitesItemName.OTHER
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_destroy = self.field_destroy

        address = self.address

        default_web_site = self.default_web_site

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
        if default_web_site is not UNSET:
            field_dict["default_web_site"] = default_web_site
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

        default_web_site = d.pop("default_web_site", UNSET)

        id = d.pop("id", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, ContactupdateFilesBodyDataWebSitesItemName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ContactupdateFilesBodyDataWebSitesItemName(_name)

        contactupdate_files_body_data_web_sites_item = cls(
            field_destroy=field_destroy,
            address=address,
            default_web_site=default_web_site,
            id=id,
            name=name,
        )

        contactupdate_files_body_data_web_sites_item.additional_properties = d
        return contactupdate_files_body_data_web_sites_item

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
