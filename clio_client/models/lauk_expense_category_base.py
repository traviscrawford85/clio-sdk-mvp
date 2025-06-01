from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LaukExpenseCategoryBase")


@_attrs_define
class LaukExpenseCategoryBase:
    """
    Attributes:
        certificated (Union[Unset, bool]): Certificated boolean identifier for expense
        civil (Union[Unset, bool]): Civil boolean identifier for expense
        created_at (Union[Unset, str]): The time the *LaukExpenseCategory* was created (as a ISO-8601 timestamp)
        criminal (Union[Unset, bool]): Criminal boolean identifier for expense
        etag (Union[Unset, str]): ETag for the *LaukExpenseCategory*
        id (Union[Unset, int]): Unique identifier for the *LaukExpenseCategory*
        key (Union[Unset, str]): Unique key
        name (Union[Unset, str]): Expense name
        rate (Union[Unset, float]): Determines rate based on region param
        updated_at (Union[Unset, str]): The time the *LaukExpenseCategory* was last updated (as a ISO-8601 timestamp)
    """

    certificated: Unset | bool = UNSET
    civil: Unset | bool = UNSET
    created_at: Unset | str = UNSET
    criminal: Unset | bool = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    key: Unset | str = UNSET
    name: Unset | str = UNSET
    rate: Unset | float = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certificated = self.certificated

        civil = self.civil

        created_at = self.created_at

        criminal = self.criminal

        etag = self.etag

        id = self.id

        key = self.key

        name = self.name

        rate = self.rate

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificated is not UNSET:
            field_dict["certificated"] = certificated
        if civil is not UNSET:
            field_dict["civil"] = civil
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if criminal is not UNSET:
            field_dict["criminal"] = criminal
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if rate is not UNSET:
            field_dict["rate"] = rate
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certificated = d.pop("certificated", UNSET)

        civil = d.pop("civil", UNSET)

        created_at = d.pop("created_at", UNSET)

        criminal = d.pop("criminal", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        rate = d.pop("rate", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        lauk_expense_category_base = cls(
            certificated=certificated,
            civil=civil,
            created_at=created_at,
            criminal=criminal,
            etag=etag,
            id=id,
            key=key,
            name=name,
            rate=rate,
            updated_at=updated_at,
        )

        lauk_expense_category_base.additional_properties = d
        return lauk_expense_category_base

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
