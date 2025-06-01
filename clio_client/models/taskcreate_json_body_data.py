from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.taskcreate_json_body_data_cascading_offset_polarity import (
    TaskcreateJsonBodyDataCascadingOffsetPolarity,
)
from ..models.taskcreate_json_body_data_cascading_offset_type import (
    TaskcreateJsonBodyDataCascadingOffsetType,
)
from ..models.taskcreate_json_body_data_permission import (
    TaskcreateJsonBodyDataPermission,
)
from ..models.taskcreate_json_body_data_priority import TaskcreateJsonBodyDataPriority
from ..models.taskcreate_json_body_data_status import TaskcreateJsonBodyDataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.taskcreate_json_body_data_assignee import (
        TaskcreateJsonBodyDataAssignee,
    )
    from ..models.taskcreate_json_body_data_matter import TaskcreateJsonBodyDataMatter
    from ..models.taskcreate_json_body_data_task_type import (
        TaskcreateJsonBodyDataTaskType,
    )


T = TypeVar("T", bound="TaskcreateJsonBodyData")


@_attrs_define
class TaskcreateJsonBodyData:
    """
    Attributes:
        assignee (TaskcreateJsonBodyDataAssignee):
        description (str): Longer description of the Task.
        name (str): Name of the Task.
        cascading (Union[Unset, bool]): Determines if the Task has a due date that is derived from another Task. (Note
            that if false, no other cascading information will be checked)
        cascading_offset (Union[Unset, int]): The amount of time that will differentiate the cascaded Task from its
            parent.
        cascading_offset_polarity (Union[Unset, TaskcreateJsonBodyDataCascadingOffsetPolarity]): Determines whether or
            not the cascading_offset occurs before or after its parent.
        cascading_offset_type (Union[Unset, TaskcreateJsonBodyDataCascadingOffsetType]): Determines the quantity of the
            cascading offset (e.g. CalendarDays, CalendarWeeks etc.)
        cascading_source (Union[Unset, int]): The parent Task that is used to determine the due_at property of the
            cascaded Task
        due_at (Union[Unset, str]): Date when the Task must be completed by. (Expects an ISO-8601 date).
        matter (Union[Unset, TaskcreateJsonBodyDataMatter]):
        notify_assignee (Union[Unset, bool]): Whether or not the Task should notify the assignee on creation.
        notify_completion (Union[Unset, bool]): Whether or not the Task should notify the assigner on completion.
        permission (Union[Unset, TaskcreateJsonBodyDataPermission]): Permission of the Task. Defaults to `public`
            Default: TaskcreateJsonBodyDataPermission.PUBLIC.
        priority (Union[Unset, TaskcreateJsonBodyDataPriority]): Priority of the Task. Default:
            TaskcreateJsonBodyDataPriority.NORMAL.
        status (Union[Unset, TaskcreateJsonBodyDataStatus]): Task status. Users without advanced tasks are allowed to
            select `Complete` or `Pending` only. Default: TaskcreateJsonBodyDataStatus.PENDING.
        statute_of_limitations (Union[Unset, bool]): Whether or not the Task should be a statute of limitations.
        task_type (Union[Unset, TaskcreateJsonBodyDataTaskType]):
        time_estimated (Union[Unset, int]): Time the Task should take to complete.
    """

    assignee: "TaskcreateJsonBodyDataAssignee"
    description: str
    name: str
    cascading: Unset | bool = UNSET
    cascading_offset: Unset | int = UNSET
    cascading_offset_polarity: Unset | TaskcreateJsonBodyDataCascadingOffsetPolarity = (
        UNSET
    )
    cascading_offset_type: Unset | TaskcreateJsonBodyDataCascadingOffsetType = UNSET
    cascading_source: Unset | int = UNSET
    due_at: Unset | str = UNSET
    matter: Union[Unset, "TaskcreateJsonBodyDataMatter"] = UNSET
    notify_assignee: Unset | bool = UNSET
    notify_completion: Unset | bool = UNSET
    permission: Unset | TaskcreateJsonBodyDataPermission = (
        TaskcreateJsonBodyDataPermission.PUBLIC
    )
    priority: Unset | TaskcreateJsonBodyDataPriority = (
        TaskcreateJsonBodyDataPriority.NORMAL
    )
    status: Unset | TaskcreateJsonBodyDataStatus = TaskcreateJsonBodyDataStatus.PENDING
    statute_of_limitations: Unset | bool = UNSET
    task_type: Union[Unset, "TaskcreateJsonBodyDataTaskType"] = UNSET
    time_estimated: Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignee = self.assignee.to_dict()

        description = self.description

        name = self.name

        cascading = self.cascading

        cascading_offset = self.cascading_offset

        cascading_offset_polarity: Unset | str = UNSET
        if not isinstance(self.cascading_offset_polarity, Unset):
            cascading_offset_polarity = self.cascading_offset_polarity.value

        cascading_offset_type: Unset | str = UNSET
        if not isinstance(self.cascading_offset_type, Unset):
            cascading_offset_type = self.cascading_offset_type.value

        cascading_source = self.cascading_source

        due_at = self.due_at

        matter: Unset | dict[str, Any] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

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

        statute_of_limitations = self.statute_of_limitations

        task_type: Unset | dict[str, Any] = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type.to_dict()

        time_estimated = self.time_estimated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignee": assignee,
                "description": description,
                "name": name,
            }
        )
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
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if matter is not UNSET:
            field_dict["matter"] = matter
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
        if statute_of_limitations is not UNSET:
            field_dict["statute_of_limitations"] = statute_of_limitations
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if time_estimated is not UNSET:
            field_dict["time_estimated"] = time_estimated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.taskcreate_json_body_data_assignee import (
            TaskcreateJsonBodyDataAssignee,
        )
        from ..models.taskcreate_json_body_data_matter import (
            TaskcreateJsonBodyDataMatter,
        )
        from ..models.taskcreate_json_body_data_task_type import (
            TaskcreateJsonBodyDataTaskType,
        )

        d = dict(src_dict)
        assignee = TaskcreateJsonBodyDataAssignee.from_dict(d.pop("assignee"))

        description = d.pop("description")

        name = d.pop("name")

        cascading = d.pop("cascading", UNSET)

        cascading_offset = d.pop("cascading_offset", UNSET)

        _cascading_offset_polarity = d.pop("cascading_offset_polarity", UNSET)
        cascading_offset_polarity: Unset | TaskcreateJsonBodyDataCascadingOffsetPolarity
        if isinstance(_cascading_offset_polarity, Unset):
            cascading_offset_polarity = UNSET
        else:
            cascading_offset_polarity = TaskcreateJsonBodyDataCascadingOffsetPolarity(
                _cascading_offset_polarity
            )

        _cascading_offset_type = d.pop("cascading_offset_type", UNSET)
        cascading_offset_type: Unset | TaskcreateJsonBodyDataCascadingOffsetType
        if isinstance(_cascading_offset_type, Unset):
            cascading_offset_type = UNSET
        else:
            cascading_offset_type = TaskcreateJsonBodyDataCascadingOffsetType(
                _cascading_offset_type
            )

        cascading_source = d.pop("cascading_source", UNSET)

        due_at = d.pop("due_at", UNSET)

        _matter = d.pop("matter", UNSET)
        matter: Unset | TaskcreateJsonBodyDataMatter
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = TaskcreateJsonBodyDataMatter.from_dict(_matter)

        notify_assignee = d.pop("notify_assignee", UNSET)

        notify_completion = d.pop("notify_completion", UNSET)

        _permission = d.pop("permission", UNSET)
        permission: Unset | TaskcreateJsonBodyDataPermission
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = TaskcreateJsonBodyDataPermission(_permission)

        _priority = d.pop("priority", UNSET)
        priority: Unset | TaskcreateJsonBodyDataPriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = TaskcreateJsonBodyDataPriority(_priority)

        _status = d.pop("status", UNSET)
        status: Unset | TaskcreateJsonBodyDataStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskcreateJsonBodyDataStatus(_status)

        statute_of_limitations = d.pop("statute_of_limitations", UNSET)

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | TaskcreateJsonBodyDataTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = TaskcreateJsonBodyDataTaskType.from_dict(_task_type)

        time_estimated = d.pop("time_estimated", UNSET)

        taskcreate_json_body_data = cls(
            assignee=assignee,
            description=description,
            name=name,
            cascading=cascading,
            cascading_offset=cascading_offset,
            cascading_offset_polarity=cascading_offset_polarity,
            cascading_offset_type=cascading_offset_type,
            cascading_source=cascading_source,
            due_at=due_at,
            matter=matter,
            notify_assignee=notify_assignee,
            notify_completion=notify_completion,
            permission=permission,
            priority=priority,
            status=status,
            statute_of_limitations=statute_of_limitations,
            task_type=task_type,
            time_estimated=time_estimated,
        )

        taskcreate_json_body_data.additional_properties = d
        return taskcreate_json_body_data

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
