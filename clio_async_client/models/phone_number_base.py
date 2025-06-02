from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.phone_number_base_name import PhoneNumberBaseName
from ..types import UNSET, Unset

T = TypeVar("T", bound="PhoneNumberBase")


@_attrs_define
class PhoneNumberBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *PhoneNumber* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *PhoneNumber*
        id (Union[Unset, int]): Unique identifier for the *PhoneNumber*
        name (Union[Unset, PhoneNumberBaseName]): The type of *PhoneNumber* it is
        number (Union[Unset, str]): Contact's Phone Number
        primary (Union[Unset, bool]): Whether it is default for this contact
        updated_at (Union[Unset, str]): The time the *PhoneNumber* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, PhoneNumberBaseName] = UNSET
    number: Union[Unset, str] = UNSET
    primary: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        etag = self.etag

        id = self.id

        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        number = self.number

        primary = self.primary

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if primary is not UNSET:
            field_dict["primary"] = primary
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, PhoneNumberBaseName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = PhoneNumberBaseName(_name)

        number = d.pop("number", UNSET)

        primary = d.pop("primary", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        phone_number_base = cls(
            created_at=created_at,
            etag=etag,
            id=id,
            name=name,
            number=number,
            primary=primary,
            updated_at=updated_at,
        )

        phone_number_base.additional_properties = d
        return phone_number_base

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
