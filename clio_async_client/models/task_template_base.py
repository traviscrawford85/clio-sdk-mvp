from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_template_base_priority import TaskTemplateBasePriority
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskTemplateBase")


@_attrs_define
class TaskTemplateBase:
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
    """

    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    priority: Union[Unset, TaskTemplateBasePriority] = UNSET
    private: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        task_template_base = cls(
            created_at=created_at,
            description=description,
            etag=etag,
            id=id,
            name=name,
            priority=priority,
            private=private,
            updated_at=updated_at,
        )

        task_template_base.additional_properties = d
        return task_template_base

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
