from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactcreate_data_body_data_web_sites_item_name import (
    ContactcreateDataBodyDataWebSitesItemName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactcreateDataBodyDataWebSitesItem")


@_attrs_define
class ContactcreateDataBodyDataWebSitesItem:
    """
    Attributes:
        address (Union[Unset, str]): URL of the WebSite.
        default_web_site (Union[Unset, bool]): Whether or not the Contact should be the default website for the Contact.
        name (Union[Unset, ContactcreateDataBodyDataWebSitesItemName]): Name of the WebSite. Default:
            ContactcreateDataBodyDataWebSitesItemName.OTHER.
    """

    address: Unset | str = UNSET
    default_web_site: Unset | bool = UNSET
    name: Unset | ContactcreateDataBodyDataWebSitesItemName = (
        ContactcreateDataBodyDataWebSitesItemName.OTHER
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        default_web_site = self.default_web_site

        name: Unset | str = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if default_web_site is not UNSET:
            field_dict["default_web_site"] = default_web_site
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        default_web_site = d.pop("default_web_site", UNSET)

        _name = d.pop("name", UNSET)
        name: Unset | ContactcreateDataBodyDataWebSitesItemName
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ContactcreateDataBodyDataWebSitesItemName(_name)

        contactcreate_data_body_data_web_sites_item = cls(
            address=address,
            default_web_site=default_web_site,
            name=name,
        )

        contactcreate_data_body_data_web_sites_item.additional_properties = d
        return contactcreate_data_body_data_web_sites_item

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
