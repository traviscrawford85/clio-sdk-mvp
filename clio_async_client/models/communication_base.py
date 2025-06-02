from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.communication_base_type import CommunicationBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommunicationBase")


@_attrs_define
class CommunicationBase:
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
    """

    body: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    received_at: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    time_entries_count: Union[Unset, int] = UNSET
    type_: Union[Unset, CommunicationBaseType] = UNSET
    updated_at: Union[Unset, str] = UNSET
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

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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
        type_: Union[Unset, CommunicationBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CommunicationBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        communication_base = cls(
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
        )

        communication_base.additional_properties = d
        return communication_base

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
