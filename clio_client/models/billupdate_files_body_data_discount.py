from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billupdate_files_body_data_discount_type import (
    BillupdateFilesBodyDataDiscountType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillupdateFilesBodyDataDiscount")


@_attrs_define
class BillupdateFilesBodyDataDiscount:
    """
    Attributes:
        note (Union[Unset, str]): A note for your Bill's discount.
        rate (Union[Unset, float]): Discount amount for the Bill. This can either be a percentage or monetary value,
            this is determined by the `discount[type]`.
        type_ (Union[Unset, BillupdateFilesBodyDataDiscountType]): The type of discount you are applying to your Bill
            with the `discount[rate]`.
    """

    note: Unset | str = UNSET
    rate: Unset | float = UNSET
    type_: Unset | BillupdateFilesBodyDataDiscountType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        note = self.note

        rate = self.rate

        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        note = d.pop("note", UNSET)

        rate = d.pop("rate", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Unset | BillupdateFilesBodyDataDiscountType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BillupdateFilesBodyDataDiscountType(_type_)

        billupdate_files_body_data_discount = cls(
            note=note,
            rate=rate,
            type_=type_,
        )

        billupdate_files_body_data_discount.additional_properties = d
        return billupdate_files_body_data_discount

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
