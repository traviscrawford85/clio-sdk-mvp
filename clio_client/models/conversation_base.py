from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConversationBase")


@_attrs_define
class ConversationBase:
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        conversation_base = cls(
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
        )

        conversation_base.additional_properties = d
        return conversation_base

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
