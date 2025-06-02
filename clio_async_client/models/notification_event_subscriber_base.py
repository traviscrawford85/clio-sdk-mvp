from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationEventSubscriberBase")


@_attrs_define
class NotificationEventSubscriberBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *NotificationEventSubscriber* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *NotificationEventSubscriber*
        id (Union[Unset, int]): Unique identifier for the *NotificationEventSubscriber*
        name (Union[Unset, str]): The User name added as a notification event subscriber to the
            NotificationEventSubscriber
        updated_at (Union[Unset, str]): The time the *NotificationEventSubscriber* was last updated (as a ISO-8601
            timestamp)
        user_id (Union[Unset, int]): The unique identifier for a User added as a notification event subscriber to the
            NotificationEventSubscriber
    """

    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        etag = self.etag

        id = self.id

        name = self.name

        updated_at = self.updated_at

        user_id = self.user_id

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
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        user_id = d.pop("user_id", UNSET)

        notification_event_subscriber_base = cls(
            created_at=created_at,
            etag=etag,
            id=id,
            name=name,
            updated_at=updated_at,
            user_id=user_id,
        )

        notification_event_subscriber_base.additional_properties = d
        return notification_event_subscriber_base

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
