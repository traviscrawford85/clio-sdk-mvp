from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrustLineItemBase")


@_attrs_define
class TrustLineItemBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *TrustLineItem* was created (as a ISO-8601 timestamp)
        date (Union[Unset, str]): The date of the *TrustLineItem* (as a ISO-8601 date)
        etag (Union[Unset, str]): ETag for the *TrustLineItem*
        id (Union[Unset, int]): Unique identifier for the *TrustLineItem*
        note (Union[Unset, str]): Note for the *TrustLineItem*
        total (Union[Unset, float]): The total amount for the *TrustLineItem*
        updated_at (Union[Unset, str]): The time the *TrustLineItem* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    note: Union[Unset, str] = UNSET
    total: Union[Unset, float] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        date = self.date

        etag = self.etag

        id = self.id

        note = self.note

        total = self.total

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if date is not UNSET:
            field_dict["date"] = date
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if note is not UNSET:
            field_dict["note"] = note
        if total is not UNSET:
            field_dict["total"] = total
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        note = d.pop("note", UNSET)

        total = d.pop("total", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        trust_line_item_base = cls(
            created_at=created_at,
            date=date,
            etag=etag,
            id=id,
            note=note,
            total=total,
            updated_at=updated_at,
        )

        trust_line_item_base.additional_properties = d
        return trust_line_item_base

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
