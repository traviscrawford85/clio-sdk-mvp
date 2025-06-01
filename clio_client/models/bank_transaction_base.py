from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BankTransactionBase")


@_attrs_define
class BankTransactionBase:
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        bank_transaction_base = cls(
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
        )

        bank_transaction_base.additional_properties = d
        return bank_transaction_base

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
