from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountBalanceBase")


@_attrs_define
class AccountBalanceBase:
    """
    Attributes:
        balance (Union[Unset, float]): The current balance of the bank account available to the matter or contact
        id (Union[Unset, int]): Unique identifier for the *AccountBalance*
        name (Union[Unset, str]): The name of the bank account
        type_ (Union[Unset, str]): The bank account type. Either Operating or Trust
    """

    balance: Unset | float = UNSET
    id: Unset | int = UNSET
    name: Unset | str = UNSET
    type_: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance = self.balance

        id = self.id

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if balance is not UNSET:
            field_dict["balance"] = balance
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        balance = d.pop("balance", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        account_balance_base = cls(
            balance=balance,
            id=id,
            name=name,
            type_=type_,
        )

        account_balance_base.additional_properties = d
        return account_balance_base

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
