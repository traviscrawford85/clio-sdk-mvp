from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AllocationBase")


@_attrs_define
class AllocationBase:
    """
    Attributes:
        amount (Union[Unset, float]): The total amount of money that the user has allocated
        created_at (Union[Unset, str]): The time the *Allocation* was created (as a ISO-8601 timestamp)
        date (Union[Unset, str]): The date the allocation was applied (as a ISO-8601 date)
        description (Union[Unset, str]): The description from the associated Credit Memo (if applicable)
        destroyable (Union[Unset, bool]): Whether the record can be deleted or not
        etag (Union[Unset, str]): ETag for the *Allocation*
        has_online_payment (Union[Unset, bool]): Whether this allocation is associated with an online payment or not
        id (Union[Unset, int]): Unique identifier for the *Allocation*
        interest (Union[Unset, bool]): Whether the allocation is applied to interest amount
        payment_type (Union[Unset, str]): A string indicating whether the payment is a card or an eCheck payment.
        updated_at (Union[Unset, str]): The time the *Allocation* was last updated (as a ISO-8601 timestamp)
        voided_at (Union[Unset, str]): Time the *Allocation* was voided (as a ISO-8601 timestamp)
    """

    amount: Unset | float = UNSET
    created_at: Unset | str = UNSET
    date: Unset | str = UNSET
    description: Unset | str = UNSET
    destroyable: Unset | bool = UNSET
    etag: Unset | str = UNSET
    has_online_payment: Unset | bool = UNSET
    id: Unset | int = UNSET
    interest: Unset | bool = UNSET
    payment_type: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    voided_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        created_at = self.created_at

        date = self.date

        description = self.description

        destroyable = self.destroyable

        etag = self.etag

        has_online_payment = self.has_online_payment

        id = self.id

        interest = self.interest

        payment_type = self.payment_type

        updated_at = self.updated_at

        voided_at = self.voided_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if destroyable is not UNSET:
            field_dict["destroyable"] = destroyable
        if etag is not UNSET:
            field_dict["etag"] = etag
        if has_online_payment is not UNSET:
            field_dict["has_online_payment"] = has_online_payment
        if id is not UNSET:
            field_dict["id"] = id
        if interest is not UNSET:
            field_dict["interest"] = interest
        if payment_type is not UNSET:
            field_dict["payment_type"] = payment_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if voided_at is not UNSET:
            field_dict["voided_at"] = voided_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        destroyable = d.pop("destroyable", UNSET)

        etag = d.pop("etag", UNSET)

        has_online_payment = d.pop("has_online_payment", UNSET)

        id = d.pop("id", UNSET)

        interest = d.pop("interest", UNSET)

        payment_type = d.pop("payment_type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        voided_at = d.pop("voided_at", UNSET)

        allocation_base = cls(
            amount=amount,
            created_at=created_at,
            date=date,
            description=description,
            destroyable=destroyable,
            etag=etag,
            has_online_payment=has_online_payment,
            id=id,
            interest=interest,
            payment_type=payment_type,
            updated_at=updated_at,
            voided_at=voided_at,
        )

        allocation_base.additional_properties = d
        return allocation_base

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
