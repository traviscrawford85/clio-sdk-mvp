from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskTemplateListBase")


@_attrs_define
class TaskTemplateListBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *TaskTemplateList* was created (as a ISO-8601 timestamp)
        description (Union[Unset, str]): A detailed description of the *TaskTemplateList*
        etag (Union[Unset, str]): ETag for the *TaskTemplateList*
        id (Union[Unset, int]): Unique identifier for the *TaskTemplateList*
        name (Union[Unset, str]): The name of the *TaskTemplateList*
        templates_count (Union[Unset, int]): How many task templates exist as an association to the *TaskTemplateList*
        updated_at (Union[Unset, str]): The time the *TaskTemplateList* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    templates_count: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        description = self.description

        etag = self.etag

        id = self.id

        name = self.name

        templates_count = self.templates_count

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
        if templates_count is not UNSET:
            field_dict["templates_count"] = templates_count
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

        templates_count = d.pop("templates_count", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        task_template_list_base = cls(
            created_at=created_at,
            description=description,
            etag=etag,
            id=id,
            name=name,
            templates_count=templates_count,
            updated_at=updated_at,
        )

        task_template_list_base.additional_properties = d
        return task_template_list_base

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
