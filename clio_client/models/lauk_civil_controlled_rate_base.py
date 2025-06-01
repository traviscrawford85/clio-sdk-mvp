from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LaukCivilControlledRateBase")


@_attrs_define
class LaukCivilControlledRateBase:
    """
    Attributes:
        activity (Union[Unset, str]): Activity of the *LaukCivilControlledRate*
        activity_type (Union[Unset, str]): Activity type
        category_of_law (Union[Unset, str]): Category of law
        created_at (Union[Unset, str]): The time the *LaukCivilControlledRate* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *LaukCivilControlledRate*
        exceptional (Union[Unset, float]): Fee applied for high activity count
        fee (Union[Unset, float]): Fee amount
        fee_scheme (Union[Unset, str]): Fee scheme
        id (Union[Unset, int]): Unique identifier for the *LaukCivilControlledRate*
        key (Union[Unset, str]): Unique key
        rate_type (Union[Unset, str]): Rate type
        region (Union[Unset, str]): Region
        updated_at (Union[Unset, str]): The time the *LaukCivilControlledRate* was last updated (as a ISO-8601
            timestamp)
    """

    activity: Unset | str = UNSET
    activity_type: Unset | str = UNSET
    category_of_law: Unset | str = UNSET
    created_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    exceptional: Unset | float = UNSET
    fee: Unset | float = UNSET
    fee_scheme: Unset | str = UNSET
    id: Unset | int = UNSET
    key: Unset | str = UNSET
    rate_type: Unset | str = UNSET
    region: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity = self.activity

        activity_type = self.activity_type

        category_of_law = self.category_of_law

        created_at = self.created_at

        etag = self.etag

        exceptional = self.exceptional

        fee = self.fee

        fee_scheme = self.fee_scheme

        id = self.id

        key = self.key

        rate_type = self.rate_type

        region = self.region

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity is not UNSET:
            field_dict["activity"] = activity
        if activity_type is not UNSET:
            field_dict["activity_type"] = activity_type
        if category_of_law is not UNSET:
            field_dict["category_of_law"] = category_of_law
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if exceptional is not UNSET:
            field_dict["exceptional"] = exceptional
        if fee is not UNSET:
            field_dict["fee"] = fee
        if fee_scheme is not UNSET:
            field_dict["fee_scheme"] = fee_scheme
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if rate_type is not UNSET:
            field_dict["rate_type"] = rate_type
        if region is not UNSET:
            field_dict["region"] = region
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity = d.pop("activity", UNSET)

        activity_type = d.pop("activity_type", UNSET)

        category_of_law = d.pop("category_of_law", UNSET)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        exceptional = d.pop("exceptional", UNSET)

        fee = d.pop("fee", UNSET)

        fee_scheme = d.pop("fee_scheme", UNSET)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        rate_type = d.pop("rate_type", UNSET)

        region = d.pop("region", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        lauk_civil_controlled_rate_base = cls(
            activity=activity,
            activity_type=activity_type,
            category_of_law=category_of_law,
            created_at=created_at,
            etag=etag,
            exceptional=exceptional,
            fee=fee,
            fee_scheme=fee_scheme,
            id=id,
            key=key,
            rate_type=rate_type,
            region=region,
            updated_at=updated_at,
        )

        lauk_civil_controlled_rate_base.additional_properties = d
        return lauk_civil_controlled_rate_base

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
