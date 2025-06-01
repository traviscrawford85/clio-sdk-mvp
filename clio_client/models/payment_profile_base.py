from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payment_profile_base_interest_type import PaymentProfileBaseInterestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentProfileBase")


@_attrs_define
class PaymentProfileBase:
    """
    Attributes:
        billing_setting_id (Union[Unset, int]): The unique identifier for the *PaymentProfile
        created_at (Union[Unset, str]): The time the *PaymentProfile* was created (as a ISO-8601 timestamp)
        discount_period (Union[Unset, int]): The early payment discount period for the *PaymentProfile
        discount_rate (Union[Unset, float]): The early payment discount rate for the *PaymentProfile
        etag (Union[Unset, str]): ETag for the *PaymentProfile*
        id (Union[Unset, int]): Unique identifier for the *PaymentProfile*
        interest_period (Union[Unset, int]): The interest period interval for the *PaymentProfile
        interest_rate (Union[Unset, float]): The interest rate for the *PaymentProfile
        interest_type (Union[Unset, PaymentProfileBaseInterestType]): The type of interest to be calculated for the
            *PaymentProfile (Simple or Compound)
        name (Union[Unset, str]): The name of the *PaymentProfile
        terms (Union[Unset, int]): The total grace period for the *PaymentProfile
        updated_at (Union[Unset, str]): The time the *PaymentProfile* was last updated (as a ISO-8601 timestamp)
    """

    billing_setting_id: Unset | int = UNSET
    created_at: Unset | str = UNSET
    discount_period: Unset | int = UNSET
    discount_rate: Unset | float = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    interest_period: Unset | int = UNSET
    interest_rate: Unset | float = UNSET
    interest_type: Unset | PaymentProfileBaseInterestType = UNSET
    name: Unset | str = UNSET
    terms: Unset | int = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_setting_id = self.billing_setting_id

        created_at = self.created_at

        discount_period = self.discount_period

        discount_rate = self.discount_rate

        etag = self.etag

        id = self.id

        interest_period = self.interest_period

        interest_rate = self.interest_rate

        interest_type: Unset | str = UNSET
        if not isinstance(self.interest_type, Unset):
            interest_type = self.interest_type.value

        name = self.name

        terms = self.terms

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_setting_id is not UNSET:
            field_dict["billing_setting_id"] = billing_setting_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if discount_period is not UNSET:
            field_dict["discount_period"] = discount_period
        if discount_rate is not UNSET:
            field_dict["discount_rate"] = discount_rate
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if interest_period is not UNSET:
            field_dict["interest_period"] = interest_period
        if interest_rate is not UNSET:
            field_dict["interest_rate"] = interest_rate
        if interest_type is not UNSET:
            field_dict["interest_type"] = interest_type
        if name is not UNSET:
            field_dict["name"] = name
        if terms is not UNSET:
            field_dict["terms"] = terms
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billing_setting_id = d.pop("billing_setting_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        discount_period = d.pop("discount_period", UNSET)

        discount_rate = d.pop("discount_rate", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        interest_period = d.pop("interest_period", UNSET)

        interest_rate = d.pop("interest_rate", UNSET)

        _interest_type = d.pop("interest_type", UNSET)
        interest_type: Unset | PaymentProfileBaseInterestType
        if isinstance(_interest_type, Unset):
            interest_type = UNSET
        else:
            interest_type = PaymentProfileBaseInterestType(_interest_type)

        name = d.pop("name", UNSET)

        terms = d.pop("terms", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        payment_profile_base = cls(
            billing_setting_id=billing_setting_id,
            created_at=created_at,
            discount_period=discount_period,
            discount_rate=discount_rate,
            etag=etag,
            id=id,
            interest_period=interest_period,
            interest_rate=interest_rate,
            interest_type=interest_type,
            name=name,
            terms=terms,
            updated_at=updated_at,
        )

        payment_profile_base.additional_properties = d
        return payment_profile_base

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
