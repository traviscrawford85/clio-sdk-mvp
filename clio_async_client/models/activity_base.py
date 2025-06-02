from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_base_tax_setting import ActivityBaseTaxSetting
from ..models.activity_base_type import ActivityBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityBase")


@_attrs_define
class ActivityBase:
    """
    Attributes:
        billed (Union[Unset, bool]): Whether the *Activity* has been added to an active bill that is in the state of
            `awaiting_payment` or `paid`
        contingency_fee (Union[Unset, bool]): Whether or not the *Activity* is a contingency fee
        created_at (Union[Unset, str]): The time the *Activity* was created (as a ISO-8601 timestamp)
        date (Union[Unset, str]): The date the *Activity* was performed (as a ISO-8601 date)
        etag (Union[Unset, str]): ETag for the *Activity*
        flat_rate (Union[Unset, bool]): Whether the *Activity* is a flat rate
        id (Union[Unset, int]): Unique identifier for the *Activity*
        no_charge (Union[Unset, bool]): Whether the non-billable *Activity* is shown on the bill.
        non_billable (Union[Unset, bool]): Whether the *Activity* is non-billable
        non_billable_total (Union[Unset, float]): The total cost of non-billable items in the *Activity*
        note (Union[Unset, str]): The details about the *Activity*
        on_bill (Union[Unset, bool]): Whether the *Activity* has been added to an active bill that is in the state of
            `draft`, `awaiting_approval`, `awaiting_payment` or `paid`
        price (Union[Unset, float]): The hourly or flat rate of the *Activity*
        quantity (Union[Unset, float]): The field is applicable to TimeEntry, ExpenseEntry, and SoftCostEntry.

            **Version <= 4.0.3:**
            The number of hours the TimeEntry took.

            **Latest version:**
            The number of seconds the TimeEntry took.
        quantity_in_hours (Union[Unset, float]): The number of hours the TimeEntry took.
        quantity_redacted (Union[Unset, bool]): Is `true` if any of the following fields are redacted:
            `quantity`, `rounded_quantity`, `rounded_quantity_in_hours`, `quantity_in_hours`, `total`, `non_billable_total`
        reference (Union[Unset, str]): A check reference for a HardCostEntry.
        rounded_quantity (Union[Unset, float]): The field is applicable to time entries only.

            **Version <= 4.0.3:**
            The number of hours rounded accordingly to the billing settings.
            The rounded value is used to calculate the total.

            **Latest version:**
            The number of seconds rounded accordingly to the billing settings.
            The rounded value is used to calculate the total.
        rounded_quantity_in_hours (Union[Unset, float]): The number of hours rounded accordingly to the billing
            settings.
            The rounded value is used to calculate the total.
        tax_setting (Union[Unset, ActivityBaseTaxSetting]): The option denoting whether primary tax, secondary tax, or
            both is applied to an expense entry.
        total (Union[Unset, float]): The total cost of draft, billable and billed items in the *Activity*
        type_ (Union[Unset, ActivityBaseType]): The type of the *Activity*
        updated_at (Union[Unset, str]): The time the *Activity* was last updated (as a ISO-8601 timestamp)
    """

    billed: Union[Unset, bool] = UNSET
    contingency_fee: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    flat_rate: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    no_charge: Union[Unset, bool] = UNSET
    non_billable: Union[Unset, bool] = UNSET
    non_billable_total: Union[Unset, float] = UNSET
    note: Union[Unset, str] = UNSET
    on_bill: Union[Unset, bool] = UNSET
    price: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    quantity_in_hours: Union[Unset, float] = UNSET
    quantity_redacted: Union[Unset, bool] = UNSET
    reference: Union[Unset, str] = UNSET
    rounded_quantity: Union[Unset, float] = UNSET
    rounded_quantity_in_hours: Union[Unset, float] = UNSET
    tax_setting: Union[Unset, ActivityBaseTaxSetting] = UNSET
    total: Union[Unset, float] = UNSET
    type_: Union[Unset, ActivityBaseType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billed = self.billed

        contingency_fee = self.contingency_fee

        created_at = self.created_at

        date = self.date

        etag = self.etag

        flat_rate = self.flat_rate

        id = self.id

        no_charge = self.no_charge

        non_billable = self.non_billable

        non_billable_total = self.non_billable_total

        note = self.note

        on_bill = self.on_bill

        price = self.price

        quantity = self.quantity

        quantity_in_hours = self.quantity_in_hours

        quantity_redacted = self.quantity_redacted

        reference = self.reference

        rounded_quantity = self.rounded_quantity

        rounded_quantity_in_hours = self.rounded_quantity_in_hours

        tax_setting: Union[Unset, str] = UNSET
        if not isinstance(self.tax_setting, Unset):
            tax_setting = self.tax_setting.value

        total = self.total

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billed is not UNSET:
            field_dict["billed"] = billed
        if contingency_fee is not UNSET:
            field_dict["contingency_fee"] = contingency_fee
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if date is not UNSET:
            field_dict["date"] = date
        if etag is not UNSET:
            field_dict["etag"] = etag
        if flat_rate is not UNSET:
            field_dict["flat_rate"] = flat_rate
        if id is not UNSET:
            field_dict["id"] = id
        if no_charge is not UNSET:
            field_dict["no_charge"] = no_charge
        if non_billable is not UNSET:
            field_dict["non_billable"] = non_billable
        if non_billable_total is not UNSET:
            field_dict["non_billable_total"] = non_billable_total
        if note is not UNSET:
            field_dict["note"] = note
        if on_bill is not UNSET:
            field_dict["on_bill"] = on_bill
        if price is not UNSET:
            field_dict["price"] = price
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if quantity_in_hours is not UNSET:
            field_dict["quantity_in_hours"] = quantity_in_hours
        if quantity_redacted is not UNSET:
            field_dict["quantity_redacted"] = quantity_redacted
        if reference is not UNSET:
            field_dict["reference"] = reference
        if rounded_quantity is not UNSET:
            field_dict["rounded_quantity"] = rounded_quantity
        if rounded_quantity_in_hours is not UNSET:
            field_dict["rounded_quantity_in_hours"] = rounded_quantity_in_hours
        if tax_setting is not UNSET:
            field_dict["tax_setting"] = tax_setting
        if total is not UNSET:
            field_dict["total"] = total
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billed = d.pop("billed", UNSET)

        contingency_fee = d.pop("contingency_fee", UNSET)

        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        etag = d.pop("etag", UNSET)

        flat_rate = d.pop("flat_rate", UNSET)

        id = d.pop("id", UNSET)

        no_charge = d.pop("no_charge", UNSET)

        non_billable = d.pop("non_billable", UNSET)

        non_billable_total = d.pop("non_billable_total", UNSET)

        note = d.pop("note", UNSET)

        on_bill = d.pop("on_bill", UNSET)

        price = d.pop("price", UNSET)

        quantity = d.pop("quantity", UNSET)

        quantity_in_hours = d.pop("quantity_in_hours", UNSET)

        quantity_redacted = d.pop("quantity_redacted", UNSET)

        reference = d.pop("reference", UNSET)

        rounded_quantity = d.pop("rounded_quantity", UNSET)

        rounded_quantity_in_hours = d.pop("rounded_quantity_in_hours", UNSET)

        _tax_setting = d.pop("tax_setting", UNSET)
        tax_setting: Union[Unset, ActivityBaseTaxSetting]
        if isinstance(_tax_setting, Unset):
            tax_setting = UNSET
        else:
            tax_setting = ActivityBaseTaxSetting(_tax_setting)

        total = d.pop("total", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ActivityBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ActivityBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        activity_base = cls(
            billed=billed,
            contingency_fee=contingency_fee,
            created_at=created_at,
            date=date,
            etag=etag,
            flat_rate=flat_rate,
            id=id,
            no_charge=no_charge,
            non_billable=non_billable,
            non_billable_total=non_billable_total,
            note=note,
            on_bill=on_bill,
            price=price,
            quantity=quantity,
            quantity_in_hours=quantity_in_hours,
            quantity_redacted=quantity_redacted,
            reference=reference,
            rounded_quantity=rounded_quantity,
            rounded_quantity_in_hours=rounded_quantity_in_hours,
            tax_setting=tax_setting,
            total=total,
            type_=type_,
            updated_at=updated_at,
        )

        activity_base.additional_properties = d
        return activity_base

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
