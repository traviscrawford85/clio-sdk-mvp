from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mattercreate_json_body_data_task_template_list_instances_item_task_template_list import (
        MattercreateJsonBodyDataTaskTemplateListInstancesItemTaskTemplateList,
    )


T = TypeVar("T", bound="MattercreateJsonBodyDataTaskTemplateListInstancesItem")


@_attrs_define
class MattercreateJsonBodyDataTaskTemplateListInstancesItem:
    """
    Attributes:
        task_template_list (MattercreateJsonBodyDataTaskTemplateListInstancesItemTaskTemplateList):
        assignee_id (Union[Unset, int]): The id of the user to assign the task template list to.
        due_at (Union[Unset, str]): Due date of the tasks. (Expects an ISO-8601 date).
        notify_assignees (Union[Unset, bool]): Whether or not task list assignees should be notified when the task list
            is assigned to a matter.
    """

    task_template_list: "MattercreateJsonBodyDataTaskTemplateListInstancesItemTaskTemplateList"
    assignee_id: Union[Unset, int] = UNSET
    due_at: Union[Unset, str] = UNSET
    notify_assignees: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_template_list = self.task_template_list.to_dict()

        assignee_id = self.assignee_id

        due_at = self.due_at

        notify_assignees = self.notify_assignees

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_template_list": task_template_list,
            }
        )
        if assignee_id is not UNSET:
            field_dict["assignee_id"] = assignee_id
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if notify_assignees is not UNSET:
            field_dict["notify_assignees"] = notify_assignees

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mattercreate_json_body_data_task_template_list_instances_item_task_template_list import (
            MattercreateJsonBodyDataTaskTemplateListInstancesItemTaskTemplateList,
        )

        d = dict(src_dict)
        task_template_list = MattercreateJsonBodyDataTaskTemplateListInstancesItemTaskTemplateList.from_dict(
            d.pop("task_template_list")
        )

        assignee_id = d.pop("assignee_id", UNSET)

        due_at = d.pop("due_at", UNSET)

        notify_assignees = d.pop("notify_assignees", UNSET)

        mattercreate_json_body_data_task_template_list_instances_item = cls(
            task_template_list=task_template_list,
            assignee_id=assignee_id,
            due_at=due_at,
            notify_assignees=notify_assignees,
        )

        mattercreate_json_body_data_task_template_list_instances_item.additional_properties = d
        return mattercreate_json_body_data_task_template_list_instances_item

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
