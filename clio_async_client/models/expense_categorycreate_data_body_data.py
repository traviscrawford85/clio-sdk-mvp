from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expense_categorycreate_data_body_data_entry_type import (
    ExpenseCategorycreateDataBodyDataEntryType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expense_categorycreate_data_body_data_groups_item import (
        ExpenseCategorycreateDataBodyDataGroupsItem,
    )
    from ..models.expense_categorycreate_data_body_data_utbms_code import (
        ExpenseCategorycreateDataBodyDataUtbmsCode,
    )


T = TypeVar("T", bound="ExpenseCategorycreateDataBodyData")


@_attrs_define
class ExpenseCategorycreateDataBodyData:
    """
    Attributes:
        name (str): Name of the Expense Category.
        entry_type (Union[Unset, ExpenseCategorycreateDataBodyDataEntryType]): Defaults to unassociated.
        groups (Union[Unset, list['ExpenseCategorycreateDataBodyDataGroupsItem']]):
        rate (Union[Unset, float]): Rate of the Expense Category, default is null.
        utbms_code (Union[Unset, ExpenseCategorycreateDataBodyDataUtbmsCode]):
    """

    name: str
    entry_type: Union[Unset, ExpenseCategorycreateDataBodyDataEntryType] = UNSET
    groups: Union[Unset, list["ExpenseCategorycreateDataBodyDataGroupsItem"]] = UNSET
    rate: Union[Unset, float] = UNSET
    utbms_code: Union[Unset, "ExpenseCategorycreateDataBodyDataUtbmsCode"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        entry_type: Union[Unset, str] = UNSET
        if not isinstance(self.entry_type, Unset):
            entry_type = self.entry_type.value

        groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        rate = self.rate

        utbms_code: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.utbms_code, Unset):
            utbms_code = self.utbms_code.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if entry_type is not UNSET:
            field_dict["entry_type"] = entry_type
        if groups is not UNSET:
            field_dict["groups"] = groups
        if rate is not UNSET:
            field_dict["rate"] = rate
        if utbms_code is not UNSET:
            field_dict["utbms_code"] = utbms_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.expense_categorycreate_data_body_data_groups_item import (
            ExpenseCategorycreateDataBodyDataGroupsItem,
        )
        from ..models.expense_categorycreate_data_body_data_utbms_code import (
            ExpenseCategorycreateDataBodyDataUtbmsCode,
        )

        d = dict(src_dict)
        name = d.pop("name")

        _entry_type = d.pop("entry_type", UNSET)
        entry_type: Union[Unset, ExpenseCategorycreateDataBodyDataEntryType]
        if isinstance(_entry_type, Unset):
            entry_type = UNSET
        else:
            entry_type = ExpenseCategorycreateDataBodyDataEntryType(_entry_type)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = ExpenseCategorycreateDataBodyDataGroupsItem.from_dict(groups_item_data)

            groups.append(groups_item)

        rate = d.pop("rate", UNSET)

        _utbms_code = d.pop("utbms_code", UNSET)
        utbms_code: Union[Unset, ExpenseCategorycreateDataBodyDataUtbmsCode]
        if isinstance(_utbms_code, Unset):
            utbms_code = UNSET
        else:
            utbms_code = ExpenseCategorycreateDataBodyDataUtbmsCode.from_dict(_utbms_code)

        expense_categorycreate_data_body_data = cls(
            name=name,
            entry_type=entry_type,
            groups=groups,
            rate=rate,
            utbms_code=utbms_code,
        )

        expense_categorycreate_data_body_data.additional_properties = d
        return expense_categorycreate_data_body_data

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
