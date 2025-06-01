from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_transaction_allocation import BankTransactionAllocation
    from ..models.bank_transaction_bank_account import BankTransactionBankAccount
    from ..models.bank_transaction_bill import BankTransactionBill
    from ..models.bank_transaction_client import BankTransactionClient
    from ..models.bank_transaction_matter import BankTransactionMatter


T = TypeVar("T", bound="BankTransaction")


@_attrs_define
class BankTransaction:
    """
    Attributes:
        amount (Union[Unset, float]): The amount of the transaction.
        bank_account_id (Union[Unset, int]): The associated bank account.
        clio_payments_transaction (Union[Unset, bool]): Whether the transaction was created through online payments.
        confirmation (Union[Unset, str]): The reference code for the transaction.
        created_at (Union[Unset, str]): The time the *BankTransaction* was created (as a ISO-8601 timestamp)
        currency (Union[Unset, str]): The currency of the transaction.
        current_account_balance (Union[Unset, float]): The current account balance.
        date (Union[Unset, str]): The date of the transaction.
        description (Union[Unset, str]): The description of the transaction.
        etag (Union[Unset, str]): ETag for the *BankTransaction*
        exchange_rate (Union[Unset, float]): The exchange rate of the transaction.
        funds_in (Union[Unset, float]): The amount of funds received in this transaction.
        funds_out (Union[Unset, float]): The amount of funds withdrawn in this transaction.
        id (Union[Unset, int]): Unique identifier for the *BankTransaction*
        read_only_confirmation (Union[Unset, bool]): Whether the transaction's reference code is read-only.
        source (Union[Unset, str]): Where the transaction came from.
        transaction_type (Union[Unset, str]): What kind of transaction.
        type_ (Union[Unset, str]): The type of the *BankTransaction*
        updated_at (Union[Unset, str]): The time the *BankTransaction* was last updated (as a ISO-8601 timestamp)
        allocation (Union[Unset, BankTransactionAllocation]):
        bank_account (Union[Unset, BankTransactionBankAccount]):
        bill (Union[Unset, BankTransactionBill]):
        client (Union[Unset, BankTransactionClient]):
        matter (Union[Unset, BankTransactionMatter]):
    """

    amount: Unset | float = UNSET
    bank_account_id: Unset | int = UNSET
    clio_payments_transaction: Unset | bool = UNSET
    confirmation: Unset | str = UNSET
    created_at: Unset | str = UNSET
    currency: Unset | str = UNSET
    current_account_balance: Unset | float = UNSET
    date: Unset | str = UNSET
    description: Unset | str = UNSET
    etag: Unset | str = UNSET
    exchange_rate: Unset | float = UNSET
    funds_in: Unset | float = UNSET
    funds_out: Unset | float = UNSET
    id: Unset | int = UNSET
    read_only_confirmation: Unset | bool = UNSET
    source: Unset | str = UNSET
    transaction_type: Unset | str = UNSET
    type_: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    allocation: Union[Unset, "BankTransactionAllocation"] = UNSET
    bank_account: Union[Unset, "BankTransactionBankAccount"] = UNSET
    bill: Union[Unset, "BankTransactionBill"] = UNSET
    client: Union[Unset, "BankTransactionClient"] = UNSET
    matter: Union[Unset, "BankTransactionMatter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        bank_account_id = self.bank_account_id

        clio_payments_transaction = self.clio_payments_transaction

        confirmation = self.confirmation

        created_at = self.created_at

        currency = self.currency

        current_account_balance = self.current_account_balance

        date = self.date

        description = self.description

        etag = self.etag

        exchange_rate = self.exchange_rate

        funds_in = self.funds_in

        funds_out = self.funds_out

        id = self.id

        read_only_confirmation = self.read_only_confirmation

        source = self.source

        transaction_type = self.transaction_type

        type_ = self.type_

        updated_at = self.updated_at

        allocation: Unset | dict[str, Any] = UNSET
        if not isinstance(self.allocation, Unset):
            allocation = self.allocation.to_dict()

        bank_account: Unset | dict[str, Any] = UNSET
        if not isinstance(self.bank_account, Unset):
            bank_account = self.bank_account.to_dict()

        bill: Unset | dict[str, Any] = UNSET
        if not isinstance(self.bill, Unset):
            bill = self.bill.to_dict()

        client: Unset | dict[str, Any] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        matter: Unset | dict[str, Any] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if bank_account_id is not UNSET:
            field_dict["bank_account_id"] = bank_account_id
        if clio_payments_transaction is not UNSET:
            field_dict["clio_payments_transaction"] = clio_payments_transaction
        if confirmation is not UNSET:
            field_dict["confirmation"] = confirmation
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if currency is not UNSET:
            field_dict["currency"] = currency
        if current_account_balance is not UNSET:
            field_dict["current_account_balance"] = current_account_balance
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if etag is not UNSET:
            field_dict["etag"] = etag
        if exchange_rate is not UNSET:
            field_dict["exchange_rate"] = exchange_rate
        if funds_in is not UNSET:
            field_dict["funds_in"] = funds_in
        if funds_out is not UNSET:
            field_dict["funds_out"] = funds_out
        if id is not UNSET:
            field_dict["id"] = id
        if read_only_confirmation is not UNSET:
            field_dict["read_only_confirmation"] = read_only_confirmation
        if source is not UNSET:
            field_dict["source"] = source
        if transaction_type is not UNSET:
            field_dict["transaction_type"] = transaction_type
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if allocation is not UNSET:
            field_dict["allocation"] = allocation
        if bank_account is not UNSET:
            field_dict["bank_account"] = bank_account
        if bill is not UNSET:
            field_dict["bill"] = bill
        if client is not UNSET:
            field_dict["client"] = client
        if matter is not UNSET:
            field_dict["matter"] = matter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bank_transaction_allocation import BankTransactionAllocation
        from ..models.bank_transaction_bank_account import BankTransactionBankAccount
        from ..models.bank_transaction_bill import BankTransactionBill
        from ..models.bank_transaction_client import BankTransactionClient
        from ..models.bank_transaction_matter import BankTransactionMatter

        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        bank_account_id = d.pop("bank_account_id", UNSET)

        clio_payments_transaction = d.pop("clio_payments_transaction", UNSET)

        confirmation = d.pop("confirmation", UNSET)

        created_at = d.pop("created_at", UNSET)

        currency = d.pop("currency", UNSET)

        current_account_balance = d.pop("current_account_balance", UNSET)

        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        exchange_rate = d.pop("exchange_rate", UNSET)

        funds_in = d.pop("funds_in", UNSET)

        funds_out = d.pop("funds_out", UNSET)

        id = d.pop("id", UNSET)

        read_only_confirmation = d.pop("read_only_confirmation", UNSET)

        source = d.pop("source", UNSET)

        transaction_type = d.pop("transaction_type", UNSET)

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _allocation = d.pop("allocation", UNSET)
        allocation: Unset | BankTransactionAllocation
        if isinstance(_allocation, Unset):
            allocation = UNSET
        else:
            allocation = BankTransactionAllocation.from_dict(_allocation)

        _bank_account = d.pop("bank_account", UNSET)
        bank_account: Unset | BankTransactionBankAccount
        if isinstance(_bank_account, Unset):
            bank_account = UNSET
        else:
            bank_account = BankTransactionBankAccount.from_dict(_bank_account)

        _bill = d.pop("bill", UNSET)
        bill: Unset | BankTransactionBill
        if isinstance(_bill, Unset):
            bill = UNSET
        else:
            bill = BankTransactionBill.from_dict(_bill)

        _client = d.pop("client", UNSET)
        client: Unset | BankTransactionClient
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = BankTransactionClient.from_dict(_client)

        _matter = d.pop("matter", UNSET)
        matter: Unset | BankTransactionMatter
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = BankTransactionMatter.from_dict(_matter)

        bank_transaction = cls(
            amount=amount,
            bank_account_id=bank_account_id,
            clio_payments_transaction=clio_payments_transaction,
            confirmation=confirmation,
            created_at=created_at,
            currency=currency,
            current_account_balance=current_account_balance,
            date=date,
            description=description,
            etag=etag,
            exchange_rate=exchange_rate,
            funds_in=funds_in,
            funds_out=funds_out,
            id=id,
            read_only_confirmation=read_only_confirmation,
            source=source,
            transaction_type=transaction_type,
            type_=type_,
            updated_at=updated_at,
            allocation=allocation,
            bank_account=bank_account,
            bill=bill,
            client=client,
            matter=matter,
        )

        bank_transaction.additional_properties = d
        return bank_transaction

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
