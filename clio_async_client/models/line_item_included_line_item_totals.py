from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LineItemIncludedLineItemTotals")


@_attrs_define
class LineItemIncludedLineItemTotals:
    """
    Attributes:
        discount_percent (Union[Unset, float]): Sum of discount as percentage for included line items.
        price (Union[Unset, float]): Sum of price for included line items.
        quantity (Union[Unset, float]): Sum of quantity for included line items.
        sub_total (Union[Unset, float]): Sum of total before discount and tax is applied.
        total (Union[Unset, float]): Sum of total for included line items.
    """

    discount_percent: Union[Unset, float] = UNSET
    price: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    total: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discount_percent = self.discount_percent

        price = self.price

        quantity = self.quantity

        sub_total = self.sub_total

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discount_percent is not UNSET:
            field_dict["discount_percent"] = discount_percent
        if price is not UNSET:
            field_dict["price"] = price
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if sub_total is not UNSET:
            field_dict["sub_total"] = sub_total
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        discount_percent = d.pop("discount_percent", UNSET)

        price = d.pop("price", UNSET)

        quantity = d.pop("quantity", UNSET)

        sub_total = d.pop("sub_total", UNSET)

        total = d.pop("total", UNSET)

        line_item_included_line_item_totals = cls(
            discount_percent=discount_percent,
            price=price,
            quantity=quantity,
            sub_total=sub_total,
            total=total,
        )

        line_item_included_line_item_totals.additional_properties = d
        return line_item_included_line_item_totals

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
