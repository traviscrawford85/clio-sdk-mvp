from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allocation_bill import AllocationBill
    from ..models.allocation_contact import AllocationContact
    from ..models.allocation_destination_bank_account import (
        AllocationDestinationBankAccount,
    )
    from ..models.allocation_matter import AllocationMatter
    from ..models.allocation_parent import AllocationParent
    from ..models.allocation_source_bank_account import AllocationSourceBankAccount


T = TypeVar("T", bound="Allocation")


@_attrs_define
class Allocation:
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
        bill (Union[Unset, AllocationBill]):
        contact (Union[Unset, AllocationContact]):
        destination_bank_account (Union[Unset, AllocationDestinationBankAccount]):
        matter (Union[Unset, AllocationMatter]):
        parent (Union[Unset, AllocationParent]):
        source_bank_account (Union[Unset, AllocationSourceBankAccount]):
    """

    amount: Union[Unset, float] = UNSET
    created_at: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    destroyable: Union[Unset, bool] = UNSET
    etag: Union[Unset, str] = UNSET
    has_online_payment: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    interest: Union[Unset, bool] = UNSET
    payment_type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    voided_at: Union[Unset, str] = UNSET
    bill: Union[Unset, "AllocationBill"] = UNSET
    contact: Union[Unset, "AllocationContact"] = UNSET
    destination_bank_account: Union[Unset, "AllocationDestinationBankAccount"] = UNSET
    matter: Union[Unset, "AllocationMatter"] = UNSET
    parent: Union[Unset, "AllocationParent"] = UNSET
    source_bank_account: Union[Unset, "AllocationSourceBankAccount"] = UNSET
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

        bill: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bill, Unset):
            bill = self.bill.to_dict()

        contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        destination_bank_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.destination_bank_account, Unset):
            destination_bank_account = self.destination_bank_account.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        parent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        source_bank_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source_bank_account, Unset):
            source_bank_account = self.source_bank_account.to_dict()

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
        if bill is not UNSET:
            field_dict["bill"] = bill
        if contact is not UNSET:
            field_dict["contact"] = contact
        if destination_bank_account is not UNSET:
            field_dict["destination_bank_account"] = destination_bank_account
        if matter is not UNSET:
            field_dict["matter"] = matter
        if parent is not UNSET:
            field_dict["parent"] = parent
        if source_bank_account is not UNSET:
            field_dict["source_bank_account"] = source_bank_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allocation_bill import AllocationBill
        from ..models.allocation_contact import AllocationContact
        from ..models.allocation_destination_bank_account import (
            AllocationDestinationBankAccount,
        )
        from ..models.allocation_matter import AllocationMatter
        from ..models.allocation_parent import AllocationParent
        from ..models.allocation_source_bank_account import AllocationSourceBankAccount

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

        _bill = d.pop("bill", UNSET)
        bill: Union[Unset, AllocationBill]
        if isinstance(_bill, Unset):
            bill = UNSET
        else:
            bill = AllocationBill.from_dict(_bill)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, AllocationContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = AllocationContact.from_dict(_contact)

        _destination_bank_account = d.pop("destination_bank_account", UNSET)
        destination_bank_account: Union[Unset, AllocationDestinationBankAccount]
        if isinstance(_destination_bank_account, Unset):
            destination_bank_account = UNSET
        else:
            destination_bank_account = AllocationDestinationBankAccount.from_dict(_destination_bank_account)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, AllocationMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = AllocationMatter.from_dict(_matter)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, AllocationParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = AllocationParent.from_dict(_parent)

        _source_bank_account = d.pop("source_bank_account", UNSET)
        source_bank_account: Union[Unset, AllocationSourceBankAccount]
        if isinstance(_source_bank_account, Unset):
            source_bank_account = UNSET
        else:
            source_bank_account = AllocationSourceBankAccount.from_dict(_source_bank_account)

        allocation = cls(
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
            bill=bill,
            contact=contact,
            destination_bank_account=destination_bank_account,
            matter=matter,
            parent=parent,
            source_bank_account=source_bank_account,
        )

        allocation.additional_properties = d
        return allocation

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
