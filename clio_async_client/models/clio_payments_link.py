from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clio_payments_link_bank_account import ClioPaymentsLinkBankAccount
    from ..models.clio_payments_link_bill import ClioPaymentsLinkBill
    from ..models.clio_payments_link_clio_payments_payment import (
        ClioPaymentsLinkClioPaymentsPayment,
    )
    from ..models.clio_payments_link_contact import ClioPaymentsLinkContact
    from ..models.clio_payments_link_destination_account import (
        ClioPaymentsLinkDestinationAccount,
    )
    from ..models.clio_payments_link_destination_contact import (
        ClioPaymentsLinkDestinationContact,
    )


T = TypeVar("T", bound="ClioPaymentsLink")


@_attrs_define
class ClioPaymentsLink:
    """
    Attributes:
        active (Union[Unset, bool]): Whether or not the payment link is active.
        amount (Union[Unset, float]): The defined amount of the payment link, if set.
        created_at (Union[Unset, str]): The time the *ClioPaymentsLink* was created (as a ISO-8601 timestamp)
        currency (Union[Unset, str]): The currency the payment link will collect.
        description (Union[Unset, str]): The defined description of the payment link, if set.
        email_address (Union[Unset, str]): The email address to pre-fill the field on the the payment link, if set.
        etag (Union[Unset, str]): ETag for the *ClioPaymentsLink*
        expires_at (Union[Unset, str]): The ISO 8601 date and time the payment link will expire.
        id (Union[Unset, int]): Unique identifier for the *ClioPaymentsLink*
        is_allocated_as_revenue (Union[Unset, bool]): Whether the payment link is allocated as revenue.
        redirect_url (Union[Unset, str]): The URL to redirect the client to after the payment has been made.
        url (Union[Unset, str]): The URL of the payment link.
        bank_account (Union[Unset, ClioPaymentsLinkBankAccount]):
        bill (Union[Unset, ClioPaymentsLinkBill]):
        clio_payments_payment (Union[Unset, ClioPaymentsLinkClioPaymentsPayment]):
        contact (Union[Unset, ClioPaymentsLinkContact]):
        destination_account (Union[Unset, ClioPaymentsLinkDestinationAccount]):
        destination_contact (Union[Unset, ClioPaymentsLinkDestinationContact]):
    """

    active: Union[Unset, bool] = UNSET
    amount: Union[Unset, float] = UNSET
    created_at: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    expires_at: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    is_allocated_as_revenue: Union[Unset, bool] = UNSET
    redirect_url: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    bank_account: Union[Unset, "ClioPaymentsLinkBankAccount"] = UNSET
    bill: Union[Unset, "ClioPaymentsLinkBill"] = UNSET
    clio_payments_payment: Union[Unset, "ClioPaymentsLinkClioPaymentsPayment"] = UNSET
    contact: Union[Unset, "ClioPaymentsLinkContact"] = UNSET
    destination_account: Union[Unset, "ClioPaymentsLinkDestinationAccount"] = UNSET
    destination_contact: Union[Unset, "ClioPaymentsLinkDestinationContact"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        amount = self.amount

        created_at = self.created_at

        currency = self.currency

        description = self.description

        email_address = self.email_address

        etag = self.etag

        expires_at = self.expires_at

        id = self.id

        is_allocated_as_revenue = self.is_allocated_as_revenue

        redirect_url = self.redirect_url

        url = self.url

        bank_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bank_account, Unset):
            bank_account = self.bank_account.to_dict()

        bill: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bill, Unset):
            bill = self.bill.to_dict()

        clio_payments_payment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.clio_payments_payment, Unset):
            clio_payments_payment = self.clio_payments_payment.to_dict()

        contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        destination_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.destination_account, Unset):
            destination_account = self.destination_account.to_dict()

        destination_contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.destination_contact, Unset):
            destination_contact = self.destination_contact.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if amount is not UNSET:
            field_dict["amount"] = amount
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if currency is not UNSET:
            field_dict["currency"] = currency
        if description is not UNSET:
            field_dict["description"] = description
        if email_address is not UNSET:
            field_dict["email_address"] = email_address
        if etag is not UNSET:
            field_dict["etag"] = etag
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if is_allocated_as_revenue is not UNSET:
            field_dict["is_allocated_as_revenue"] = is_allocated_as_revenue
        if redirect_url is not UNSET:
            field_dict["redirect_url"] = redirect_url
        if url is not UNSET:
            field_dict["url"] = url
        if bank_account is not UNSET:
            field_dict["bank_account"] = bank_account
        if bill is not UNSET:
            field_dict["bill"] = bill
        if clio_payments_payment is not UNSET:
            field_dict["clio_payments_payment"] = clio_payments_payment
        if contact is not UNSET:
            field_dict["contact"] = contact
        if destination_account is not UNSET:
            field_dict["destination_account"] = destination_account
        if destination_contact is not UNSET:
            field_dict["destination_contact"] = destination_contact

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clio_payments_link_bank_account import ClioPaymentsLinkBankAccount
        from ..models.clio_payments_link_bill import ClioPaymentsLinkBill
        from ..models.clio_payments_link_clio_payments_payment import (
            ClioPaymentsLinkClioPaymentsPayment,
        )
        from ..models.clio_payments_link_contact import ClioPaymentsLinkContact
        from ..models.clio_payments_link_destination_account import (
            ClioPaymentsLinkDestinationAccount,
        )
        from ..models.clio_payments_link_destination_contact import (
            ClioPaymentsLinkDestinationContact,
        )

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        amount = d.pop("amount", UNSET)

        created_at = d.pop("created_at", UNSET)

        currency = d.pop("currency", UNSET)

        description = d.pop("description", UNSET)

        email_address = d.pop("email_address", UNSET)

        etag = d.pop("etag", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        id = d.pop("id", UNSET)

        is_allocated_as_revenue = d.pop("is_allocated_as_revenue", UNSET)

        redirect_url = d.pop("redirect_url", UNSET)

        url = d.pop("url", UNSET)

        _bank_account = d.pop("bank_account", UNSET)
        bank_account: Union[Unset, ClioPaymentsLinkBankAccount]
        if isinstance(_bank_account, Unset):
            bank_account = UNSET
        else:
            bank_account = ClioPaymentsLinkBankAccount.from_dict(_bank_account)

        _bill = d.pop("bill", UNSET)
        bill: Union[Unset, ClioPaymentsLinkBill]
        if isinstance(_bill, Unset):
            bill = UNSET
        else:
            bill = ClioPaymentsLinkBill.from_dict(_bill)

        _clio_payments_payment = d.pop("clio_payments_payment", UNSET)
        clio_payments_payment: Union[Unset, ClioPaymentsLinkClioPaymentsPayment]
        if isinstance(_clio_payments_payment, Unset):
            clio_payments_payment = UNSET
        else:
            clio_payments_payment = ClioPaymentsLinkClioPaymentsPayment.from_dict(_clio_payments_payment)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, ClioPaymentsLinkContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ClioPaymentsLinkContact.from_dict(_contact)

        _destination_account = d.pop("destination_account", UNSET)
        destination_account: Union[Unset, ClioPaymentsLinkDestinationAccount]
        if isinstance(_destination_account, Unset):
            destination_account = UNSET
        else:
            destination_account = ClioPaymentsLinkDestinationAccount.from_dict(_destination_account)

        _destination_contact = d.pop("destination_contact", UNSET)
        destination_contact: Union[Unset, ClioPaymentsLinkDestinationContact]
        if isinstance(_destination_contact, Unset):
            destination_contact = UNSET
        else:
            destination_contact = ClioPaymentsLinkDestinationContact.from_dict(_destination_contact)

        clio_payments_link = cls(
            active=active,
            amount=amount,
            created_at=created_at,
            currency=currency,
            description=description,
            email_address=email_address,
            etag=etag,
            expires_at=expires_at,
            id=id,
            is_allocated_as_revenue=is_allocated_as_revenue,
            redirect_url=redirect_url,
            url=url,
            bank_account=bank_account,
            bill=bill,
            clio_payments_payment=clio_payments_payment,
            contact=contact,
            destination_account=destination_account,
            destination_contact=destination_contact,
        )

        clio_payments_link.additional_properties = d
        return clio_payments_link

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
