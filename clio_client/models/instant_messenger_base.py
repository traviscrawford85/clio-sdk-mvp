from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.instant_messenger_base_name import InstantMessengerBaseName
from ..types import UNSET, Unset

T = TypeVar("T", bound="InstantMessengerBase")


@_attrs_define
class InstantMessengerBase:
    """
    Attributes:
        address (Union[Unset, str]): The address of the *InstantMessenger*
        created_at (Union[Unset, str]): The time the *InstantMessenger* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *InstantMessenger*
        id (Union[Unset, int]): Unique identifier for the *InstantMessenger*
        name (Union[Unset, InstantMessengerBaseName]): The type of *InstantMessenger* it is
        updated_at (Union[Unset, str]): The time the *InstantMessenger* was last updated (as a ISO-8601 timestamp)
    """

    address: Unset | str = UNSET
    created_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    name: Unset | InstantMessengerBaseName = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        created_at = self.created_at

        etag = self.etag

        id = self.id

        name: Unset | str = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        _name = d.pop("name", UNSET)
        name: Unset | InstantMessengerBaseName
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = InstantMessengerBaseName(_name)

        updated_at = d.pop("updated_at", UNSET)

        instant_messenger_base = cls(
            address=address,
            created_at=created_at,
            etag=etag,
            id=id,
            name=name,
            updated_at=updated_at,
        )

        instant_messenger_base.additional_properties = d
        return instant_messenger_base

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
