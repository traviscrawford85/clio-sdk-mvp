from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_value_base_field_type import CustomFieldValueBaseFieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldValueBase")


@_attrs_define
class CustomFieldValueBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *CustomFieldValue* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *CustomFieldValue*
        field_display_order (Union[Unset, int]): The display position of the *CustomFieldValue*
        field_displayed (Union[Unset, bool]): Whether the *CustomFieldValue* is displayed by default
        field_name (Union[Unset, str]): The name of the custom field
        field_required (Union[Unset, bool]): Whether the *CustomFieldValue* requires a value
        field_type (Union[Unset, CustomFieldValueBaseFieldType]): The type of the *CustomFieldValue*
        id (Union[Unset, str]): Unique identifier for the *CustomFieldValue*
        soft_deleted (Union[Unset, bool]): Whether the value is associated with a deleted custom field
        updated_at (Union[Unset, str]): The time the *CustomFieldValue* was last updated (as a ISO-8601 timestamp)
        value (Union[Unset, str]): The value of the *CustomFieldValue*
    """

    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    field_display_order: Union[Unset, int] = UNSET
    field_displayed: Union[Unset, bool] = UNSET
    field_name: Union[Unset, str] = UNSET
    field_required: Union[Unset, bool] = UNSET
    field_type: Union[Unset, CustomFieldValueBaseFieldType] = UNSET
    id: Union[Unset, str] = UNSET
    soft_deleted: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        etag = self.etag

        field_display_order = self.field_display_order

        field_displayed = self.field_displayed

        field_name = self.field_name

        field_required = self.field_required

        field_type: Union[Unset, str] = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.value

        id = self.id

        soft_deleted = self.soft_deleted

        updated_at = self.updated_at

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if field_display_order is not UNSET:
            field_dict["field_display_order"] = field_display_order
        if field_displayed is not UNSET:
            field_dict["field_displayed"] = field_displayed
        if field_name is not UNSET:
            field_dict["field_name"] = field_name
        if field_required is not UNSET:
            field_dict["field_required"] = field_required
        if field_type is not UNSET:
            field_dict["field_type"] = field_type
        if id is not UNSET:
            field_dict["id"] = id
        if soft_deleted is not UNSET:
            field_dict["soft_deleted"] = soft_deleted
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        field_display_order = d.pop("field_display_order", UNSET)

        field_displayed = d.pop("field_displayed", UNSET)

        field_name = d.pop("field_name", UNSET)

        field_required = d.pop("field_required", UNSET)

        _field_type = d.pop("field_type", UNSET)
        field_type: Union[Unset, CustomFieldValueBaseFieldType]
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = CustomFieldValueBaseFieldType(_field_type)

        id = d.pop("id", UNSET)

        soft_deleted = d.pop("soft_deleted", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        value = d.pop("value", UNSET)

        custom_field_value_base = cls(
            created_at=created_at,
            etag=etag,
            field_display_order=field_display_order,
            field_displayed=field_displayed,
            field_name=field_name,
            field_required=field_required,
            field_type=field_type,
            id=id,
            soft_deleted=soft_deleted,
            updated_at=updated_at,
            value=value,
        )

        custom_field_value_base.additional_properties = d
        return custom_field_value_base

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
