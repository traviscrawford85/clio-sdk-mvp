from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterestChargeBase")


@_attrs_define
class InterestChargeBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *InterestCharge* was created (as a ISO-8601 timestamp)
        date (Union[Unset, str]): The *InterestCharge* date (as a ISO-8601 date)
        description (Union[Unset, str]): The description for the *InterestCharge*
        etag (Union[Unset, str]): ETag for the *InterestCharge*
        id (Union[Unset, int]): Unique identifier for the *InterestCharge*
        total (Union[Unset, float]): The total amount for the *InterestCharge*
        updated_at (Union[Unset, str]): The time the *InterestCharge* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Unset | str = UNSET
    date: Unset | str = UNSET
    description: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    total: Unset | float = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        date = self.date

        description = self.description

        etag = self.etag

        id = self.id

        total = self.total

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
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

        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        total = d.pop("total", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        interest_charge_base = cls(
            created_at=created_at,
            date=date,
            description=description,
            etag=etag,
            id=id,
            total=total,
            updated_at=updated_at,
        )

        interest_charge_base.additional_properties = d
        return interest_charge_base

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
