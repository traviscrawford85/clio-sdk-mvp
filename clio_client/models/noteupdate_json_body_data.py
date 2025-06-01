from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.noteupdate_json_body_data_notification_event_subscribers_item import (
        NoteupdateJsonBodyDataNotificationEventSubscribersItem,
    )


T = TypeVar("T", bound="NoteupdateJsonBodyData")


@_attrs_define
class NoteupdateJsonBodyData:
    """
    Attributes:
        date (Union[Unset, str]): Date for the Note. (Expects an ISO-8601 date).
        detail (Union[Unset, str]): Note body.
        notification_event_subscribers (Union[Unset, list['NoteupdateJsonBodyDataNotificationEventSubscribersItem']]):
        subject (Union[Unset, str]): Note subject.
    """

    date: Unset | str = UNSET
    detail: Unset | str = UNSET
    notification_event_subscribers: (
        Unset | list["NoteupdateJsonBodyDataNotificationEventSubscribersItem"]
    ) = UNSET
    subject: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        detail = self.detail

        notification_event_subscribers: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.notification_event_subscribers, Unset):
            notification_event_subscribers = []
            for (
                notification_event_subscribers_item_data
            ) in self.notification_event_subscribers:
                notification_event_subscribers_item = (
                    notification_event_subscribers_item_data.to_dict()
                )
                notification_event_subscribers.append(
                    notification_event_subscribers_item
                )

        subject = self.subject

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if detail is not UNSET:
            field_dict["detail"] = detail
        if notification_event_subscribers is not UNSET:
            field_dict["notification_event_subscribers"] = (
                notification_event_subscribers
            )
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.noteupdate_json_body_data_notification_event_subscribers_item import (
            NoteupdateJsonBodyDataNotificationEventSubscribersItem,
        )

        d = dict(src_dict)
        date = d.pop("date", UNSET)

        detail = d.pop("detail", UNSET)

        notification_event_subscribers = []
        _notification_event_subscribers = d.pop("notification_event_subscribers", UNSET)
        for notification_event_subscribers_item_data in (
            _notification_event_subscribers or []
        ):
            notification_event_subscribers_item = (
                NoteupdateJsonBodyDataNotificationEventSubscribersItem.from_dict(
                    notification_event_subscribers_item_data
                )
            )

            notification_event_subscribers.append(notification_event_subscribers_item)

        subject = d.pop("subject", UNSET)

        noteupdate_json_body_data = cls(
            date=date,
            detail=detail,
            notification_event_subscribers=notification_event_subscribers,
            subject=subject,
        )

        noteupdate_json_body_data.additional_properties = d
        return noteupdate_json_body_data

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
