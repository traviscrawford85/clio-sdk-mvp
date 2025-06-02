from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.clio_payments_payment_base_state import ClioPaymentsPaymentBaseState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allocation_base import AllocationBase
    from ..models.bill_base import BillBase
    from ..models.clio_payments_payment_bank_transaction import (
        ClioPaymentsPaymentBankTransaction,
    )
    from ..models.clio_payments_payment_clio_payments_link import (
        ClioPaymentsPaymentClioPaymentsLink,
    )
    from ..models.clio_payments_payment_contact import ClioPaymentsPaymentContact
    from ..models.clio_payments_payment_destination_account import (
        ClioPaymentsPaymentDestinationAccount,
    )
    from ..models.clio_payments_payment_user import ClioPaymentsPaymentUser
    from ..models.matter_base import MatterBase


T = TypeVar("T", bound="ClioPaymentsPayment")


@_attrs_define
class ClioPaymentsPayment:
    """
    Attributes:
        amount (Union[Unset, float]): The amount of the payment.
        confirmation_number (Union[Unset, str]): The confirmatin number of the payment.
        created_at (Union[Unset, str]): The time the *ClioPaymentsPayment* was created (as a ISO-8601 timestamp)
        currency (Union[Unset, str]): The currency the payment was processed in.
        deposit_as_revenue (Union[Unset, bool]): Whether the payment was deposited as revenue.
        description (Union[Unset, str]): The description of the payment.
        email_address (Union[Unset, str]): The email address of the client.
        id (Union[Unset, int]): Unique identifier for the *ClioPaymentsPayment*
        state (Union[Unset, ClioPaymentsPaymentBaseState]): The state of the payment (authorized, completed, failed,
            etc).
        updated_at (Union[Unset, str]): The time the *ClioPaymentsPayment* was last updated (as a ISO-8601 timestamp)
        allocations (Union[Unset, list['AllocationBase']]): Allocation
        bank_transaction (Union[Unset, ClioPaymentsPaymentBankTransaction]):
        bills (Union[Unset, list['BillBase']]): Bill
        clio_payments_link (Union[Unset, ClioPaymentsPaymentClioPaymentsLink]):
        contact (Union[Unset, ClioPaymentsPaymentContact]):
        destination_account (Union[Unset, ClioPaymentsPaymentDestinationAccount]):
        matters (Union[Unset, list['MatterBase']]): Matter
        user (Union[Unset, ClioPaymentsPaymentUser]):
    """

    amount: Union[Unset, float] = UNSET
    confirmation_number: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    deposit_as_revenue: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    state: Union[Unset, ClioPaymentsPaymentBaseState] = UNSET
    updated_at: Union[Unset, str] = UNSET
    allocations: Union[Unset, list["AllocationBase"]] = UNSET
    bank_transaction: Union[Unset, "ClioPaymentsPaymentBankTransaction"] = UNSET
    bills: Union[Unset, list["BillBase"]] = UNSET
    clio_payments_link: Union[Unset, "ClioPaymentsPaymentClioPaymentsLink"] = UNSET
    contact: Union[Unset, "ClioPaymentsPaymentContact"] = UNSET
    destination_account: Union[Unset, "ClioPaymentsPaymentDestinationAccount"] = UNSET
    matters: Union[Unset, list["MatterBase"]] = UNSET
    user: Union[Unset, "ClioPaymentsPaymentUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        confirmation_number = self.confirmation_number

        created_at = self.created_at

        currency = self.currency

        deposit_as_revenue = self.deposit_as_revenue

        description = self.description

        email_address = self.email_address

        id = self.id

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        updated_at = self.updated_at

        allocations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.allocations, Unset):
            allocations = []
            for allocations_item_data in self.allocations:
                allocations_item = allocations_item_data.to_dict()
                allocations.append(allocations_item)

        bank_transaction: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bank_transaction, Unset):
            bank_transaction = self.bank_transaction.to_dict()

        bills: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bills, Unset):
            bills = []
            for bills_item_data in self.bills:
                bills_item = bills_item_data.to_dict()
                bills.append(bills_item)

        clio_payments_link: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.clio_payments_link, Unset):
            clio_payments_link = self.clio_payments_link.to_dict()

        contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        destination_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.destination_account, Unset):
            destination_account = self.destination_account.to_dict()

        matters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matters, Unset):
            matters = []
            for matters_item_data in self.matters:
                matters_item = matters_item_data.to_dict()
                matters.append(matters_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if confirmation_number is not UNSET:
            field_dict["confirmation_number"] = confirmation_number
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if currency is not UNSET:
            field_dict["currency"] = currency
        if deposit_as_revenue is not UNSET:
            field_dict["deposit_as_revenue"] = deposit_as_revenue
        if description is not UNSET:
            field_dict["description"] = description
        if email_address is not UNSET:
            field_dict["email_address"] = email_address
        if id is not UNSET:
            field_dict["id"] = id
        if state is not UNSET:
            field_dict["state"] = state
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if allocations is not UNSET:
            field_dict["allocations"] = allocations
        if bank_transaction is not UNSET:
            field_dict["bank_transaction"] = bank_transaction
        if bills is not UNSET:
            field_dict["bills"] = bills
        if clio_payments_link is not UNSET:
            field_dict["clio_payments_link"] = clio_payments_link
        if contact is not UNSET:
            field_dict["contact"] = contact
        if destination_account is not UNSET:
            field_dict["destination_account"] = destination_account
        if matters is not UNSET:
            field_dict["matters"] = matters
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allocation_base import AllocationBase
        from ..models.bill_base import BillBase
        from ..models.clio_payments_payment_bank_transaction import (
            ClioPaymentsPaymentBankTransaction,
        )
        from ..models.clio_payments_payment_clio_payments_link import (
            ClioPaymentsPaymentClioPaymentsLink,
        )
        from ..models.clio_payments_payment_contact import ClioPaymentsPaymentContact
        from ..models.clio_payments_payment_destination_account import (
            ClioPaymentsPaymentDestinationAccount,
        )
        from ..models.clio_payments_payment_user import ClioPaymentsPaymentUser
        from ..models.matter_base import MatterBase

        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        confirmation_number = d.pop("confirmation_number", UNSET)

        created_at = d.pop("created_at", UNSET)

        currency = d.pop("currency", UNSET)

        deposit_as_revenue = d.pop("deposit_as_revenue", UNSET)

        description = d.pop("description", UNSET)

        email_address = d.pop("email_address", UNSET)

        id = d.pop("id", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, ClioPaymentsPaymentBaseState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ClioPaymentsPaymentBaseState(_state)

        updated_at = d.pop("updated_at", UNSET)

        allocations = []
        _allocations = d.pop("allocations", UNSET)
        for allocations_item_data in _allocations or []:
            allocations_item = AllocationBase.from_dict(allocations_item_data)

            allocations.append(allocations_item)

        _bank_transaction = d.pop("bank_transaction", UNSET)
        bank_transaction: Union[Unset, ClioPaymentsPaymentBankTransaction]
        if isinstance(_bank_transaction, Unset):
            bank_transaction = UNSET
        else:
            bank_transaction = ClioPaymentsPaymentBankTransaction.from_dict(_bank_transaction)

        bills = []
        _bills = d.pop("bills", UNSET)
        for bills_item_data in _bills or []:
            bills_item = BillBase.from_dict(bills_item_data)

            bills.append(bills_item)

        _clio_payments_link = d.pop("clio_payments_link", UNSET)
        clio_payments_link: Union[Unset, ClioPaymentsPaymentClioPaymentsLink]
        if isinstance(_clio_payments_link, Unset):
            clio_payments_link = UNSET
        else:
            clio_payments_link = ClioPaymentsPaymentClioPaymentsLink.from_dict(_clio_payments_link)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, ClioPaymentsPaymentContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ClioPaymentsPaymentContact.from_dict(_contact)

        _destination_account = d.pop("destination_account", UNSET)
        destination_account: Union[Unset, ClioPaymentsPaymentDestinationAccount]
        if isinstance(_destination_account, Unset):
            destination_account = UNSET
        else:
            destination_account = ClioPaymentsPaymentDestinationAccount.from_dict(_destination_account)

        matters = []
        _matters = d.pop("matters", UNSET)
        for matters_item_data in _matters or []:
            matters_item = MatterBase.from_dict(matters_item_data)

            matters.append(matters_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ClioPaymentsPaymentUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ClioPaymentsPaymentUser.from_dict(_user)

        clio_payments_payment = cls(
            amount=amount,
            confirmation_number=confirmation_number,
            created_at=created_at,
            currency=currency,
            deposit_as_revenue=deposit_as_revenue,
            description=description,
            email_address=email_address,
            id=id,
            state=state,
            updated_at=updated_at,
            allocations=allocations,
            bank_transaction=bank_transaction,
            bills=bills,
            clio_payments_link=clio_payments_link,
            contact=contact,
            destination_account=destination_account,
            matters=matters,
            user=user,
        )

        clio_payments_payment.additional_properties = d
        return clio_payments_payment

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
