from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expense_categoryupdate_data_body_data_entry_type import (
    ExpenseCategoryupdateDataBodyDataEntryType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expense_categoryupdate_data_body_data_groups_item import (
        ExpenseCategoryupdateDataBodyDataGroupsItem,
    )
    from ..models.expense_categoryupdate_data_body_data_utbms_code import (
        ExpenseCategoryupdateDataBodyDataUtbmsCode,
    )


T = TypeVar("T", bound="ExpenseCategoryupdateDataBodyData")


@_attrs_define
class ExpenseCategoryupdateDataBodyData:
    """
    Attributes:
        entry_type (Union[Unset, ExpenseCategoryupdateDataBodyDataEntryType]): Defaults to unassociated.
        groups (Union[Unset, list['ExpenseCategoryupdateDataBodyDataGroupsItem']]):
        name (Union[Unset, str]): Name of the Expense Category.
        rate (Union[Unset, float]): Rate of the Expense Category, default is null.
        utbms_code (Union[Unset, ExpenseCategoryupdateDataBodyDataUtbmsCode]):
    """

    entry_type: Unset | ExpenseCategoryupdateDataBodyDataEntryType = UNSET
    groups: Unset | list["ExpenseCategoryupdateDataBodyDataGroupsItem"] = UNSET
    name: Unset | str = UNSET
    rate: Unset | float = UNSET
    utbms_code: Union[Unset, "ExpenseCategoryupdateDataBodyDataUtbmsCode"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry_type: Unset | str = UNSET
        if not isinstance(self.entry_type, Unset):
            entry_type = self.entry_type.value

        groups: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        name = self.name

        rate = self.rate

        utbms_code: Unset | dict[str, Any] = UNSET
        if not isinstance(self.utbms_code, Unset):
            utbms_code = self.utbms_code.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry_type is not UNSET:
            field_dict["entry_type"] = entry_type
        if groups is not UNSET:
            field_dict["groups"] = groups
        if name is not UNSET:
            field_dict["name"] = name
        if rate is not UNSET:
            field_dict["rate"] = rate
        if utbms_code is not UNSET:
            field_dict["utbms_code"] = utbms_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.expense_categoryupdate_data_body_data_groups_item import (
            ExpenseCategoryupdateDataBodyDataGroupsItem,
        )
        from ..models.expense_categoryupdate_data_body_data_utbms_code import (
            ExpenseCategoryupdateDataBodyDataUtbmsCode,
        )

        d = dict(src_dict)
        _entry_type = d.pop("entry_type", UNSET)
        entry_type: Unset | ExpenseCategoryupdateDataBodyDataEntryType
        if isinstance(_entry_type, Unset):
            entry_type = UNSET
        else:
            entry_type = ExpenseCategoryupdateDataBodyDataEntryType(_entry_type)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = ExpenseCategoryupdateDataBodyDataGroupsItem.from_dict(
                groups_item_data
            )

            groups.append(groups_item)

        name = d.pop("name", UNSET)

        rate = d.pop("rate", UNSET)

        _utbms_code = d.pop("utbms_code", UNSET)
        utbms_code: Unset | ExpenseCategoryupdateDataBodyDataUtbmsCode
        if isinstance(_utbms_code, Unset):
            utbms_code = UNSET
        else:
            utbms_code = ExpenseCategoryupdateDataBodyDataUtbmsCode.from_dict(
                _utbms_code
            )

        expense_categoryupdate_data_body_data = cls(
            entry_type=entry_type,
            groups=groups,
            name=name,
            rate=rate,
            utbms_code=utbms_code,
        )

        expense_categoryupdate_data_body_data.additional_properties = d
        return expense_categoryupdate_data_body_data

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
