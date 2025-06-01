from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_base_priority import TaskBasePriority
from ..models.task_base_status import TaskBaseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClioTask")


@_attrs_define
class ClioTask:
    """
    Attributes:
        data (ClioTask):
        completed_at (Union[Unset, str]): The time the *Task* was completed (as a ISO-8601 timestamp)
        created_at (Union[Unset, str]): The time the *Task* was created (as a ISO-8601 timestamp)
        description (Union[Unset, str]): A detailed description of the *Task*
        due_at (Union[Unset, str]): The date the *Task* is due (as a ISO-8601 date)
        etag (Union[Unset, str]): ETag for the *Task*
        id (Union[Unset, int]): Unique identifier for the *Task*
        name (Union[Unset, str]): The name of the *Task*
        notify_completion (Union[Unset, bool]): Whether to notify the assigner of the task's completion
        permission (Union[Unset, str]): The permission of the *Task*
        priority (Union[Unset, TaskBasePriority]): The priority of the *Task*
        status (Union[Unset, TaskBaseStatus]): Status of the *Task*. (Note that users without advanced tasks can only
            have either complete or pending)
        statute_of_limitations (Union[Unset, bool]): Whether the task is a statute of limitations
        time_entries_count (Union[Unset, int]): The number of time entries associated with this task
        time_estimated (Union[Unset, int]): Time the *Task* should take to complete
        updated_at (Union[Unset, str]): The time the *Task* was last updated (as a ISO-8601 timestamp)
    """

    data: "ClioTask"
    completed_at: Unset | str = UNSET
    created_at: Unset | str = UNSET
    description: Unset | str = UNSET
    due_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    name: Unset | str = UNSET
    notify_completion: Unset | bool = UNSET
    permission: Unset | str = UNSET
    priority: Unset | TaskBasePriority = UNSET
    status: Unset | TaskBaseStatus = UNSET
    statute_of_limitations: Unset | bool = UNSET
    time_entries_count: Unset | int = UNSET
    time_estimated: Unset | int = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        completed_at = self.completed_at

        created_at = self.created_at

        description = self.description

        due_at = self.due_at

        etag = self.etag

        id = self.id

        name = self.name

        notify_completion = self.notify_completion

        permission = self.permission

        priority: Unset | str = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        statute_of_limitations = self.statute_of_limitations

        time_entries_count = self.time_entries_count

        time_estimated = self.time_estimated

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
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
        if time_entries_count is not UNSET:
            field_dict["time_entries_count"] = time_entries_count
        if time_estimated is not UNSET:
            field_dict["time_estimated"] = time_estimated
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = ClioTask.from_dict(d.pop("data"))

        completed_at = d.pop("completed_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        due_at = d.pop("due_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        notify_completion = d.pop("notify_completion", UNSET)

        permission = d.pop("permission", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Unset | TaskBasePriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = TaskBasePriority(_priority)

        _status = d.pop("status", UNSET)
        status: Unset | TaskBaseStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskBaseStatus(_status)

        statute_of_limitations = d.pop("statute_of_limitations", UNSET)

        time_entries_count = d.pop("time_entries_count", UNSET)

        time_estimated = d.pop("time_estimated", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        task = cls(
            data=data,
            completed_at=completed_at,
            created_at=created_at,
            description=description,
            due_at=due_at,
            etag=etag,
            id=id,
            name=name,
            notify_completion=notify_completion,
            permission=permission,
            priority=priority,
            status=status,
            statute_of_limitations=statute_of_limitations,
            time_entries_count=time_entries_count,
            time_estimated=time_estimated,
            updated_at=updated_at,
        )

        task.additional_properties = d
        return task

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
