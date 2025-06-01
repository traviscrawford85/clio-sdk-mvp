from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.taskupdate_data_body_data_cascading_offset_polarity import (
    TaskupdateDataBodyDataCascadingOffsetPolarity,
)
from ..models.taskupdate_data_body_data_cascading_offset_type import (
    TaskupdateDataBodyDataCascadingOffsetType,
)
from ..models.taskupdate_data_body_data_permission import (
    TaskupdateDataBodyDataPermission,
)
from ..models.taskupdate_data_body_data_priority import TaskupdateDataBodyDataPriority
from ..models.taskupdate_data_body_data_status import TaskupdateDataBodyDataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.taskupdate_data_body_data_assignee import (
        TaskupdateDataBodyDataAssignee,
    )
    from ..models.taskupdate_data_body_data_matter import TaskupdateDataBodyDataMatter
    from ..models.taskupdate_data_body_data_task_type import (
        TaskupdateDataBodyDataTaskType,
    )


T = TypeVar("T", bound="TaskupdateDataBodyData")


@_attrs_define
class TaskupdateDataBodyData:
    """
    Attributes:
        assignee (Union[Unset, TaskupdateDataBodyDataAssignee]):
        cascading (Union[Unset, bool]): Determines if the Task has a due date that is derived from another Task. (Note
            that if false, no other cascading information will be checked)
        cascading_offset (Union[Unset, int]): The amount of time that will differentiate the cascaded Task from its
            parent.
        cascading_offset_polarity (Union[Unset, TaskupdateDataBodyDataCascadingOffsetPolarity]): Determines whether or
            not the cascading_offset occurs before or after its parent.
        cascading_offset_type (Union[Unset, TaskupdateDataBodyDataCascadingOffsetType]): Determines the quantity of the
            cascading offset (e.g. CalendarDays, CalendarWeeks etc.)
        cascading_source (Union[Unset, int]): The parent Task that is used to determine the due_at property of the
            cascaded Task
        description (Union[Unset, str]): Longer description of the Task.
        due_at (Union[Unset, str]): Date when the Task must be completed by. (Expects an ISO-8601 date).
        matter (Union[Unset, TaskupdateDataBodyDataMatter]):
        name (Union[Unset, str]): Name of the Task.
        notify_assignee (Union[Unset, bool]): Whether or not the Task should notify the assignee on creation.
        notify_completion (Union[Unset, bool]): Whether or not the Task should notify the assigner on completion.
        permission (Union[Unset, TaskupdateDataBodyDataPermission]): Permission of the Task. Defaults to `public`
            Default: TaskupdateDataBodyDataPermission.PUBLIC.
        priority (Union[Unset, TaskupdateDataBodyDataPriority]): Priority of the Task. Default:
            TaskupdateDataBodyDataPriority.NORMAL.
        status (Union[Unset, TaskupdateDataBodyDataStatus]): Task status. Users without advanced tasks are allowed to
            select `Complete` or `Pending` only. Default: TaskupdateDataBodyDataStatus.PENDING.
        task_type (Union[Unset, TaskupdateDataBodyDataTaskType]):
        time_estimated (Union[Unset, int]): Time the Task should take to complete.
    """

    assignee: Union[Unset, "TaskupdateDataBodyDataAssignee"] = UNSET
    cascading: Unset | bool = UNSET
    cascading_offset: Unset | int = UNSET
    cascading_offset_polarity: Unset | TaskupdateDataBodyDataCascadingOffsetPolarity = (
        UNSET
    )
    cascading_offset_type: Unset | TaskupdateDataBodyDataCascadingOffsetType = UNSET
    cascading_source: Unset | int = UNSET
    description: Unset | str = UNSET
    due_at: Unset | str = UNSET
    matter: Union[Unset, "TaskupdateDataBodyDataMatter"] = UNSET
    name: Unset | str = UNSET
    notify_assignee: Unset | bool = UNSET
    notify_completion: Unset | bool = UNSET
    permission: Unset | TaskupdateDataBodyDataPermission = (
        TaskupdateDataBodyDataPermission.PUBLIC
    )
    priority: Unset | TaskupdateDataBodyDataPriority = (
        TaskupdateDataBodyDataPriority.NORMAL
    )
    status: Unset | TaskupdateDataBodyDataStatus = TaskupdateDataBodyDataStatus.PENDING
    task_type: Union[Unset, "TaskupdateDataBodyDataTaskType"] = UNSET
    time_estimated: Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignee: Unset | dict[str, Any] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        cascading = self.cascading

        cascading_offset = self.cascading_offset

        cascading_offset_polarity: Unset | str = UNSET
        if not isinstance(self.cascading_offset_polarity, Unset):
            cascading_offset_polarity = self.cascading_offset_polarity.value

        cascading_offset_type: Unset | str = UNSET
        if not isinstance(self.cascading_offset_type, Unset):
            cascading_offset_type = self.cascading_offset_type.value

        cascading_source = self.cascading_source

        description = self.description

        due_at = self.due_at

        matter: Unset | dict[str, Any] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        name = self.name

        notify_assignee = self.notify_assignee

        notify_completion = self.notify_completion

        permission: Unset | str = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        priority: Unset | str = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        task_type: Unset | dict[str, Any] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.to_dict()

        time_estimated = self.time_estimated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if cascading is not UNSET:
            field_dict["cascading"] = cascading
        if cascading_offset is not UNSET:
            field_dict["cascading_offset"] = cascading_offset
        if cascading_offset_polarity is not UNSET:
            field_dict["cascading_offset_polarity"] = cascading_offset_polarity
        if cascading_offset_type is not UNSET:
            field_dict["cascading_offset_type"] = cascading_offset_type
        if cascading_source is not UNSET:
            field_dict["cascading_source"] = cascading_source
        if description is not UNSET:
            field_dict["description"] = description
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if matter is not UNSET:
            field_dict["matter"] = matter
        if name is not UNSET:
            field_dict["name"] = name
        if notify_assignee is not UNSET:
            field_dict["notify_assignee"] = notify_assignee
        if notify_completion is not UNSET:
            field_dict["notify_completion"] = notify_completion
        if permission is not UNSET:
            field_dict["permission"] = permission
        if priority is not UNSET:
            field_dict["priority"] = priority
        if status is not UNSET:
            field_dict["status"] = status
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if time_estimated is not UNSET:
            field_dict["time_estimated"] = time_estimated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.taskupdate_data_body_data_assignee import (
            TaskupdateDataBodyDataAssignee,
        )
        from ..models.taskupdate_data_body_data_matter import (
            TaskupdateDataBodyDataMatter,
        )
        from ..models.taskupdate_data_body_data_task_type import (
            TaskupdateDataBodyDataTaskType,
        )

        d = dict(src_dict)
        _assignee = d.pop("assignee", UNSET)
        assignee: Unset | TaskupdateDataBodyDataAssignee
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = TaskupdateDataBodyDataAssignee.from_dict(_assignee)

        cascading = d.pop("cascading", UNSET)

        cascading_offset = d.pop("cascading_offset", UNSET)

        _cascading_offset_polarity = d.pop("cascading_offset_polarity", UNSET)
        cascading_offset_polarity: Unset | TaskupdateDataBodyDataCascadingOffsetPolarity
        if isinstance(_cascading_offset_polarity, Unset):
            cascading_offset_polarity = UNSET
        else:
            cascading_offset_polarity = TaskupdateDataBodyDataCascadingOffsetPolarity(
                _cascading_offset_polarity
            )

        _cascading_offset_type = d.pop("cascading_offset_type", UNSET)
        cascading_offset_type: Unset | TaskupdateDataBodyDataCascadingOffsetType
        if isinstance(_cascading_offset_type, Unset):
            cascading_offset_type = UNSET
        else:
            cascading_offset_type = TaskupdateDataBodyDataCascadingOffsetType(
                _cascading_offset_type
            )

        cascading_source = d.pop("cascading_source", UNSET)

        description = d.pop("description", UNSET)

        due_at = d.pop("due_at", UNSET)

        _matter = d.pop("matter", UNSET)
        matter: Unset | TaskupdateDataBodyDataMatter
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = TaskupdateDataBodyDataMatter.from_dict(_matter)

        name = d.pop("name", UNSET)

        notify_assignee = d.pop("notify_assignee", UNSET)

        notify_completion = d.pop("notify_completion", UNSET)

        _permission = d.pop("permission", UNSET)
        permission: Unset | TaskupdateDataBodyDataPermission
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = TaskupdateDataBodyDataPermission(_permission)

        _priority = d.pop("priority", UNSET)
        priority: Unset | TaskupdateDataBodyDataPriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = TaskupdateDataBodyDataPriority(_priority)

        _status = d.pop("status", UNSET)
        status: Unset | TaskupdateDataBodyDataStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskupdateDataBodyDataStatus(_status)

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | TaskupdateDataBodyDataTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = TaskupdateDataBodyDataTaskType.from_dict(_task_type)

        time_estimated = d.pop("time_estimated", UNSET)

        taskupdate_data_body_data = cls(
            assignee=assignee,
            cascading=cascading,
            cascading_offset=cascading_offset,
            cascading_offset_polarity=cascading_offset_polarity,
            cascading_offset_type=cascading_offset_type,
            cascading_source=cascading_source,
            description=description,
            due_at=due_at,
            matter=matter,
            name=name,
            notify_assignee=notify_assignee,
            notify_completion=notify_completion,
            permission=permission,
            priority=priority,
            status=status,
            task_type=task_type,
            time_estimated=time_estimated,
        )

        taskupdate_data_body_data.additional_properties = d
        return taskupdate_data_body_data

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
