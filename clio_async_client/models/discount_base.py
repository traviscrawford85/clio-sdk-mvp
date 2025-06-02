from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.discount_base_type import DiscountBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiscountBase")


@_attrs_define
class DiscountBase:
    """
    Attributes:
        early_payment_period (Union[Unset, int]): The number of days for your *Discount* period. If your bill is paid
            within this time, apply your *Discount* rate to the bill.
        early_payment_rate (Union[Unset, int]): The % discount that will be applied if your *Discount* is paid within
            the early payment period.
        note (Union[Unset, str]): A note for your *Discount*
        rate (Union[Unset, float]): The rate of the *Discount%*
        type_ (Union[Unset, DiscountBaseType]): The type of *Discount* being applied in your *Discount* rate.
    """

    early_payment_period: Union[Unset, int] = UNSET
    early_payment_rate: Union[Unset, int] = UNSET
    note: Union[Unset, str] = UNSET
    rate: Union[Unset, float] = UNSET
    type_: Union[Unset, DiscountBaseType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        early_payment_period = self.early_payment_period

        early_payment_rate = self.early_payment_rate

        note = self.note

        rate = self.rate

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if early_payment_period is not UNSET:
            field_dict["early_payment_period"] = early_payment_period
        if early_payment_rate is not UNSET:
            field_dict["early_payment_rate"] = early_payment_rate
        if note is not UNSET:
            field_dict["note"] = note
        if rate is not UNSET:
            field_dict["rate"] = rate
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        early_payment_period = d.pop("early_payment_period", UNSET)

        early_payment_rate = d.pop("early_payment_rate", UNSET)

        note = d.pop("note", UNSET)

        rate = d.pop("rate", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, DiscountBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DiscountBaseType(_type_)

        discount_base = cls(
            early_payment_period=early_payment_period,
            early_payment_rate=early_payment_rate,
            note=note,
            rate=rate,
            type_=type_,
        )

        discount_base.additional_properties = d
        return discount_base

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
