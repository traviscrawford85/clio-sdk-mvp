from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConversationMembershipBase")


@_attrs_define
class ConversationMembershipBase:
    """
    Attributes:
        archived (Union[Unset, bool]): Whether or not the ConversationMembership has been archived by the member
        created_at (Union[Unset, str]): The time the *ConversationMembership* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *ConversationMembership*
        id (Union[Unset, int]): Unique identifier for the *ConversationMembership*
        read (Union[Unset, bool]): Whether or not the ConversationMembership has been read by the member
        updated_at (Union[Unset, str]): The time the *ConversationMembership* was last updated (as a ISO-8601 timestamp)
    """

    archived: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    read: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archived = self.archived

        created_at = self.created_at

        etag = self.etag

        id = self.id

        read = self.read

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived is not UNSET:
            field_dict["archived"] = archived
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if read is not UNSET:
            field_dict["read"] = read
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        archived = d.pop("archived", UNSET)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        read = d.pop("read", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        conversation_membership_base = cls(
            archived=archived,
            created_at=created_at,
            etag=etag,
            id=id,
            read=read,
            updated_at=updated_at,
        )

        conversation_membership_base.additional_properties = d
        return conversation_membership_base

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
