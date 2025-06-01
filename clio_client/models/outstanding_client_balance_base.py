from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutstandingClientBalanceBase")


@_attrs_define
class OutstandingClientBalanceBase:
    """
    Attributes:
        associated_matter_ids (Union[Unset, list[int]]): An array of Matter IDs associated with bills in the unpaid
            state
        created_at (Union[Unset, str]): The time the *OutstandingClientBalance* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *OutstandingClientBalance*
        id (Union[Unset, int]): Unique identifier for the *OutstandingClientBalance*
        last_payment_date (Union[Unset, str]): The date the most recent payment from the contact was received
        last_shared_date (Union[Unset, str]): The date of the most recently shared bills through the outstanding balance
            table
        newest_issued_bill_due_date (Union[Unset, str]): The due date of the contact's newest bill
        pending_payments_total (Union[Unset, float]): The sum of all online payments in a pending state on the
            outstanding bills
        reminders_enabled (Union[Unset, bool]): The status of automated reminders for this client
        total_outstanding_balance (Union[Unset, float]): The sum of all bills in the unpaid state
        updated_at (Union[Unset, str]): The time the *OutstandingClientBalance* was last updated (as a ISO-8601
            timestamp)
    """

    associated_matter_ids: Unset | list[int] = UNSET
    created_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    last_payment_date: Unset | str = UNSET
    last_shared_date: Unset | str = UNSET
    newest_issued_bill_due_date: Unset | str = UNSET
    pending_payments_total: Unset | float = UNSET
    reminders_enabled: Unset | bool = UNSET
    total_outstanding_balance: Unset | float = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        associated_matter_ids: Unset | list[int] = UNSET
        if not isinstance(self.associated_matter_ids, Unset):
            associated_matter_ids = self.associated_matter_ids

        created_at = self.created_at

        etag = self.etag

        id = self.id

        last_payment_date = self.last_payment_date

        last_shared_date = self.last_shared_date

        newest_issued_bill_due_date = self.newest_issued_bill_due_date

        pending_payments_total = self.pending_payments_total

        reminders_enabled = self.reminders_enabled

        total_outstanding_balance = self.total_outstanding_balance

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associated_matter_ids is not UNSET:
            field_dict["associated_matter_ids"] = associated_matter_ids
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if last_payment_date is not UNSET:
            field_dict["last_payment_date"] = last_payment_date
        if last_shared_date is not UNSET:
            field_dict["last_shared_date"] = last_shared_date
        if newest_issued_bill_due_date is not UNSET:
            field_dict["newest_issued_bill_due_date"] = newest_issued_bill_due_date
        if pending_payments_total is not UNSET:
            field_dict["pending_payments_total"] = pending_payments_total
        if reminders_enabled is not UNSET:
            field_dict["reminders_enabled"] = reminders_enabled
        if total_outstanding_balance is not UNSET:
            field_dict["total_outstanding_balance"] = total_outstanding_balance
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        associated_matter_ids = cast(list[int], d.pop("associated_matter_ids", UNSET))

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        last_payment_date = d.pop("last_payment_date", UNSET)

        last_shared_date = d.pop("last_shared_date", UNSET)

        newest_issued_bill_due_date = d.pop("newest_issued_bill_due_date", UNSET)

        pending_payments_total = d.pop("pending_payments_total", UNSET)

        reminders_enabled = d.pop("reminders_enabled", UNSET)

        total_outstanding_balance = d.pop("total_outstanding_balance", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        outstanding_client_balance_base = cls(
            associated_matter_ids=associated_matter_ids,
            created_at=created_at,
            etag=etag,
            id=id,
            last_payment_date=last_payment_date,
            last_shared_date=last_shared_date,
            newest_issued_bill_due_date=newest_issued_bill_due_date,
            pending_payments_total=pending_payments_total,
            reminders_enabled=reminders_enabled,
            total_outstanding_balance=total_outstanding_balance,
            updated_at=updated_at,
        )

        outstanding_client_balance_base.additional_properties = d
        return outstanding_client_balance_base

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
