from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UtbmsSet")


@_attrs_define
class UtbmsSet:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *UtbmsSet* was created (as a ISO-8601 timestamp)
        enabled (Union[Unset, bool]): Whether the *UtbmsSet* is enabled for the current account.
        etag (Union[Unset, str]): ETag for the *UtbmsSet*
        id (Union[Unset, int]): Unique identifier for the *UtbmsSet*
        name (Union[Unset, str]): The name of the *UtbmsSet*
        updated_at (Union[Unset, str]): The time the *UtbmsSet* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Unset | str = UNSET
    enabled: Unset | bool = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    name: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        enabled = self.enabled

        etag = self.etag

        id = self.id

        name = self.name

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
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
        created_at = d.pop("created_at", UNSET)

        enabled = d.pop("enabled", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        utbms_set = cls(
            created_at=created_at,
            enabled=enabled,
            etag=etag,
            id=id,
            name=name,
            updated_at=updated_at,
        )

        utbms_set.additional_properties = d
        return utbms_set

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
