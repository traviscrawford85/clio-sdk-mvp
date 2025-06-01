from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_first_message import ConversationFirstMessage
    from ..models.conversation_last_message import ConversationLastMessage
    from ..models.conversation_matter import ConversationMatter
    from ..models.conversation_membership import ConversationMembership
    from ..models.conversation_message_base import ConversationMessageBase
    from ..models.document_base import DocumentBase


T = TypeVar("T", bound="Conversation")


@_attrs_define
class Conversation:
    """
    Attributes:
        archived (Union[Unset, bool]): Whether the conversation has been archived
        created_at (Union[Unset, str]): The time the *Conversation* was created (as a ISO-8601 timestamp)
        current_user_is_member (Union[Unset, bool]): Whether the current user is a member of this conversation
        etag (Union[Unset, str]): ETag for the *Conversation*
        id (Union[Unset, int]): Unique identifier for the *Conversation*
        message_count (Union[Unset, int]): The number of messages in this conversation
        read (Union[Unset, bool]): Whether any messages in this conversation have been viewed
        read_only (Union[Unset, bool]): Whether the conversation is read only
        subject (Union[Unset, str]): The subject of the *Conversation*
        time_entries_count (Union[Unset, int]): The number of time entries applied to this conversation
        updated_at (Union[Unset, str]): The time the *Conversation* was last updated (as a ISO-8601 timestamp)
        documents (Union[Unset, list['DocumentBase']]): Document
        first_message (Union[Unset, ConversationFirstMessage]):
        last_message (Union[Unset, ConversationLastMessage]):
        matter (Union[Unset, ConversationMatter]):
        memberships (Union[Unset, list['ConversationMembership']]): ConversationMembership
        messages (Union[Unset, list['ConversationMessageBase']]): ConversationMessage
    """

    archived: Unset | bool = UNSET
    created_at: Unset | str = UNSET
    current_user_is_member: Unset | bool = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    message_count: Unset | int = UNSET
    read: Unset | bool = UNSET
    read_only: Unset | bool = UNSET
    subject: Unset | str = UNSET
    time_entries_count: Unset | int = UNSET
    updated_at: Unset | str = UNSET
    documents: Unset | list["DocumentBase"] = UNSET
    first_message: Union[Unset, "ConversationFirstMessage"] = UNSET
    last_message: Union[Unset, "ConversationLastMessage"] = UNSET
    matter: Union[Unset, "ConversationMatter"] = UNSET
    memberships: Unset | list["ConversationMembership"] = UNSET
    messages: Unset | list["ConversationMessageBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archived = self.archived

        created_at = self.created_at

        current_user_is_member = self.current_user_is_member

        etag = self.etag

        id = self.id

        message_count = self.message_count

        read = self.read

        read_only = self.read_only

        subject = self.subject

        time_entries_count = self.time_entries_count

        updated_at = self.updated_at

        documents: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        first_message: Unset | dict[str, Any] = UNSET
        if not isinstance(self.first_message, Unset):
            first_message = self.first_message.to_dict()

        last_message: Unset | dict[str, Any] = UNSET
        if not isinstance(self.last_message, Unset):
            last_message = self.last_message.to_dict()

        matter: Unset | dict[str, Any] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        memberships: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.memberships, Unset):
            memberships = []
            for memberships_item_data in self.memberships:
                memberships_item = memberships_item_data.to_dict()
                memberships.append(memberships_item)

        messages: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived is not UNSET:
            field_dict["archived"] = archived
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if current_user_is_member is not UNSET:
            field_dict["current_user_is_member"] = current_user_is_member
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if message_count is not UNSET:
            field_dict["message_count"] = message_count
        if read is not UNSET:
            field_dict["read"] = read
        if read_only is not UNSET:
            field_dict["read_only"] = read_only
        if subject is not UNSET:
            field_dict["subject"] = subject
        if time_entries_count is not UNSET:
            field_dict["time_entries_count"] = time_entries_count
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if documents is not UNSET:
            field_dict["documents"] = documents
        if first_message is not UNSET:
            field_dict["first_message"] = first_message
        if last_message is not UNSET:
            field_dict["last_message"] = last_message
        if matter is not UNSET:
            field_dict["matter"] = matter
        if memberships is not UNSET:
            field_dict["memberships"] = memberships
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_first_message import ConversationFirstMessage
        from ..models.conversation_last_message import ConversationLastMessage
        from ..models.conversation_matter import ConversationMatter
        from ..models.conversation_membership import ConversationMembership
        from ..models.conversation_message_base import ConversationMessageBase
        from ..models.document_base import DocumentBase

        d = dict(src_dict)
        archived = d.pop("archived", UNSET)

        created_at = d.pop("created_at", UNSET)

        current_user_is_member = d.pop("current_user_is_member", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        message_count = d.pop("message_count", UNSET)

        read = d.pop("read", UNSET)

        read_only = d.pop("read_only", UNSET)

        subject = d.pop("subject", UNSET)

        time_entries_count = d.pop("time_entries_count", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = DocumentBase.from_dict(documents_item_data)

            documents.append(documents_item)

        _first_message = d.pop("first_message", UNSET)
        first_message: Unset | ConversationFirstMessage
        if isinstance(_first_message, Unset):
            first_message = UNSET
        else:
            first_message = ConversationFirstMessage.from_dict(_first_message)

        _last_message = d.pop("last_message", UNSET)
        last_message: Unset | ConversationLastMessage
        if isinstance(_last_message, Unset):
            last_message = UNSET
        else:
            last_message = ConversationLastMessage.from_dict(_last_message)

        _matter = d.pop("matter", UNSET)
        matter: Unset | ConversationMatter
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = ConversationMatter.from_dict(_matter)

        memberships = []
        _memberships = d.pop("memberships", UNSET)
        for memberships_item_data in _memberships or []:
            memberships_item = ConversationMembership.from_dict(memberships_item_data)

            memberships.append(memberships_item)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = ConversationMessageBase.from_dict(messages_item_data)

            messages.append(messages_item)

        conversation = cls(
            archived=archived,
            created_at=created_at,
            current_user_is_member=current_user_is_member,
            etag=etag,
            id=id,
            message_count=message_count,
            read=read,
            read_only=read_only,
            subject=subject,
            time_entries_count=time_entries_count,
            updated_at=updated_at,
            documents=documents,
            first_message=first_message,
            last_message=last_message,
            matter=matter,
            memberships=memberships,
            messages=messages,
        )

        conversation.additional_properties = d
        return conversation

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
