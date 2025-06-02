from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bill_base_available_state_transitions import (
    BillBaseAvailableStateTransitions,
)
from ..models.bill_base_kind import BillBaseKind
from ..models.bill_base_state import BillBaseState
from ..models.bill_base_type import BillBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_base import AddressBase
    from ..models.balance_base import BalanceBase
    from ..models.bill_bill_theme import BillBillTheme
    from ..models.bill_billing_setting import BillBillingSetting
    from ..models.bill_client import BillClient
    from ..models.bill_currency import BillCurrency
    from ..models.bill_destination_account import BillDestinationAccount
    from ..models.bill_discount import BillDiscount
    from ..models.bill_group import BillGroup
    from ..models.bill_interest import BillInterest
    from ..models.bill_legal_aid_uk_bill import BillLegalAidUkBill
    from ..models.bill_original_bill import BillOriginalBill
    from ..models.bill_user import BillUser
    from ..models.matter_balance_base import MatterBalanceBase
    from ..models.matter_base import MatterBase


T = TypeVar("T", bound="Bill")


@_attrs_define
class Bill:
    """
    Attributes:
        available_state_transitions (Union[Unset, BillBaseAvailableStateTransitions]): The available *Bill* state
            transitions.
        balance (Union[Unset, float]): The outstanding balance of the *Bill*
        can_update (Union[Unset, bool]): This value indicates if your *Bill*'s line items and information can be
            updated.
        created_at (Union[Unset, str]): The time the *Bill* was created (as a ISO-8601 timestamp)
        credits_issued (Union[Unset, float]): The total credits issued for the *Bill*
        discount_services_only (Union[Unset, str]): The selected discount is applied to services only.
        due (Union[Unset, float]): The total amount of the *Bill* with interest and less discounts
        due_at (Union[Unset, str]): The date the *Bill* is due (as a ISO-8601 date)
        end_at (Union[Unset, str]): The time the billing period ends (as a ISO-8601 date)
        etag (Union[Unset, str]): ETag for the *Bill*
        id (Union[Unset, int]): Unique identifier for the *Bill*
        issued_at (Union[Unset, str]): The time the *Bill* was issued (as a ISO-8601 date)
        kind (Union[Unset, BillBaseKind]): The kind of the *Bill*
        last_sent_at (Union[Unset, str]): The last time the *Bill* was sent (as a ISO-8601 date)
        memo (Union[Unset, str]): A memo for the *Bill*
        number (Union[Unset, str]): The *Bill* identifier (not necessarily numeric)'
        paid (Union[Unset, float]): The total amount paid for the *Bill*
        paid_at (Union[Unset, str]): The date of the last payment on the *Bill*
        pending (Union[Unset, float]): The amount of pending credit card payments on the *Bill*
        purchase_order (Union[Unset, str]): The purchase order of the *Bill*
        secondary_tax_rate (Union[Unset, float]): A secondary tax rate applied to the *Bill*
        secondary_tax_sum (Union[Unset, float]): Sum of secondary tax for the model
        secondary_taxable_sub_total (Union[Unset, int]): The subtotal of the bill's secondary tax
        services_secondary_tax (Union[Unset, float]): The total secondary tax of the bill's line items of a service kind
        services_secondary_taxable_sub_total (Union[Unset, int]): The services portion of the bill's secondary tax
        services_sub_total (Union[Unset, float]): The sub total of all the bill's line items of a service kind
        services_tax (Union[Unset, float]): The total tax of the bill's line items of a service kind
        services_taxable_sub_total (Union[Unset, int]): The services portion of the bill's primary tax
        shared (Union[Unset, bool]): Whether the *Bill* is a shared
        start_at (Union[Unset, str]): The time the billing period starts (as a ISO-8601 date)
        state (Union[Unset, BillBaseState]): The billing state the *Bill* is in
        sub_total (Union[Unset, float]): Sub total for the *Bill*
        subject (Union[Unset, str]): The subject of the *Bill*
        tax_rate (Union[Unset, float]): The tax rate to the *Bill*
        tax_sum (Union[Unset, float]): Sum of primary tax for the model
        taxable_sub_total (Union[Unset, int]): The total taxable bill amount
        total (Union[Unset, float]): The total with interest of the *Bill*
        total_tax (Union[Unset, float]): The total amount of tax for the bill.
        type_ (Union[Unset, BillBaseType]): The type of the *Bill*
        updated_at (Union[Unset, str]): The time the *Bill* was last updated (as a ISO-8601 timestamp)
        balances (Union[Unset, list['BalanceBase']]): Balance
        bill_theme (Union[Unset, BillBillTheme]):
        billing_setting (Union[Unset, BillBillingSetting]):
        client (Union[Unset, BillClient]):
        client_addresses (Union[Unset, list['AddressBase']]): Address
        currency (Union[Unset, BillCurrency]):
        destination_account (Union[Unset, BillDestinationAccount]):
        discount (Union[Unset, BillDiscount]):
        group (Union[Unset, BillGroup]):
        interest (Union[Unset, BillInterest]):
        legal_aid_uk_bill (Union[Unset, BillLegalAidUkBill]):
        matter_totals (Union[Unset, list['MatterBalanceBase']]): MatterBalance
        matters (Union[Unset, list['MatterBase']]): Matter
        original_bill (Union[Unset, BillOriginalBill]):
        user (Union[Unset, BillUser]):
    """

    available_state_transitions: Union[Unset, BillBaseAvailableStateTransitions] = UNSET
    balance: Union[Unset, float] = UNSET
    can_update: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    credits_issued: Union[Unset, float] = UNSET
    discount_services_only: Union[Unset, str] = UNSET
    due: Union[Unset, float] = UNSET
    due_at: Union[Unset, str] = UNSET
    end_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    issued_at: Union[Unset, str] = UNSET
    kind: Union[Unset, BillBaseKind] = UNSET
    last_sent_at: Union[Unset, str] = UNSET
    memo: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    paid: Union[Unset, float] = UNSET
    paid_at: Union[Unset, str] = UNSET
    pending: Union[Unset, float] = UNSET
    purchase_order: Union[Unset, str] = UNSET
    secondary_tax_rate: Union[Unset, float] = UNSET
    secondary_tax_sum: Union[Unset, float] = UNSET
    secondary_taxable_sub_total: Union[Unset, int] = UNSET
    services_secondary_tax: Union[Unset, float] = UNSET
    services_secondary_taxable_sub_total: Union[Unset, int] = UNSET
    services_sub_total: Union[Unset, float] = UNSET
    services_tax: Union[Unset, float] = UNSET
    services_taxable_sub_total: Union[Unset, int] = UNSET
    shared: Union[Unset, bool] = UNSET
    start_at: Union[Unset, str] = UNSET
    state: Union[Unset, BillBaseState] = UNSET
    sub_total: Union[Unset, float] = UNSET
    subject: Union[Unset, str] = UNSET
    tax_rate: Union[Unset, float] = UNSET
    tax_sum: Union[Unset, float] = UNSET
    taxable_sub_total: Union[Unset, int] = UNSET
    total: Union[Unset, float] = UNSET
    total_tax: Union[Unset, float] = UNSET
    type_: Union[Unset, BillBaseType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    balances: Union[Unset, list["BalanceBase"]] = UNSET
    bill_theme: Union[Unset, "BillBillTheme"] = UNSET
    billing_setting: Union[Unset, "BillBillingSetting"] = UNSET
    client: Union[Unset, "BillClient"] = UNSET
    client_addresses: Union[Unset, list["AddressBase"]] = UNSET
    currency: Union[Unset, "BillCurrency"] = UNSET
    destination_account: Union[Unset, "BillDestinationAccount"] = UNSET
    discount: Union[Unset, "BillDiscount"] = UNSET
    group: Union[Unset, "BillGroup"] = UNSET
    interest: Union[Unset, "BillInterest"] = UNSET
    legal_aid_uk_bill: Union[Unset, "BillLegalAidUkBill"] = UNSET
    matter_totals: Union[Unset, list["MatterBalanceBase"]] = UNSET
    matters: Union[Unset, list["MatterBase"]] = UNSET
    original_bill: Union[Unset, "BillOriginalBill"] = UNSET
    user: Union[Unset, "BillUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_state_transitions: Union[Unset, str] = UNSET
        if not isinstance(self.available_state_transitions, Unset):
            available_state_transitions = self.available_state_transitions.value

        balance = self.balance

        can_update = self.can_update

        created_at = self.created_at

        credits_issued = self.credits_issued

        discount_services_only = self.discount_services_only

        due = self.due

        due_at = self.due_at

        end_at = self.end_at

        etag = self.etag

        id = self.id

        issued_at = self.issued_at

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        last_sent_at = self.last_sent_at

        memo = self.memo

        number = self.number

        paid = self.paid

        paid_at = self.paid_at

        pending = self.pending

        purchase_order = self.purchase_order

        secondary_tax_rate = self.secondary_tax_rate

        secondary_tax_sum = self.secondary_tax_sum

        secondary_taxable_sub_total = self.secondary_taxable_sub_total

        services_secondary_tax = self.services_secondary_tax

        services_secondary_taxable_sub_total = self.services_secondary_taxable_sub_total

        services_sub_total = self.services_sub_total

        services_tax = self.services_tax

        services_taxable_sub_total = self.services_taxable_sub_total

        shared = self.shared

        start_at = self.start_at

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        sub_total = self.sub_total

        subject = self.subject

        tax_rate = self.tax_rate

        tax_sum = self.tax_sum

        taxable_sub_total = self.taxable_sub_total

        total = self.total

        total_tax = self.total_tax

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        balances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.balances, Unset):
            balances = []
            for balances_item_data in self.balances:
                balances_item = balances_item_data.to_dict()
                balances.append(balances_item)

        bill_theme: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bill_theme, Unset):
            bill_theme = self.bill_theme.to_dict()

        billing_setting: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.billing_setting, Unset):
            billing_setting = self.billing_setting.to_dict()

        client: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        client_addresses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.client_addresses, Unset):
            client_addresses = []
            for client_addresses_item_data in self.client_addresses:
                client_addresses_item = client_addresses_item_data.to_dict()
                client_addresses.append(client_addresses_item)

        currency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        destination_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.destination_account, Unset):
            destination_account = self.destination_account.to_dict()

        discount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        interest: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.interest, Unset):
            interest = self.interest.to_dict()

        legal_aid_uk_bill: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legal_aid_uk_bill, Unset):
            legal_aid_uk_bill = self.legal_aid_uk_bill.to_dict()

        matter_totals: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matter_totals, Unset):
            matter_totals = []
            for matter_totals_item_data in self.matter_totals:
                matter_totals_item = matter_totals_item_data.to_dict()
                matter_totals.append(matter_totals_item)

        matters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matters, Unset):
            matters = []
            for matters_item_data in self.matters:
                matters_item = matters_item_data.to_dict()
                matters.append(matters_item)

        original_bill: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.original_bill, Unset):
            original_bill = self.original_bill.to_dict()

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_state_transitions is not UNSET:
            field_dict["available_state_transitions"] = available_state_transitions
        if balance is not UNSET:
            field_dict["balance"] = balance
        if can_update is not UNSET:
            field_dict["can_update"] = can_update
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if credits_issued is not UNSET:
            field_dict["credits_issued"] = credits_issued
        if discount_services_only is not UNSET:
            field_dict["discount_services_only"] = discount_services_only
        if due is not UNSET:
            field_dict["due"] = due
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if issued_at is not UNSET:
            field_dict["issued_at"] = issued_at
        if kind is not UNSET:
            field_dict["kind"] = kind
        if last_sent_at is not UNSET:
            field_dict["last_sent_at"] = last_sent_at
        if memo is not UNSET:
            field_dict["memo"] = memo
        if number is not UNSET:
            field_dict["number"] = number
        if paid is not UNSET:
            field_dict["paid"] = paid
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if pending is not UNSET:
            field_dict["pending"] = pending
        if purchase_order is not UNSET:
            field_dict["purchase_order"] = purchase_order
        if secondary_tax_rate is not UNSET:
            field_dict["secondary_tax_rate"] = secondary_tax_rate
        if secondary_tax_sum is not UNSET:
            field_dict["secondary_tax_sum"] = secondary_tax_sum
        if secondary_taxable_sub_total is not UNSET:
            field_dict["secondary_taxable_sub_total"] = secondary_taxable_sub_total
        if services_secondary_tax is not UNSET:
            field_dict["services_secondary_tax"] = services_secondary_tax
        if services_secondary_taxable_sub_total is not UNSET:
            field_dict["services_secondary_taxable_sub_total"] = services_secondary_taxable_sub_total
        if services_sub_total is not UNSET:
            field_dict["services_sub_total"] = services_sub_total
        if services_tax is not UNSET:
            field_dict["services_tax"] = services_tax
        if services_taxable_sub_total is not UNSET:
            field_dict["services_taxable_sub_total"] = services_taxable_sub_total
        if shared is not UNSET:
            field_dict["shared"] = shared
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if state is not UNSET:
            field_dict["state"] = state
        if sub_total is not UNSET:
            field_dict["sub_total"] = sub_total
        if subject is not UNSET:
            field_dict["subject"] = subject
        if tax_rate is not UNSET:
            field_dict["tax_rate"] = tax_rate
        if tax_sum is not UNSET:
            field_dict["tax_sum"] = tax_sum
        if taxable_sub_total is not UNSET:
            field_dict["taxable_sub_total"] = taxable_sub_total
        if total is not UNSET:
            field_dict["total"] = total
        if total_tax is not UNSET:
            field_dict["total_tax"] = total_tax
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if balances is not UNSET:
            field_dict["balances"] = balances
        if bill_theme is not UNSET:
            field_dict["bill_theme"] = bill_theme
        if billing_setting is not UNSET:
            field_dict["billing_setting"] = billing_setting
        if client is not UNSET:
            field_dict["client"] = client
        if client_addresses is not UNSET:
            field_dict["client_addresses"] = client_addresses
        if currency is not UNSET:
            field_dict["currency"] = currency
        if destination_account is not UNSET:
            field_dict["destination_account"] = destination_account
        if discount is not UNSET:
            field_dict["discount"] = discount
        if group is not UNSET:
            field_dict["group"] = group
        if interest is not UNSET:
            field_dict["interest"] = interest
        if legal_aid_uk_bill is not UNSET:
            field_dict["legal_aid_uk_bill"] = legal_aid_uk_bill
        if matter_totals is not UNSET:
            field_dict["matter_totals"] = matter_totals
        if matters is not UNSET:
            field_dict["matters"] = matters
        if original_bill is not UNSET:
            field_dict["original_bill"] = original_bill
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_base import AddressBase
        from ..models.balance_base import BalanceBase
        from ..models.bill_bill_theme import BillBillTheme
        from ..models.bill_billing_setting import BillBillingSetting
        from ..models.bill_client import BillClient
        from ..models.bill_currency import BillCurrency
        from ..models.bill_destination_account import BillDestinationAccount
        from ..models.bill_discount import BillDiscount
        from ..models.bill_group import BillGroup
        from ..models.bill_interest import BillInterest
        from ..models.bill_legal_aid_uk_bill import BillLegalAidUkBill
        from ..models.bill_original_bill import BillOriginalBill
        from ..models.bill_user import BillUser
        from ..models.matter_balance_base import MatterBalanceBase
        from ..models.matter_base import MatterBase

        d = dict(src_dict)
        _available_state_transitions = d.pop("available_state_transitions", UNSET)
        available_state_transitions: Union[Unset, BillBaseAvailableStateTransitions]
        if isinstance(_available_state_transitions, Unset):
            available_state_transitions = UNSET
        else:
            available_state_transitions = BillBaseAvailableStateTransitions(_available_state_transitions)

        balance = d.pop("balance", UNSET)

        can_update = d.pop("can_update", UNSET)

        created_at = d.pop("created_at", UNSET)

        credits_issued = d.pop("credits_issued", UNSET)

        discount_services_only = d.pop("discount_services_only", UNSET)

        due = d.pop("due", UNSET)

        due_at = d.pop("due_at", UNSET)

        end_at = d.pop("end_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        issued_at = d.pop("issued_at", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, BillBaseKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = BillBaseKind(_kind)

        last_sent_at = d.pop("last_sent_at", UNSET)

        memo = d.pop("memo", UNSET)

        number = d.pop("number", UNSET)

        paid = d.pop("paid", UNSET)

        paid_at = d.pop("paid_at", UNSET)

        pending = d.pop("pending", UNSET)

        purchase_order = d.pop("purchase_order", UNSET)

        secondary_tax_rate = d.pop("secondary_tax_rate", UNSET)

        secondary_tax_sum = d.pop("secondary_tax_sum", UNSET)

        secondary_taxable_sub_total = d.pop("secondary_taxable_sub_total", UNSET)

        services_secondary_tax = d.pop("services_secondary_tax", UNSET)

        services_secondary_taxable_sub_total = d.pop("services_secondary_taxable_sub_total", UNSET)

        services_sub_total = d.pop("services_sub_total", UNSET)

        services_tax = d.pop("services_tax", UNSET)

        services_taxable_sub_total = d.pop("services_taxable_sub_total", UNSET)

        shared = d.pop("shared", UNSET)

        start_at = d.pop("start_at", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, BillBaseState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = BillBaseState(_state)

        sub_total = d.pop("sub_total", UNSET)

        subject = d.pop("subject", UNSET)

        tax_rate = d.pop("tax_rate", UNSET)

        tax_sum = d.pop("tax_sum", UNSET)

        taxable_sub_total = d.pop("taxable_sub_total", UNSET)

        total = d.pop("total", UNSET)

        total_tax = d.pop("total_tax", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BillBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BillBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        balances = []
        _balances = d.pop("balances", UNSET)
        for balances_item_data in _balances or []:
            balances_item = BalanceBase.from_dict(balances_item_data)

            balances.append(balances_item)

        _bill_theme = d.pop("bill_theme", UNSET)
        bill_theme: Union[Unset, BillBillTheme]
        if isinstance(_bill_theme, Unset):
            bill_theme = UNSET
        else:
            bill_theme = BillBillTheme.from_dict(_bill_theme)

        _billing_setting = d.pop("billing_setting", UNSET)
        billing_setting: Union[Unset, BillBillingSetting]
        if isinstance(_billing_setting, Unset):
            billing_setting = UNSET
        else:
            billing_setting = BillBillingSetting.from_dict(_billing_setting)

        _client = d.pop("client", UNSET)
        client: Union[Unset, BillClient]
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = BillClient.from_dict(_client)

        client_addresses = []
        _client_addresses = d.pop("client_addresses", UNSET)
        for client_addresses_item_data in _client_addresses or []:
            client_addresses_item = AddressBase.from_dict(client_addresses_item_data)

            client_addresses.append(client_addresses_item)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, BillCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = BillCurrency.from_dict(_currency)

        _destination_account = d.pop("destination_account", UNSET)
        destination_account: Union[Unset, BillDestinationAccount]
        if isinstance(_destination_account, Unset):
            destination_account = UNSET
        else:
            destination_account = BillDestinationAccount.from_dict(_destination_account)

        _discount = d.pop("discount", UNSET)
        discount: Union[Unset, BillDiscount]
        if isinstance(_discount, Unset):
            discount = UNSET
        else:
            discount = BillDiscount.from_dict(_discount)

        _group = d.pop("group", UNSET)
        group: Union[Unset, BillGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = BillGroup.from_dict(_group)

        _interest = d.pop("interest", UNSET)
        interest: Union[Unset, BillInterest]
        if isinstance(_interest, Unset):
            interest = UNSET
        else:
            interest = BillInterest.from_dict(_interest)

        _legal_aid_uk_bill = d.pop("legal_aid_uk_bill", UNSET)
        legal_aid_uk_bill: Union[Unset, BillLegalAidUkBill]
        if isinstance(_legal_aid_uk_bill, Unset):
            legal_aid_uk_bill = UNSET
        else:
            legal_aid_uk_bill = BillLegalAidUkBill.from_dict(_legal_aid_uk_bill)

        matter_totals = []
        _matter_totals = d.pop("matter_totals", UNSET)
        for matter_totals_item_data in _matter_totals or []:
            matter_totals_item = MatterBalanceBase.from_dict(matter_totals_item_data)

            matter_totals.append(matter_totals_item)

        matters = []
        _matters = d.pop("matters", UNSET)
        for matters_item_data in _matters or []:
            matters_item = MatterBase.from_dict(matters_item_data)

            matters.append(matters_item)

        _original_bill = d.pop("original_bill", UNSET)
        original_bill: Union[Unset, BillOriginalBill]
        if isinstance(_original_bill, Unset):
            original_bill = UNSET
        else:
            original_bill = BillOriginalBill.from_dict(_original_bill)

        _user = d.pop("user", UNSET)
        user: Union[Unset, BillUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = BillUser.from_dict(_user)

        bill = cls(
            available_state_transitions=available_state_transitions,
            balance=balance,
            can_update=can_update,
            created_at=created_at,
            credits_issued=credits_issued,
            discount_services_only=discount_services_only,
            due=due,
            due_at=due_at,
            end_at=end_at,
            etag=etag,
            id=id,
            issued_at=issued_at,
            kind=kind,
            last_sent_at=last_sent_at,
            memo=memo,
            number=number,
            paid=paid,
            paid_at=paid_at,
            pending=pending,
            purchase_order=purchase_order,
            secondary_tax_rate=secondary_tax_rate,
            secondary_tax_sum=secondary_tax_sum,
            secondary_taxable_sub_total=secondary_taxable_sub_total,
            services_secondary_tax=services_secondary_tax,
            services_secondary_taxable_sub_total=services_secondary_taxable_sub_total,
            services_sub_total=services_sub_total,
            services_tax=services_tax,
            services_taxable_sub_total=services_taxable_sub_total,
            shared=shared,
            start_at=start_at,
            state=state,
            sub_total=sub_total,
            subject=subject,
            tax_rate=tax_rate,
            tax_sum=tax_sum,
            taxable_sub_total=taxable_sub_total,
            total=total,
            total_tax=total_tax,
            type_=type_,
            updated_at=updated_at,
            balances=balances,
            bill_theme=bill_theme,
            billing_setting=billing_setting,
            client=client,
            client_addresses=client_addresses,
            currency=currency,
            destination_account=destination_account,
            discount=discount,
            group=group,
            interest=interest,
            legal_aid_uk_bill=legal_aid_uk_bill,
            matter_totals=matter_totals,
            matters=matters,
            original_bill=original_bill,
            user=user,
        )

        bill.additional_properties = d
        return bill

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
