from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarEntryConferenceMeeting")


@_attrs_define
class CalendarEntryConferenceMeeting:
    """
    Attributes:
        conference_id (Union[Unset, int]): Third-party provider unique meeting ID
        conference_password (Union[Unset, str]): Third-party provider meeting password
        created_at (Union[Unset, str]): The time the *ConferenceMeeting* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *ConferenceMeeting*
        id (Union[Unset, int]): Unique identifier for the *ConferenceMeeting*
        join_url (Union[Unset, str]): URL for participants to join the video conference
        source_id (Union[Unset, int]): The external ID of the video conference meeting
        type_ (Union[Unset, str]): The type of video conference
        updated_at (Union[Unset, str]): The time the *ConferenceMeeting* was last updated (as a ISO-8601 timestamp)
    """

    conference_id: Union[Unset, int] = UNSET
    conference_password: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    join_url: Union[Unset, str] = UNSET
    source_id: Union[Unset, int] = UNSET
    type_: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conference_id = self.conference_id

        conference_password = self.conference_password

        created_at = self.created_at

        etag = self.etag

        id = self.id

        join_url = self.join_url

        source_id = self.source_id

        type_ = self.type_

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conference_id is not UNSET:
            field_dict["conference_id"] = conference_id
        if conference_password is not UNSET:
            field_dict["conference_password"] = conference_password
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if join_url is not UNSET:
            field_dict["join_url"] = join_url
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conference_id = d.pop("conference_id", UNSET)

        conference_password = d.pop("conference_password", UNSET)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        join_url = d.pop("join_url", UNSET)

        source_id = d.pop("source_id", UNSET)

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        calendar_entry_conference_meeting = cls(
            conference_id=conference_id,
            conference_password=conference_password,
            created_at=created_at,
            etag=etag,
            id=id,
            join_url=join_url,
            source_id=source_id,
            type_=type_,
            updated_at=updated_at,
        )

        calendar_entry_conference_meeting.additional_properties = d
        return calendar_entry_conference_meeting

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
