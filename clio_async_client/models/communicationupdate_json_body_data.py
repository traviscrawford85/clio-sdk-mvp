from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.communicationupdate_json_body_data_type import (
    CommunicationupdateJsonBodyDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.communicationupdate_json_body_data_external_properties_item import (
        CommunicationupdateJsonBodyDataExternalPropertiesItem,
    )
    from ..models.communicationupdate_json_body_data_matter import (
        CommunicationupdateJsonBodyDataMatter,
    )
    from ..models.communicationupdate_json_body_data_notification_event_subscribers_item import (
        CommunicationupdateJsonBodyDataNotificationEventSubscribersItem,
    )
    from ..models.communicationupdate_json_body_data_receivers_item import (
        CommunicationupdateJsonBodyDataReceiversItem,
    )
    from ..models.communicationupdate_json_body_data_senders_item import (
        CommunicationupdateJsonBodyDataSendersItem,
    )


T = TypeVar("T", bound="CommunicationupdateJsonBodyData")


@_attrs_define
class CommunicationupdateJsonBodyData:
    """
    Attributes:
        body (Union[Unset, str]): The body value.
        date (Union[Unset, str]): The date for the Communication. (Expects an ISO-8601 date.)
        external_properties (Union[Unset, list['CommunicationupdateJsonBodyDataExternalPropertiesItem']]):
        matter (Union[Unset, CommunicationupdateJsonBodyDataMatter]):
        notification_event_subscribers (Union[Unset,
            list['CommunicationupdateJsonBodyDataNotificationEventSubscribersItem']]):
        received_at (Union[Unset, str]): The date-time for the Communication. (Expects an ISO-8601 date-time.)
        receivers (Union[Unset, list['CommunicationupdateJsonBodyDataReceiversItem']]):
        senders (Union[Unset, list['CommunicationupdateJsonBodyDataSendersItem']]):
        subject (Union[Unset, str]): The subject value.
        type_ (Union[Unset, CommunicationupdateJsonBodyDataType]): Type of the Communication.
    """

    body: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    external_properties: Union[Unset, list["CommunicationupdateJsonBodyDataExternalPropertiesItem"]] = UNSET
    matter: Union[Unset, "CommunicationupdateJsonBodyDataMatter"] = UNSET
    notification_event_subscribers: Union[
        Unset, list["CommunicationupdateJsonBodyDataNotificationEventSubscribersItem"]
    ] = UNSET
    received_at: Union[Unset, str] = UNSET
    receivers: Union[Unset, list["CommunicationupdateJsonBodyDataReceiversItem"]] = UNSET
    senders: Union[Unset, list["CommunicationupdateJsonBodyDataSendersItem"]] = UNSET
    subject: Union[Unset, str] = UNSET
    type_: Union[Unset, CommunicationupdateJsonBodyDataType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        date = self.date

        external_properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.external_properties, Unset):
            external_properties = []
            for external_properties_item_data in self.external_properties:
                external_properties_item = external_properties_item_data.to_dict()
                external_properties.append(external_properties_item)

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        notification_event_subscribers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notification_event_subscribers, Unset):
            notification_event_subscribers = []
            for notification_event_subscribers_item_data in self.notification_event_subscribers:
                notification_event_subscribers_item = notification_event_subscribers_item_data.to_dict()
                notification_event_subscribers.append(notification_event_subscribers_item)

        received_at = self.received_at

        receivers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.receivers, Unset):
            receivers = []
            for receivers_item_data in self.receivers:
                receivers_item = receivers_item_data.to_dict()
                receivers.append(receivers_item)

        senders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.senders, Unset):
            senders = []
            for senders_item_data in self.senders:
                senders_item = senders_item_data.to_dict()
                senders.append(senders_item)

        subject = self.subject

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if date is not UNSET:
            field_dict["date"] = date
        if external_properties is not UNSET:
            field_dict["external_properties"] = external_properties
        if matter is not UNSET:
            field_dict["matter"] = matter
        if notification_event_subscribers is not UNSET:
            field_dict["notification_event_subscribers"] = notification_event_subscribers
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if receivers is not UNSET:
            field_dict["receivers"] = receivers
        if senders is not UNSET:
            field_dict["senders"] = senders
        if subject is not UNSET:
            field_dict["subject"] = subject
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communicationupdate_json_body_data_external_properties_item import (
            CommunicationupdateJsonBodyDataExternalPropertiesItem,
        )
        from ..models.communicationupdate_json_body_data_matter import (
            CommunicationupdateJsonBodyDataMatter,
        )
        from ..models.communicationupdate_json_body_data_notification_event_subscribers_item import (
            CommunicationupdateJsonBodyDataNotificationEventSubscribersItem,
        )
        from ..models.communicationupdate_json_body_data_receivers_item import (
            CommunicationupdateJsonBodyDataReceiversItem,
        )
        from ..models.communicationupdate_json_body_data_senders_item import (
            CommunicationupdateJsonBodyDataSendersItem,
        )

        d = dict(src_dict)
        body = d.pop("body", UNSET)

        date = d.pop("date", UNSET)

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = CommunicationupdateJsonBodyDataExternalPropertiesItem.from_dict(
                external_properties_item_data
            )

            external_properties.append(external_properties_item)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, CommunicationupdateJsonBodyDataMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = CommunicationupdateJsonBodyDataMatter.from_dict(_matter)

        notification_event_subscribers = []
        _notification_event_subscribers = d.pop("notification_event_subscribers", UNSET)
        for notification_event_subscribers_item_data in _notification_event_subscribers or []:
            notification_event_subscribers_item = (
                CommunicationupdateJsonBodyDataNotificationEventSubscribersItem.from_dict(
                    notification_event_subscribers_item_data
                )
            )

            notification_event_subscribers.append(notification_event_subscribers_item)

        received_at = d.pop("received_at", UNSET)

        receivers = []
        _receivers = d.pop("receivers", UNSET)
        for receivers_item_data in _receivers or []:
            receivers_item = CommunicationupdateJsonBodyDataReceiversItem.from_dict(receivers_item_data)

            receivers.append(receivers_item)

        senders = []
        _senders = d.pop("senders", UNSET)
        for senders_item_data in _senders or []:
            senders_item = CommunicationupdateJsonBodyDataSendersItem.from_dict(senders_item_data)

            senders.append(senders_item)

        subject = d.pop("subject", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CommunicationupdateJsonBodyDataType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CommunicationupdateJsonBodyDataType(_type_)

        communicationupdate_json_body_data = cls(
            body=body,
            date=date,
            external_properties=external_properties,
            matter=matter,
            notification_event_subscribers=notification_event_subscribers,
            received_at=received_at,
            receivers=receivers,
            senders=senders,
            subject=subject,
            type_=type_,
        )

        communicationupdate_json_body_data.additional_properties = d
        return communicationupdate_json_body_data

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
