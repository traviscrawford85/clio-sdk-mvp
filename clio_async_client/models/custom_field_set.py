from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_set_base_parent_type import CustomFieldSetBaseParentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_base import CustomFieldBase


T = TypeVar("T", bound="CustomFieldSet")


@_attrs_define
class CustomFieldSet:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *CustomFieldSet* was created (as a ISO-8601 timestamp)
        displayed (Union[Unset, bool]): Whether or not the *CustomFieldSet* should be displayed by default.
        etag (Union[Unset, str]): ETag for the *CustomFieldSet*
        id (Union[Unset, int]): Unique identifier for the *CustomFieldSet*
        name (Union[Unset, str]): The name of the custom field set.
        parent_type (Union[Unset, CustomFieldSetBaseParentType]): Type of object the *CustomFieldSet* is for.
        updated_at (Union[Unset, str]): The time the *CustomFieldSet* was last updated (as a ISO-8601 timestamp)
        custom_fields (Union[Unset, list['CustomFieldBase']]): CustomField
    """

    created_at: Union[Unset, str] = UNSET
    displayed: Union[Unset, bool] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    parent_type: Union[Unset, CustomFieldSetBaseParentType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, list["CustomFieldBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        displayed = self.displayed

        etag = self.etag

        id = self.id

        name = self.name

        parent_type: Union[Unset, str] = UNSET
        if not isinstance(self.parent_type, Unset):
            parent_type = self.parent_type.value

        updated_at = self.updated_at

        custom_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if displayed is not UNSET:
            field_dict["displayed"] = displayed
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if parent_type is not UNSET:
            field_dict["parent_type"] = parent_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_base import CustomFieldBase

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        displayed = d.pop("displayed", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _parent_type = d.pop("parent_type", UNSET)
        parent_type: Union[Unset, CustomFieldSetBaseParentType]
        if isinstance(_parent_type, Unset):
            parent_type = UNSET
        else:
            parent_type = CustomFieldSetBaseParentType(_parent_type)

        updated_at = d.pop("updated_at", UNSET)

        custom_fields = []
        _custom_fields = d.pop("custom_fields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = CustomFieldBase.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        custom_field_set = cls(
            created_at=created_at,
            displayed=displayed,
            etag=etag,
            id=id,
            name=name,
            parent_type=parent_type,
            updated_at=updated_at,
            custom_fields=custom_fields,
        )

        custom_field_set.additional_properties = d
        return custom_field_set

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
