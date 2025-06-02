from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityRateBase")


@_attrs_define
class ActivityRateBase:
    """
    Attributes:
        co_counsel_contact_id (Union[Unset, int]): Filter ActivityRate records for the co-counsel.
        contact_id (Union[Unset, int]): Filter ActivityRate records for the contact.
        created_at (Union[Unset, str]): The time the *ActivityRate* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *ActivityRate*
        flat_rate (Union[Unset, bool]): Whether this is a flat rate
        id (Union[Unset, int]): Unique identifier for the *ActivityRate*
        rate (Union[Unset, float]): Monetary value of this rate. Either hourly value or flat rate value
        updated_at (Union[Unset, str]): The time the *ActivityRate* was last updated (as a ISO-8601 timestamp)
    """

    co_counsel_contact_id: Union[Unset, int] = UNSET
    contact_id: Union[Unset, int] = UNSET
    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    flat_rate: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    rate: Union[Unset, float] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        co_counsel_contact_id = self.co_counsel_contact_id

        contact_id = self.contact_id

        created_at = self.created_at

        etag = self.etag

        flat_rate = self.flat_rate

        id = self.id

        rate = self.rate

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if co_counsel_contact_id is not UNSET:
            field_dict["co_counsel_contact_id"] = co_counsel_contact_id
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if flat_rate is not UNSET:
            field_dict["flat_rate"] = flat_rate
        if id is not UNSET:
            field_dict["id"] = id
        if rate is not UNSET:
            field_dict["rate"] = rate
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        co_counsel_contact_id = d.pop("co_counsel_contact_id", UNSET)

        contact_id = d.pop("contact_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        flat_rate = d.pop("flat_rate", UNSET)

        id = d.pop("id", UNSET)

        rate = d.pop("rate", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        activity_rate_base = cls(
            co_counsel_contact_id=co_counsel_contact_id,
            contact_id=contact_id,
            created_at=created_at,
            etag=etag,
            flat_rate=flat_rate,
            id=id,
            rate=rate,
            updated_at=updated_at,
        )

        activity_rate_base.additional_properties = d
        return activity_rate_base

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
