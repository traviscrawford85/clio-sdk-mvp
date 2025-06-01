from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExpenseCategoryBase")


@_attrs_define
class ExpenseCategoryBase:
    """
    Attributes:
        accessible_to_user (Union[Unset, bool]): Determines if expense category is accessible to user
        created_at (Union[Unset, str]): The time the *ExpenseCategory* was created (as a ISO-8601 timestamp)
        entry_type (Union[Unset, str]): The type of expense entry the category is associated to. Can be either
            "hard_cost", "soft_cost" or "unassociated"
        etag (Union[Unset, str]): ETag for the *ExpenseCategory*
        id (Union[Unset, int]): Unique identifier for the *ExpenseCategory*
        name (Union[Unset, str]): The name of the expense category
        rate (Union[Unset, int]): The price charged per unit cost
        tax_setting (Union[Unset, str]): The type of tax rate applied to the expense category.
        updated_at (Union[Unset, str]): The time the *ExpenseCategory* was last updated (as a ISO-8601 timestamp)
        xero_expense_code (Union[Unset, str]): Custom Xero expense code for an expense category
    """

    accessible_to_user: Unset | bool = UNSET
    created_at: Unset | str = UNSET
    entry_type: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    name: Unset | str = UNSET
    rate: Unset | int = UNSET
    tax_setting: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    xero_expense_code: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accessible_to_user = self.accessible_to_user

        created_at = self.created_at

        entry_type = self.entry_type

        etag = self.etag

        id = self.id

        name = self.name

        rate = self.rate

        tax_setting = self.tax_setting

        updated_at = self.updated_at

        xero_expense_code = self.xero_expense_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accessible_to_user is not UNSET:
            field_dict["accessible_to_user"] = accessible_to_user
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if entry_type is not UNSET:
            field_dict["entry_type"] = entry_type
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if rate is not UNSET:
            field_dict["rate"] = rate
        if tax_setting is not UNSET:
            field_dict["tax_setting"] = tax_setting
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if xero_expense_code is not UNSET:
            field_dict["xero_expense_code"] = xero_expense_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accessible_to_user = d.pop("accessible_to_user", UNSET)

        created_at = d.pop("created_at", UNSET)

        entry_type = d.pop("entry_type", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        rate = d.pop("rate", UNSET)

        tax_setting = d.pop("tax_setting", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        xero_expense_code = d.pop("xero_expense_code", UNSET)

        expense_category_base = cls(
            accessible_to_user=accessible_to_user,
            created_at=created_at,
            entry_type=entry_type,
            etag=etag,
            id=id,
            name=name,
            rate=rate,
            tax_setting=tax_setting,
            updated_at=updated_at,
            xero_expense_code=xero_expense_code,
        )

        expense_category_base.additional_properties = d
        return expense_category_base

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
