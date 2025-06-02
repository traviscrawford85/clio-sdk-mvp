from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_message_conversation import (
        ConversationMessageConversation,
    )
    from ..models.conversation_message_document import ConversationMessageDocument
    from ..models.conversation_message_sender import ConversationMessageSender
    from ..models.unredacted_participant_base import UnredactedParticipantBase


T = TypeVar("T", bound="ConversationMessage")


@_attrs_define
class ConversationMessage:
    """
    Attributes:
        body (Union[Unset, str]): The main content of the *ConversationMessage*
        created_at (Union[Unset, str]): The time the *ConversationMessage* was created (as a ISO-8601 timestamp)
        date (Union[Unset, str]): The creation date of the message in the current user's time zone
        etag (Union[Unset, str]): ETag for the *ConversationMessage*
        id (Union[Unset, int]): Unique identifier for the *ConversationMessage*
        updated_at (Union[Unset, str]): The time the *ConversationMessage* was last updated (as a ISO-8601 timestamp)
        conversation (Union[Unset, ConversationMessageConversation]):
        document (Union[Unset, ConversationMessageDocument]):
        receivers (Union[Unset, list['UnredactedParticipantBase']]): UnredactedParticipant
        sender (Union[Unset, ConversationMessageSender]):
    """

    body: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    conversation: Union[Unset, "ConversationMessageConversation"] = UNSET
    document: Union[Unset, "ConversationMessageDocument"] = UNSET
    receivers: Union[Unset, list["UnredactedParticipantBase"]] = UNSET
    sender: Union[Unset, "ConversationMessageSender"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        created_at = self.created_at

        date = self.date

        etag = self.etag

        id = self.id

        updated_at = self.updated_at

        conversation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.conversation, Unset):
            conversation = self.conversation.to_dict()

        document: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        receivers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.receivers, Unset):
            receivers = []
            for receivers_item_data in self.receivers:
                receivers_item = receivers_item_data.to_dict()
                receivers.append(receivers_item)

        sender: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

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
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if conversation is not UNSET:
            field_dict["conversation"] = conversation
        if document is not UNSET:
            field_dict["document"] = document
        if receivers is not UNSET:
            field_dict["receivers"] = receivers
        if sender is not UNSET:
            field_dict["sender"] = sender

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_message_conversation import (
            ConversationMessageConversation,
        )
        from ..models.conversation_message_document import ConversationMessageDocument
        from ..models.conversation_message_sender import ConversationMessageSender
        from ..models.unredacted_participant_base import UnredactedParticipantBase

        d = dict(src_dict)
        body = d.pop("body", UNSET)

        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _conversation = d.pop("conversation", UNSET)
        conversation: Union[Unset, ConversationMessageConversation]
        if isinstance(_conversation, Unset):
            conversation = UNSET
        else:
            conversation = ConversationMessageConversation.from_dict(_conversation)

        _document = d.pop("document", UNSET)
        document: Union[Unset, ConversationMessageDocument]
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = ConversationMessageDocument.from_dict(_document)

        receivers = []
        _receivers = d.pop("receivers", UNSET)
        for receivers_item_data in _receivers or []:
            receivers_item = UnredactedParticipantBase.from_dict(receivers_item_data)

            receivers.append(receivers_item)

        _sender = d.pop("sender", UNSET)
        sender: Union[Unset, ConversationMessageSender]
        if isinstance(_sender, Unset):
            sender = UNSET
        else:
            sender = ConversationMessageSender.from_dict(_sender)

        conversation_message = cls(
            body=body,
            created_at=created_at,
            date=date,
            etag=etag,
            id=id,
            updated_at=updated_at,
            conversation=conversation,
            document=document,
            receivers=receivers,
            sender=sender,
        )

        conversation_message.additional_properties = d
        return conversation_message

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
