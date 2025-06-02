from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExpenseCategoryupdateJsonBodyDataGroupsItem")


@_attrs_define
class ExpenseCategoryupdateJsonBodyDataGroupsItem:
    """
    Attributes:
        field_deleted (Union[Unset, bool]): A flag to determine if this Group should lose access to this
            ExpenseCategory.
        id (Union[Unset, int]): The unique identifier for a single Group associated with the ExpenseCategory. The
            keyword `null` is not valid for this field.
    """

    field_deleted: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_deleted = self.field_deleted

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_deleted is not UNSET:
            field_dict["_deleted"] = field_deleted
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_deleted = d.pop("_deleted", UNSET)

        id = d.pop("id", UNSET)

        expense_categoryupdate_json_body_data_groups_item = cls(
            field_deleted=field_deleted,
            id=id,
        )

        expense_categoryupdate_json_body_data_groups_item.additional_properties = d
        return expense_categoryupdate_json_body_data_groups_item

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
