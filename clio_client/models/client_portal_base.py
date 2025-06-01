from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientPortalBase")


@_attrs_define
class ClientPortalBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *ClientPortal* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *ClientPortal*
        id (Union[Unset, int]): Unique identifier for the *ClientPortal*
        unread_count (Union[Unset, int]): The number of unread count messages for the current user.
        unread_notifiable_count (Union[Unset, int]): The number of unread messages for the current user once their
            notification settings have been applied.
        updated_at (Union[Unset, str]): The time the *ClientPortal* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    unread_count: Unset | int = UNSET
    unread_notifiable_count: Unset | int = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        etag = self.etag

        id = self.id

        unread_count = self.unread_count

        unread_notifiable_count = self.unread_notifiable_count

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
        if unread_count is not UNSET:
            field_dict["unread_count"] = unread_count
        if unread_notifiable_count is not UNSET:
            field_dict["unread_notifiable_count"] = unread_notifiable_count
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        unread_count = d.pop("unread_count", UNSET)

        unread_notifiable_count = d.pop("unread_notifiable_count", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        client_portal_base = cls(
            created_at=created_at,
            etag=etag,
            id=id,
            unread_count=unread_count,
            unread_notifiable_count=unread_notifiable_count,
            updated_at=updated_at,
        )

        client_portal_base.additional_properties = d
        return client_portal_base

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
