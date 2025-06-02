from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillableMatterBase")


@_attrs_define
class BillableMatterBase:
    """
    Attributes:
        amount_in_trust (Union[Unset, float]): The trust amount available for the matter
        display_number (Union[Unset, str]): The reference to the matter
        id (Union[Unset, int]): Unique identifier for the *BillableMatter*
        unbilled_amount (Union[Unset, float]): The unbilled amount for the matter
        unbilled_hours (Union[Unset, float]): The unbilled number of hours for the matter
    """

    amount_in_trust: Union[Unset, float] = UNSET
    display_number: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    unbilled_amount: Union[Unset, float] = UNSET
    unbilled_hours: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_in_trust = self.amount_in_trust

        display_number = self.display_number

        id = self.id

        unbilled_amount = self.unbilled_amount

        unbilled_hours = self.unbilled_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_in_trust is not UNSET:
            field_dict["amount_in_trust"] = amount_in_trust
        if display_number is not UNSET:
            field_dict["display_number"] = display_number
        if id is not UNSET:
            field_dict["id"] = id
        if unbilled_amount is not UNSET:
            field_dict["unbilled_amount"] = unbilled_amount
        if unbilled_hours is not UNSET:
            field_dict["unbilled_hours"] = unbilled_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_in_trust = d.pop("amount_in_trust", UNSET)

        display_number = d.pop("display_number", UNSET)

        id = d.pop("id", UNSET)

        unbilled_amount = d.pop("unbilled_amount", UNSET)

        unbilled_hours = d.pop("unbilled_hours", UNSET)

        billable_matter_base = cls(
            amount_in_trust=amount_in_trust,
            display_number=display_number,
            id=id,
            unbilled_amount=unbilled_amount,
            unbilled_hours=unbilled_hours,
        )

        billable_matter_base.additional_properties = d
        return billable_matter_base

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
