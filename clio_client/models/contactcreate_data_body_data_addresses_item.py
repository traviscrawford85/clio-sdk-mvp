from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contactcreate_data_body_data_addresses_item_name import (
    ContactcreateDataBodyDataAddressesItemName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactcreateDataBodyDataAddressesItem")


@_attrs_define
class ContactcreateDataBodyDataAddressesItem:
    """
    Attributes:
        city (Union[Unset, str]): City.
        country (Union[Unset, str]): Country
        name (Union[Unset, ContactcreateDataBodyDataAddressesItemName]): Name of the Address. Default:
            ContactcreateDataBodyDataAddressesItemName.OTHER.
        postal_code (Union[Unset, str]): Postal code or zip code.
        province (Union[Unset, str]): Province or state.
        street (Union[Unset, str]): Street.
    """

    city: Unset | str = UNSET
    country: Unset | str = UNSET
    name: Unset | ContactcreateDataBodyDataAddressesItemName = (
        ContactcreateDataBodyDataAddressesItemName.OTHER
    )
    postal_code: Unset | str = UNSET
    province: Unset | str = UNSET
    street: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        country = self.country

        name: Unset | str = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        postal_code = self.postal_code

        province = self.province

        street = self.street

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if name is not UNSET:
            field_dict["name"] = name
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if province is not UNSET:
            field_dict["province"] = province
        if street is not UNSET:
            field_dict["street"] = street

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        _name = d.pop("name", UNSET)
        name: Unset | ContactcreateDataBodyDataAddressesItemName
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ContactcreateDataBodyDataAddressesItemName(_name)

        postal_code = d.pop("postal_code", UNSET)

        province = d.pop("province", UNSET)

        street = d.pop("street", UNSET)

        contactcreate_data_body_data_addresses_item = cls(
            city=city,
            country=country,
            name=name,
            postal_code=postal_code,
            province=province,
            street=street,
        )

        contactcreate_data_body_data_addresses_item.additional_properties = d
        return contactcreate_data_body_data_addresses_item

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
