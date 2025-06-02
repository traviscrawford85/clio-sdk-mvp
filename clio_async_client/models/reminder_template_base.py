from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reminder_template_base_notification_type import (
    ReminderTemplateBaseNotificationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReminderTemplateBase")


@_attrs_define
class ReminderTemplateBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *ReminderTemplate* was created (as a ISO-8601 timestamp)
        duration (Union[Unset, int]): The time in minutes to remind user before the subject.
        etag (Union[Unset, str]): ETag for the *ReminderTemplate*
        id (Union[Unset, int]): Unique identifier for the *ReminderTemplate*
        notification_type (Union[Unset, ReminderTemplateBaseNotificationType]): The type of method to be notified by
        updated_at (Union[Unset, str]): The time the *ReminderTemplate* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Union[Unset, str] = UNSET
    duration: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    notification_type: Union[Unset, ReminderTemplateBaseNotificationType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        duration = self.duration

        etag = self.etag

        id = self.id

        notification_type: Union[Unset, str] = UNSET
        if not isinstance(self.notification_type, Unset):
            notification_type = self.notification_type.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if duration is not UNSET:
            field_dict["duration"] = duration
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if notification_type is not UNSET:
            field_dict["notification_type"] = notification_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        duration = d.pop("duration", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        _notification_type = d.pop("notification_type", UNSET)
        notification_type: Union[Unset, ReminderTemplateBaseNotificationType]
        if isinstance(_notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = ReminderTemplateBaseNotificationType(_notification_type)

        updated_at = d.pop("updated_at", UNSET)

        reminder_template_base = cls(
            created_at=created_at,
            duration=duration,
            etag=etag,
            id=id,
            notification_type=notification_type,
            updated_at=updated_at,
        )

        reminder_template_base.additional_properties = d
        return reminder_template_base

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
