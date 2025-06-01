from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_setting_base_secondary_tax_rule import (
    BillingSettingBaseSecondaryTaxRule,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingSetting")


@_attrs_define
class BillingSetting:
    """
    Attributes:
        apply_tax_by_default (Union[Unset, bool]): Used to determine if primary tax should be applied to invoices by
            default
        created_at (Union[Unset, str]): The time the *BillingSetting* was created (as a ISO-8601 timestamp)
        currency (Union[Unset, str]): Current user setting of currency
        currency_sign (Union[Unset, str]): The sign of the current currency
        etag (Union[Unset, str]): ETag for the *BillingSetting*
        id (Union[Unset, int]): Unique identifier for the *BillingSetting*
        notify_after_bill_created (Union[Unset, bool]): Flag to indicate if users should have the option to notify other
            users when generating a bill
        rounded_duration (Union[Unset, float]): Rounded equivalent of duration submitted
        rounding (Union[Unset, int]): Minute increment for time rounding
        secondary_tax_name (Union[Unset, str]): Name shown for secondary tax on invoices using this BillingSetting
        secondary_tax_rate (Union[Unset, float]): Rate applied for secondary tax on invoices using this BillingSetting
        secondary_tax_rule (Union[Unset, BillingSettingBaseSecondaryTaxRule]): Used to determine if secondary tax should
            be applied separately or additionally to primary tax
        tax_name (Union[Unset, str]): Name shown for primary tax on invoices using this BillingSetting
        tax_rate (Union[Unset, float]): Rate applied for primary tax on invoices using this BillingSetting
        time_on_flat_rate_contingency_matters_is_non_billable (Union[Unset, bool]): Used to determine if hourly time
            entries on flat rate or contingency fee matters should be non-billable by default
        updated_at (Union[Unset, str]): The time the *BillingSetting* was last updated (as a ISO-8601 timestamp)
        use_decimal_rounding (Union[Unset, bool]): Round time to two decimal places
        use_secondary_tax (Union[Unset, bool]): Used to determine if secondary tax applies to invoices using this
            BillingSetting
        use_utbms_codes (Union[Unset, bool]): Controls usage of UTBMS codes, allowing creation of coded time entries and
            expenses
    """

    apply_tax_by_default: Unset | bool = UNSET
    created_at: Unset | str = UNSET
    currency: Unset | str = UNSET
    currency_sign: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    notify_after_bill_created: Unset | bool = UNSET
    rounded_duration: Unset | float = UNSET
    rounding: Unset | int = UNSET
    secondary_tax_name: Unset | str = UNSET
    secondary_tax_rate: Unset | float = UNSET
    secondary_tax_rule: Unset | BillingSettingBaseSecondaryTaxRule = UNSET
    tax_name: Unset | str = UNSET
    tax_rate: Unset | float = UNSET
    time_on_flat_rate_contingency_matters_is_non_billable: Unset | bool = UNSET
    updated_at: Unset | str = UNSET
    use_decimal_rounding: Unset | bool = UNSET
    use_secondary_tax: Unset | bool = UNSET
    use_utbms_codes: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apply_tax_by_default = self.apply_tax_by_default

        created_at = self.created_at

        currency = self.currency

        currency_sign = self.currency_sign

        etag = self.etag

        id = self.id

        notify_after_bill_created = self.notify_after_bill_created

        rounded_duration = self.rounded_duration

        rounding = self.rounding

        secondary_tax_name = self.secondary_tax_name

        secondary_tax_rate = self.secondary_tax_rate

        secondary_tax_rule: Unset | str = UNSET
        if not isinstance(self.secondary_tax_rule, Unset):
            secondary_tax_rule = self.secondary_tax_rule.value

        tax_name = self.tax_name

        tax_rate = self.tax_rate

        time_on_flat_rate_contingency_matters_is_non_billable = (
            self.time_on_flat_rate_contingency_matters_is_non_billable
        )

        updated_at = self.updated_at

        use_decimal_rounding = self.use_decimal_rounding

        use_secondary_tax = self.use_secondary_tax

        use_utbms_codes = self.use_utbms_codes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apply_tax_by_default is not UNSET:
            field_dict["apply_tax_by_default"] = apply_tax_by_default
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_sign is not UNSET:
            field_dict["currency_sign"] = currency_sign
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if notify_after_bill_created is not UNSET:
            field_dict["notify_after_bill_created"] = notify_after_bill_created
        if rounded_duration is not UNSET:
            field_dict["rounded_duration"] = rounded_duration
        if rounding is not UNSET:
            field_dict["rounding"] = rounding
        if secondary_tax_name is not UNSET:
            field_dict["secondary_tax_name"] = secondary_tax_name
        if secondary_tax_rate is not UNSET:
            field_dict["secondary_tax_rate"] = secondary_tax_rate
        if secondary_tax_rule is not UNSET:
            field_dict["secondary_tax_rule"] = secondary_tax_rule
        if tax_name is not UNSET:
            field_dict["tax_name"] = tax_name
        if tax_rate is not UNSET:
            field_dict["tax_rate"] = tax_rate
        if time_on_flat_rate_contingency_matters_is_non_billable is not UNSET:
            field_dict["time_on_flat_rate_contingency_matters_is_non_billable"] = (
                time_on_flat_rate_contingency_matters_is_non_billable
            )
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if use_decimal_rounding is not UNSET:
            field_dict["use_decimal_rounding"] = use_decimal_rounding
        if use_secondary_tax is not UNSET:
            field_dict["use_secondary_tax"] = use_secondary_tax
        if use_utbms_codes is not UNSET:
            field_dict["use_utbms_codes"] = use_utbms_codes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        apply_tax_by_default = d.pop("apply_tax_by_default", UNSET)

        created_at = d.pop("created_at", UNSET)

        currency = d.pop("currency", UNSET)

        currency_sign = d.pop("currency_sign", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        notify_after_bill_created = d.pop("notify_after_bill_created", UNSET)

        rounded_duration = d.pop("rounded_duration", UNSET)

        rounding = d.pop("rounding", UNSET)

        secondary_tax_name = d.pop("secondary_tax_name", UNSET)

        secondary_tax_rate = d.pop("secondary_tax_rate", UNSET)

        _secondary_tax_rule = d.pop("secondary_tax_rule", UNSET)
        secondary_tax_rule: Unset | BillingSettingBaseSecondaryTaxRule
        if isinstance(_secondary_tax_rule, Unset):
            secondary_tax_rule = UNSET
        else:
            secondary_tax_rule = BillingSettingBaseSecondaryTaxRule(_secondary_tax_rule)

        tax_name = d.pop("tax_name", UNSET)

        tax_rate = d.pop("tax_rate", UNSET)

        time_on_flat_rate_contingency_matters_is_non_billable = d.pop(
            "time_on_flat_rate_contingency_matters_is_non_billable", UNSET
        )

        updated_at = d.pop("updated_at", UNSET)

        use_decimal_rounding = d.pop("use_decimal_rounding", UNSET)

        use_secondary_tax = d.pop("use_secondary_tax", UNSET)

        use_utbms_codes = d.pop("use_utbms_codes", UNSET)

        billing_setting = cls(
            apply_tax_by_default=apply_tax_by_default,
            created_at=created_at,
            currency=currency,
            currency_sign=currency_sign,
            etag=etag,
            id=id,
            notify_after_bill_created=notify_after_bill_created,
            rounded_duration=rounded_duration,
            rounding=rounding,
            secondary_tax_name=secondary_tax_name,
            secondary_tax_rate=secondary_tax_rate,
            secondary_tax_rule=secondary_tax_rule,
            tax_name=tax_name,
            tax_rate=tax_rate,
            time_on_flat_rate_contingency_matters_is_non_billable=time_on_flat_rate_contingency_matters_is_non_billable,
            updated_at=updated_at,
            use_decimal_rounding=use_decimal_rounding,
            use_secondary_tax=use_secondary_tax,
            use_utbms_codes=use_utbms_codes,
        )

        billing_setting.additional_properties = d
        return billing_setting

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
