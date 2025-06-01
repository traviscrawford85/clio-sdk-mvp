from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactupdate_data_body_data_web_sites_item_name import (
    ContactupdateDataBodyDataWebSitesItemName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactupdateDataBodyDataWebSitesItem")


@_attrs_define
class ContactupdateDataBodyDataWebSitesItem:
    """
    Attributes:
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated WebSite is present, the WebSite is deleted from the Contact.
        address (Union[Unset, str]): URL of the WebSite.
        default_web_site (Union[Unset, bool]): Whether or not the Contact should be the default website for the Contact.
        id (Union[Unset, int]): The unique identifier for a single WebSite associated with the Contact. The keyword
            `null` is not valid for this field.
        name (Union[Unset, ContactupdateDataBodyDataWebSitesItemName]): Name of the WebSite. Default:
            ContactupdateDataBodyDataWebSitesItemName.OTHER.
    """

    field_destroy: Unset | bool = UNSET
    address: Unset | str = UNSET
    default_web_site: Unset | bool = UNSET
    id: Unset | int = UNSET
    name: Unset | ContactupdateDataBodyDataWebSitesItemName = (
        ContactupdateDataBodyDataWebSitesItemName.OTHER
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_destroy = self.field_destroy

        address = self.address

        default_web_site = self.default_web_site

        id = self.id

        name: Unset | str = UNSET
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
        name: Unset | ContactupdateDataBodyDataWebSitesItemName
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ContactupdateDataBodyDataWebSitesItemName(_name)

        contactupdate_data_body_data_web_sites_item = cls(
            field_destroy=field_destroy,
            address=address,
            default_web_site=default_web_site,
            id=id,
            name=name,
        )

        contactupdate_data_body_data_web_sites_item.additional_properties = d
        return contactupdate_data_body_data_web_sites_item

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
