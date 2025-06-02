from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.balance_base_type import BalanceBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BalanceBase")


@_attrs_define
class BalanceBase:
    """
    Attributes:
        amount (Union[Unset, float]): The amount for this Balance.
        due (Union[Unset, float]): The amount due for this Balance, factoring in applicable discounts.
        id (Union[Unset, int]): Unique identifier for the *Balance*
        interest_amount (Union[Unset, float]): The interest amount for this Balance.
        type_ (Union[Unset, BalanceBaseType]): The type of Balance this data is for.
    """

    amount: Union[Unset, float] = UNSET
    due: Union[Unset, float] = UNSET
    id: Union[Unset, int] = UNSET
    interest_amount: Union[Unset, float] = UNSET
    type_: Union[Unset, BalanceBaseType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        due = self.due

        id = self.id

        interest_amount = self.interest_amount

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if due is not UNSET:
            field_dict["due"] = due
        if id is not UNSET:
            field_dict["id"] = id
        if interest_amount is not UNSET:
            field_dict["interest_amount"] = interest_amount
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        due = d.pop("due", UNSET)

        id = d.pop("id", UNSET)

        interest_amount = d.pop("interest_amount", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BalanceBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BalanceBaseType(_type_)

        balance_base = cls(
            amount=amount,
            due=due,
            id=id,
            interest_amount=interest_amount,
            type_=type_,
        )

        balance_base.additional_properties = d
        return balance_base

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
