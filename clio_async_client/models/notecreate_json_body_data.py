from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notecreate_json_body_data_type import NotecreateJsonBodyDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notecreate_json_body_data_contact import NotecreateJsonBodyDataContact
    from ..models.notecreate_json_body_data_matter import NotecreateJsonBodyDataMatter
    from ..models.notecreate_json_body_data_notification_event_subscribers_item import (
        NotecreateJsonBodyDataNotificationEventSubscribersItem,
    )


T = TypeVar("T", bound="NotecreateJsonBodyData")


@_attrs_define
class NotecreateJsonBodyData:
    """
    Attributes:
        contact (NotecreateJsonBodyDataContact):
        matter (NotecreateJsonBodyDataMatter):
        type_ (NotecreateJsonBodyDataType): Note type.
        date (Union[Unset, str]): Date for the Note. (Expects an ISO-8601 date).
        detail (Union[Unset, str]): Note body.
        notification_event_subscribers (Union[Unset, list['NotecreateJsonBodyDataNotificationEventSubscribersItem']]):
        subject (Union[Unset, str]): Note subject.
    """

    contact: "NotecreateJsonBodyDataContact"
    matter: "NotecreateJsonBodyDataMatter"
    type_: NotecreateJsonBodyDataType
    date: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    notification_event_subscribers: Union[Unset, list["NotecreateJsonBodyDataNotificationEventSubscribersItem"]] = UNSET
    subject: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact = self.contact.to_dict()

        matter = self.matter.to_dict()

        type_ = self.type_.value

        date = self.date

        detail = self.detail

        notification_event_subscribers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notification_event_subscribers, Unset):
            notification_event_subscribers = []
            for notification_event_subscribers_item_data in self.notification_event_subscribers:
                notification_event_subscribers_item = notification_event_subscribers_item_data.to_dict()
                notification_event_subscribers.append(notification_event_subscribers_item)

        subject = self.subject

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contact": contact,
                "matter": matter,
                "type": type_,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if detail is not UNSET:
            field_dict["detail"] = detail
        if notification_event_subscribers is not UNSET:
            field_dict["notification_event_subscribers"] = notification_event_subscribers
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notecreate_json_body_data_contact import (
            NotecreateJsonBodyDataContact,
        )
        from ..models.notecreate_json_body_data_matter import (
            NotecreateJsonBodyDataMatter,
        )
        from ..models.notecreate_json_body_data_notification_event_subscribers_item import (
            NotecreateJsonBodyDataNotificationEventSubscribersItem,
        )

        d = dict(src_dict)
        contact = NotecreateJsonBodyDataContact.from_dict(d.pop("contact"))

        matter = NotecreateJsonBodyDataMatter.from_dict(d.pop("matter"))

        type_ = NotecreateJsonBodyDataType(d.pop("type"))

        date = d.pop("date", UNSET)

        detail = d.pop("detail", UNSET)

        notification_event_subscribers = []
        _notification_event_subscribers = d.pop("notification_event_subscribers", UNSET)
        for notification_event_subscribers_item_data in _notification_event_subscribers or []:
            notification_event_subscribers_item = NotecreateJsonBodyDataNotificationEventSubscribersItem.from_dict(
                notification_event_subscribers_item_data
            )

            notification_event_subscribers.append(notification_event_subscribers_item)

        subject = d.pop("subject", UNSET)

        notecreate_json_body_data = cls(
            contact=contact,
            matter=matter,
            type_=type_,
            date=date,
            detail=detail,
            notification_event_subscribers=notification_event_subscribers,
            subject=subject,
        )

        notecreate_json_body_data.additional_properties = d
        return notecreate_json_body_data

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
