from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_value_base_field_type import CustomFieldValueBaseFieldType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact import ClioContact
    from ..models.custom_field import CustomField
    from ..models.custom_field_value_extended_matter import (
        CustomFieldValueExtendedMatter,
    )
    from ..models.picklist_option import PicklistOption


T = TypeVar("T", bound="CustomFieldValue")


@_attrs_define
class CustomFieldValue:
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
        custom_field (Union[Unset, CustomField]):
        picklist_option (Union[Unset, PicklistOption]):
        matter (Union[Unset, CustomFieldValueExtendedMatter]):
        contact (Union[Unset, ClioContact]):
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
    custom_field: Union[Unset, "CustomField"] = UNSET
    picklist_option: Union[Unset, "PicklistOption"] = UNSET
    matter: Union[Unset, "CustomFieldValueExtendedMatter"] = UNSET
    contact: Union[Unset, "ClioContact"] = UNSET
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

        custom_field: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_field, Unset):
            custom_field = self.custom_field.to_dict()

        picklist_option: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.picklist_option, Unset):
            picklist_option = self.picklist_option.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

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
        if custom_field is not UNSET:
            field_dict["custom_field"] = custom_field
        if picklist_option is not UNSET:
            field_dict["picklist_option"] = picklist_option
        if matter is not UNSET:
            field_dict["matter"] = matter
        if contact is not UNSET:
            field_dict["contact"] = contact

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact import ClioContact
        from ..models.custom_field import CustomField
        from ..models.custom_field_value_extended_matter import (
            CustomFieldValueExtendedMatter,
        )
        from ..models.picklist_option import PicklistOption

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

        _custom_field = d.pop("custom_field", UNSET)
        custom_field: Union[Unset, CustomField]
        if isinstance(_custom_field, Unset):
            custom_field = UNSET
        else:
            custom_field = CustomField.from_dict(_custom_field)

        _picklist_option = d.pop("picklist_option", UNSET)
        picklist_option: Union[Unset, PicklistOption]
        if isinstance(_picklist_option, Unset):
            picklist_option = UNSET
        else:
            picklist_option = PicklistOption.from_dict(_picklist_option)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, CustomFieldValueExtendedMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = CustomFieldValueExtendedMatter.from_dict(_matter)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, ClioContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ClioContact.from_dict(_contact)

        custom_field_value = cls(
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
            custom_field=custom_field,
            picklist_option=picklist_option,
            matter=matter,
            contact=contact,
        )

        custom_field_value.additional_properties = d
        return custom_field_value

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
