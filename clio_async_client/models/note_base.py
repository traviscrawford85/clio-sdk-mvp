from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.note_base_type import NoteBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NoteBase")


@_attrs_define
class NoteBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *Note* was created (as a ISO-8601 timestamp)
        date (Union[Unset, str]): The date the *Note* is for (as a ISO-8601 date)
        detail (Union[Unset, str]): The body of the *Note*
        etag (Union[Unset, str]): ETag for the *Note*
        id (Union[Unset, int]): Unique identifier for the *Note*
        subject (Union[Unset, str]): The subject of the *Note*
        time_entries_count (Union[Unset, int]): The number of time_entries associated with the *Note*
        type_ (Union[Unset, NoteBaseType]): The type of the *Note*
        updated_at (Union[Unset, str]): The time the *Note* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    subject: Union[Unset, str] = UNSET
    time_entries_count: Union[Unset, int] = UNSET
    type_: Union[Unset, NoteBaseType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        date = self.date

        detail = self.detail

        etag = self.etag

        id = self.id

        subject = self.subject

        time_entries_count = self.time_entries_count

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if date is not UNSET:
            field_dict["date"] = date
        if detail is not UNSET:
            field_dict["detail"] = detail
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
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
        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        detail = d.pop("detail", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        subject = d.pop("subject", UNSET)

        time_entries_count = d.pop("time_entries_count", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, NoteBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = NoteBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        note_base = cls(
            created_at=created_at,
            date=date,
            detail=detail,
            etag=etag,
            id=id,
            subject=subject,
            time_entries_count=time_entries_count,
            type_=type_,
            updated_at=updated_at,
        )

        note_base.additional_properties = d
        return note_base

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
