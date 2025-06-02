from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.address_base_name import AddressBaseName
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddressBase")


@_attrs_define
class AddressBase:
    """
    Attributes:
        city (Union[Unset, str]): City of the *Address*
        country (Union[Unset, str]): Country of the *Address*
        created_at (Union[Unset, str]): The time the *Address* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *Address*
        id (Union[Unset, int]): Unique identifier for the *Address*
        name (Union[Unset, AddressBaseName]): The name of the *Address*
        postal_code (Union[Unset, str]): Postal code of the *Address*
        primary (Union[Unset, bool]): Whether it is the default for this contact
        province (Union[Unset, str]): Province or state of the *Address*
        street (Union[Unset, str]): Street of the *Address*
        updated_at (Union[Unset, str]): The time the *Address* was last updated (as a ISO-8601 timestamp)
    """

    city: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, AddressBaseName] = UNSET
    postal_code: Union[Unset, str] = UNSET
    primary: Union[Unset, bool] = UNSET
    province: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        country = self.country

        created_at = self.created_at

        etag = self.etag

        id = self.id

        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        postal_code = self.postal_code

        primary = self.primary

        province = self.province

        street = self.street

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if primary is not UNSET:
            field_dict["primary"] = primary
        if province is not UNSET:
            field_dict["province"] = province
        if street is not UNSET:
            field_dict["street"] = street
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, AddressBaseName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = AddressBaseName(_name)

        postal_code = d.pop("postal_code", UNSET)

        primary = d.pop("primary", UNSET)

        province = d.pop("province", UNSET)

        street = d.pop("street", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        address_base = cls(
            city=city,
            country=country,
            created_at=created_at,
            etag=etag,
            id=id,
            name=name,
            postal_code=postal_code,
            primary=primary,
            province=province,
            street=street,
            updated_at=updated_at,
        )

        address_base.additional_properties = d
        return address_base

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
