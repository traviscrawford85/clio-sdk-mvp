from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConversationFirstMessage")


@_attrs_define
class ConversationFirstMessage:
    """
    Attributes:
        body (Union[Unset, str]): The main content of the *ConversationMessage*
        created_at (Union[Unset, str]): The time the *ConversationMessage* was created (as a ISO-8601 timestamp)
        date (Union[Unset, str]): The creation date of the message in the current user's time zone
        etag (Union[Unset, str]): ETag for the *ConversationMessage*
        id (Union[Unset, int]): Unique identifier for the *ConversationMessage*
        updated_at (Union[Unset, str]): The time the *ConversationMessage* was last updated (as a ISO-8601 timestamp)
    """

    body: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        created_at = self.created_at

        date = self.date

        etag = self.etag

        id = self.id

        updated_at = self.updated_at

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body", UNSET)

        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        conversation_first_message = cls(
            body=body,
            created_at=created_at,
            date=date,
            etag=etag,
            id=id,
            updated_at=updated_at,
        )

        conversation_first_message.additional_properties = d
        return conversation_first_message

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
