from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reminder_base_state import ReminderBaseState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reminder_notification_method import ReminderNotificationMethod
    from ..models.reminder_subject import ReminderSubject


T = TypeVar("T", bound="Reminder")


@_attrs_define
class Reminder:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *Reminder* was created (as a ISO-8601 timestamp)
        duration (Union[Unset, int]): Time in minutes to remind user before the subject
        etag (Union[Unset, str]): ETag for the *Reminder*
        id (Union[Unset, int]): Unique identifier for the *Reminder*
        next_delivery_at (Union[Unset, str]): The time the *Reminder* will be delivered (as a ISO-8601 timestamp)
        state (Union[Unset, ReminderBaseState]): The current state of the *Reminder*
        updated_at (Union[Unset, str]): The time the *Reminder* was last updated (as a ISO-8601 timestamp)
        notification_method (Union[Unset, ReminderNotificationMethod]):
        subject (Union[Unset, ReminderSubject]):
    """

    created_at: Union[Unset, str] = UNSET
    duration: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    next_delivery_at: Union[Unset, str] = UNSET
    state: Union[Unset, ReminderBaseState] = UNSET
    updated_at: Union[Unset, str] = UNSET
    notification_method: Union[Unset, "ReminderNotificationMethod"] = UNSET
    subject: Union[Unset, "ReminderSubject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        duration = self.duration

        etag = self.etag

        id = self.id

        next_delivery_at = self.next_delivery_at

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        updated_at = self.updated_at

        notification_method: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.notification_method, Unset):
            notification_method = self.notification_method.to_dict()

        subject: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.subject, Unset):
            subject = self.subject.to_dict()

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
        if next_delivery_at is not UNSET:
            field_dict["next_delivery_at"] = next_delivery_at
        if state is not UNSET:
            field_dict["state"] = state
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if notification_method is not UNSET:
            field_dict["notification_method"] = notification_method
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reminder_notification_method import ReminderNotificationMethod
        from ..models.reminder_subject import ReminderSubject

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        duration = d.pop("duration", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        next_delivery_at = d.pop("next_delivery_at", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, ReminderBaseState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ReminderBaseState(_state)

        updated_at = d.pop("updated_at", UNSET)

        _notification_method = d.pop("notification_method", UNSET)
        notification_method: Union[Unset, ReminderNotificationMethod]
        if isinstance(_notification_method, Unset):
            notification_method = UNSET
        else:
            notification_method = ReminderNotificationMethod.from_dict(_notification_method)

        _subject = d.pop("subject", UNSET)
        subject: Union[Unset, ReminderSubject]
        if isinstance(_subject, Unset):
            subject = UNSET
        else:
            subject = ReminderSubject.from_dict(_subject)

        reminder = cls(
            created_at=created_at,
            duration=duration,
            etag=etag,
            id=id,
            next_delivery_at=next_delivery_at,
            state=state,
            updated_at=updated_at,
            notification_method=notification_method,
            subject=subject,
        )

        reminder.additional_properties = d
        return reminder

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
