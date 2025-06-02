from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_template_base_priority import TaskTemplateBasePriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reminder_template_base import ReminderTemplateBase
    from ..models.task_template_assignee import TaskTemplateAssignee
    from ..models.task_template_cascading_source import TaskTemplateCascadingSource
    from ..models.task_template_task_template_list import TaskTemplateTaskTemplateList
    from ..models.task_template_task_type import TaskTemplateTaskType
    from ..models.task_template_template_creator import TaskTemplateTemplateCreator


T = TypeVar("T", bound="TaskTemplate")


@_attrs_define
class TaskTemplate:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *TaskTemplate* was created (as a ISO-8601 timestamp)
        description (Union[Unset, str]): A detailed description of the *TaskTemplate*
        etag (Union[Unset, str]): ETag for the *TaskTemplate*
        id (Union[Unset, int]): Unique identifier for the *TaskTemplate*
        name (Union[Unset, str]): The name of the *TaskTemplate*
        priority (Union[Unset, TaskTemplateBasePriority]): *TaskTemplate* priority
        private (Union[Unset, bool]): Whether the *TaskTemplate* is private.
        updated_at (Union[Unset, str]): The time the *TaskTemplate* was last updated (as a ISO-8601 timestamp)
        assignee (Union[Unset, TaskTemplateAssignee]):
        cascading_source (Union[Unset, TaskTemplateCascadingSource]):
        reminder_templates (Union[Unset, list['ReminderTemplateBase']]): ReminderTemplate
        task_template_list (Union[Unset, TaskTemplateTaskTemplateList]):
        task_type (Union[Unset, TaskTemplateTaskType]):
        template_creator (Union[Unset, TaskTemplateTemplateCreator]):
    """

    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    priority: Union[Unset, TaskTemplateBasePriority] = UNSET
    private: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    assignee: Union[Unset, "TaskTemplateAssignee"] = UNSET
    cascading_source: Union[Unset, "TaskTemplateCascadingSource"] = UNSET
    reminder_templates: Union[Unset, list["ReminderTemplateBase"]] = UNSET
    task_template_list: Union[Unset, "TaskTemplateTaskTemplateList"] = UNSET
    task_type: Union[Unset, "TaskTemplateTaskType"] = UNSET
    template_creator: Union[Unset, "TaskTemplateTemplateCreator"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        description = self.description

        etag = self.etag

        id = self.id

        name = self.name

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        private = self.private

        updated_at = self.updated_at

        assignee: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        cascading_source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cascading_source, Unset):
            cascading_source = self.cascading_source.to_dict()

        reminder_templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.reminder_templates, Unset):
            reminder_templates = []
            for reminder_templates_item_data in self.reminder_templates:
                reminder_templates_item = reminder_templates_item_data.to_dict()
                reminder_templates.append(reminder_templates_item)

        task_template_list: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.task_template_list, Unset):
            task_template_list = self.task_template_list.to_dict()

        task_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.to_dict()

        template_creator: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.template_creator, Unset):
            template_creator = self.template_creator.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if priority is not UNSET:
            field_dict["priority"] = priority
        if private is not UNSET:
            field_dict["private"] = private
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if cascading_source is not UNSET:
            field_dict["cascading_source"] = cascading_source
        if reminder_templates is not UNSET:
            field_dict["reminder_templates"] = reminder_templates
        if task_template_list is not UNSET:
            field_dict["task_template_list"] = task_template_list
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if template_creator is not UNSET:
            field_dict["template_creator"] = template_creator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reminder_template_base import ReminderTemplateBase
        from ..models.task_template_assignee import TaskTemplateAssignee
        from ..models.task_template_cascading_source import TaskTemplateCascadingSource
        from ..models.task_template_task_template_list import (
            TaskTemplateTaskTemplateList,
        )
        from ..models.task_template_task_type import TaskTemplateTaskType
        from ..models.task_template_template_creator import TaskTemplateTemplateCreator

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, TaskTemplateBasePriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = TaskTemplateBasePriority(_priority)

        private = d.pop("private", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _assignee = d.pop("assignee", UNSET)
        assignee: Union[Unset, TaskTemplateAssignee]
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = TaskTemplateAssignee.from_dict(_assignee)

        _cascading_source = d.pop("cascading_source", UNSET)
        cascading_source: Union[Unset, TaskTemplateCascadingSource]
        if isinstance(_cascading_source, Unset):
            cascading_source = UNSET
        else:
            cascading_source = TaskTemplateCascadingSource.from_dict(_cascading_source)

        reminder_templates = []
        _reminder_templates = d.pop("reminder_templates", UNSET)
        for reminder_templates_item_data in _reminder_templates or []:
            reminder_templates_item = ReminderTemplateBase.from_dict(reminder_templates_item_data)

            reminder_templates.append(reminder_templates_item)

        _task_template_list = d.pop("task_template_list", UNSET)
        task_template_list: Union[Unset, TaskTemplateTaskTemplateList]
        if isinstance(_task_template_list, Unset):
            task_template_list = UNSET
        else:
            task_template_list = TaskTemplateTaskTemplateList.from_dict(_task_template_list)

        _task_type = d.pop("task_type", UNSET)
        task_type: Union[Unset, TaskTemplateTaskType]
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = TaskTemplateTaskType.from_dict(_task_type)

        _template_creator = d.pop("template_creator", UNSET)
        template_creator: Union[Unset, TaskTemplateTemplateCreator]
        if isinstance(_template_creator, Unset):
            template_creator = UNSET
        else:
            template_creator = TaskTemplateTemplateCreator.from_dict(_template_creator)

        task_template = cls(
            created_at=created_at,
            description=description,
            etag=etag,
            id=id,
            name=name,
            priority=priority,
            private=private,
            updated_at=updated_at,
            assignee=assignee,
            cascading_source=cascading_source,
            reminder_templates=reminder_templates,
            task_template_list=task_template_list,
            task_type=task_type,
            template_creator=template_creator,
        )

        task_template.additional_properties = d
        return task_template

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
