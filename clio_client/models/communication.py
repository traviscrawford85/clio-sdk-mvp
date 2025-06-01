from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.communication_base_type import CommunicationBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_base import ActivityBase
    from ..models.communication_communication_eml_file import (
        CommunicationCommunicationEmlFile,
    )
    from ..models.communication_matter import CommunicationMatter
    from ..models.communication_user import CommunicationUser
    from ..models.document_base import DocumentBase
    from ..models.external_property_base import ExternalPropertyBase
    from ..models.notification_event_subscriber_base import (
        NotificationEventSubscriberBase,
    )
    from ..models.participant import Participant


T = TypeVar("T", bound="Communication")


@_attrs_define
class Communication:
    """
    Attributes:
        body (Union[Unset, str]): The main content of the *Communication*
        created_at (Union[Unset, str]): The time the *Communication* was created (as a ISO-8601 timestamp)
        date (Union[Unset, str]): The date of the *Communication* (as a ISO-8601 datestamp)
        etag (Union[Unset, str]): ETag for the *Communication*
        id (Union[Unset, int]): Unique identifier for the *Communication*
        received_at (Union[Unset, str]): The date-time of the *Communication* (in ISO-8601 format)
        subject (Union[Unset, str]): The subject line of the *Communication*
        time_entries_count (Union[Unset, int]): The number of time_entries associated with the *Communication*
        type_ (Union[Unset, CommunicationBaseType]): The type of the *Communication*
        updated_at (Union[Unset, str]): The time the *Communication* was last updated (as a ISO-8601 timestamp)
        communication_eml_file (Union[Unset, CommunicationCommunicationEmlFile]):
        documents (Union[Unset, list['DocumentBase']]): Document
        external_properties (Union[Unset, list['ExternalPropertyBase']]): ExternalProperty
        matter (Union[Unset, CommunicationMatter]):
        notification_event_subscribers (Union[Unset, list['NotificationEventSubscriberBase']]):
            NotificationEventSubscriber
        receivers (Union[Unset, list['Participant']]): Participant
        senders (Union[Unset, list['Participant']]): Participant
        time_entries (Union[Unset, list['ActivityBase']]): Activity
        user (Union[Unset, CommunicationUser]):
    """

    body: Unset | str = UNSET
    created_at: Unset | str = UNSET
    date: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    received_at: Unset | str = UNSET
    subject: Unset | str = UNSET
    time_entries_count: Unset | int = UNSET
    type_: Unset | CommunicationBaseType = UNSET
    updated_at: Unset | str = UNSET
    communication_eml_file: Union[Unset, "CommunicationCommunicationEmlFile"] = UNSET
    documents: Unset | list["DocumentBase"] = UNSET
    external_properties: Unset | list["ExternalPropertyBase"] = UNSET
    matter: Union[Unset, "CommunicationMatter"] = UNSET
    notification_event_subscribers: Unset | list["NotificationEventSubscriberBase"] = (
        UNSET
    )
    receivers: Unset | list["Participant"] = UNSET
    senders: Unset | list["Participant"] = UNSET
    time_entries: Unset | list["ActivityBase"] = UNSET
    user: Union[Unset, "CommunicationUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        created_at = self.created_at

        date = self.date

        etag = self.etag

        id = self.id

        received_at = self.received_at

        subject = self.subject

        time_entries_count = self.time_entries_count

        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        communication_eml_file: Unset | dict[str, Any] = UNSET
        if not isinstance(self.communication_eml_file, Unset):
            communication_eml_file = self.communication_eml_file.to_dict()

        documents: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        external_properties: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.external_properties, Unset):
            external_properties = []
            for external_properties_item_data in self.external_properties:
                external_properties_item = external_properties_item_data.to_dict()
                external_properties.append(external_properties_item)

        matter: Unset | dict[str, Any] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

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

        receivers: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.receivers, Unset):
            receivers = []
            for receivers_item_data in self.receivers:
                receivers_item = receivers_item_data.to_dict()
                receivers.append(receivers_item)

        senders: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.senders, Unset):
            senders = []
            for senders_item_data in self.senders:
                senders_item = senders_item_data.to_dict()
                senders.append(senders_item)

        time_entries: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.time_entries, Unset):
            time_entries = []
            for time_entries_item_data in self.time_entries:
                time_entries_item = time_entries_item_data.to_dict()
                time_entries.append(time_entries_item)

        user: Unset | dict[str, Any] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if date is not UNSET:
            field_dict["date"] = date
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if subject is not UNSET:
            field_dict["subject"] = subject
        if time_entries_count is not UNSET:
            field_dict["time_entries_count"] = time_entries_count
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if communication_eml_file is not UNSET:
            field_dict["communication_eml_file"] = communication_eml_file
        if documents is not UNSET:
            field_dict["documents"] = documents
        if external_properties is not UNSET:
            field_dict["external_properties"] = external_properties
        if matter is not UNSET:
            field_dict["matter"] = matter
        if notification_event_subscribers is not UNSET:
            field_dict["notification_event_subscribers"] = (
                notification_event_subscribers
            )
        if receivers is not UNSET:
            field_dict["receivers"] = receivers
        if senders is not UNSET:
            field_dict["senders"] = senders
        if time_entries is not UNSET:
            field_dict["time_entries"] = time_entries
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_base import ActivityBase
        from ..models.communication_communication_eml_file import (
            CommunicationCommunicationEmlFile,
        )
        from ..models.communication_matter import CommunicationMatter
        from ..models.communication_user import CommunicationUser
        from ..models.document_base import DocumentBase
        from ..models.external_property_base import ExternalPropertyBase
        from ..models.notification_event_subscriber_base import (
            NotificationEventSubscriberBase,
        )
        from ..models.participant import Participant

        d = dict(src_dict)
        body = d.pop("body", UNSET)

        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        received_at = d.pop("received_at", UNSET)

        subject = d.pop("subject", UNSET)

        time_entries_count = d.pop("time_entries_count", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Unset | CommunicationBaseType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CommunicationBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        _communication_eml_file = d.pop("communication_eml_file", UNSET)
        communication_eml_file: Unset | CommunicationCommunicationEmlFile
        if isinstance(_communication_eml_file, Unset):
            communication_eml_file = UNSET
        else:
            communication_eml_file = CommunicationCommunicationEmlFile.from_dict(
                _communication_eml_file
            )

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = DocumentBase.from_dict(documents_item_data)

            documents.append(documents_item)

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = ExternalPropertyBase.from_dict(
                external_properties_item_data
            )

            external_properties.append(external_properties_item)

        _matter = d.pop("matter", UNSET)
        matter: Unset | CommunicationMatter
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = CommunicationMatter.from_dict(_matter)

        notification_event_subscribers = []
        _notification_event_subscribers = d.pop("notification_event_subscribers", UNSET)
        for notification_event_subscribers_item_data in (
            _notification_event_subscribers or []
        ):
            notification_event_subscribers_item = (
                NotificationEventSubscriberBase.from_dict(
                    notification_event_subscribers_item_data
                )
            )

            notification_event_subscribers.append(notification_event_subscribers_item)

        receivers = []
        _receivers = d.pop("receivers", UNSET)
        for receivers_item_data in _receivers or []:
            receivers_item = Participant.from_dict(receivers_item_data)

            receivers.append(receivers_item)

        senders = []
        _senders = d.pop("senders", UNSET)
        for senders_item_data in _senders or []:
            senders_item = Participant.from_dict(senders_item_data)

            senders.append(senders_item)

        time_entries = []
        _time_entries = d.pop("time_entries", UNSET)
        for time_entries_item_data in _time_entries or []:
            time_entries_item = ActivityBase.from_dict(time_entries_item_data)

            time_entries.append(time_entries_item)

        _user = d.pop("user", UNSET)
        user: Unset | CommunicationUser
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = CommunicationUser.from_dict(_user)

        communication = cls(
            body=body,
            created_at=created_at,
            date=date,
            etag=etag,
            id=id,
            received_at=received_at,
            subject=subject,
            time_entries_count=time_entries_count,
            type_=type_,
            updated_at=updated_at,
            communication_eml_file=communication_eml_file,
            documents=documents,
            external_properties=external_properties,
            matter=matter,
            notification_event_subscribers=notification_event_subscribers,
            receivers=receivers,
            senders=senders,
            time_entries=time_entries,
            user=user,
        )

        communication.additional_properties = d
        return communication

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
