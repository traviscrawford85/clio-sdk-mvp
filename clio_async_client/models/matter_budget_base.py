from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatterBudgetBase")


@_attrs_define
class MatterBudgetBase:
    """
    Attributes:
        budget (Union[Unset, float]): The amount allocated for the matter.
        created_at (Union[Unset, str]): The time the *MatterBudget* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *MatterBudget*
        id (Union[Unset, int]): Unique identifier for the *MatterBudget*
        include_expenses (Union[Unset, bool]): Whether the budget includes expenses.
        notification_threshold (Union[Unset, int]): Percentage of the budget when it starts notifying users. The number
            must be between 0 and 100.
        notify_users (Union[Unset, bool]): Whether to notify users when the matter reaches the notification threshold.
        updated_at (Union[Unset, str]): The time the *MatterBudget* was last updated (as a ISO-8601 timestamp)
    """

    budget: Union[Unset, float] = UNSET
    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    include_expenses: Union[Unset, bool] = UNSET
    notification_threshold: Union[Unset, int] = UNSET
    notify_users: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        budget = self.budget

        created_at = self.created_at

        etag = self.etag

        id = self.id

        include_expenses = self.include_expenses

        notification_threshold = self.notification_threshold

        notify_users = self.notify_users

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if budget is not UNSET:
            field_dict["budget"] = budget
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if include_expenses is not UNSET:
            field_dict["include_expenses"] = include_expenses
        if notification_threshold is not UNSET:
            field_dict["notification_threshold"] = notification_threshold
        if notify_users is not UNSET:
            field_dict["notify_users"] = notify_users
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        budget = d.pop("budget", UNSET)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        include_expenses = d.pop("include_expenses", UNSET)

        notification_threshold = d.pop("notification_threshold", UNSET)

        notify_users = d.pop("notify_users", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        matter_budget_base = cls(
            budget=budget,
            created_at=created_at,
            etag=etag,
            id=id,
            include_expenses=include_expenses,
            notification_threshold=notification_threshold,
            notify_users=notify_users,
            updated_at=updated_at,
        )

        matter_budget_base.additional_properties = d
        return matter_budget_base

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
