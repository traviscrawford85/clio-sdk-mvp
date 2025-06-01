from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_base_field_type import CustomFieldBaseFieldType
from ..models.custom_field_base_parent_type import CustomFieldBaseParentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.picklist_option import PicklistOption


T = TypeVar("T", bound="CustomFieldExtended")


@_attrs_define
class CustomFieldExtended:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *CustomField* was created (as a ISO-8601 timestamp)
        deleted (Union[Unset, bool]): Whether the *CustomField* is deleted for future use
        display_order (Union[Unset, int]): The display position of the *CustomField*
        displayed (Union[Unset, bool]): Whether the *CustomField* is displayed by default
        etag (Union[Unset, str]): ETag for the *CustomField*
        field_type (Union[Unset, CustomFieldBaseFieldType]): Field type of the *CustomField*
        id (Union[Unset, int]): Unique identifier for the *CustomField*
        name (Union[Unset, str]): The name of the *CustomField*
        parent_type (Union[Unset, CustomFieldBaseParentType]): Type of object the *CustomField* is for
        required (Union[Unset, bool]): Whether the *CustomField* requires a value
        updated_at (Union[Unset, str]): The time the *CustomField* was last updated (as a ISO-8601 timestamp)
        picklist_options (Union[Unset, list['PicklistOption']]):
    """

    created_at: Unset | str = UNSET
    deleted: Unset | bool = UNSET
    display_order: Unset | int = UNSET
    displayed: Unset | bool = UNSET
    etag: Unset | str = UNSET
    field_type: Unset | CustomFieldBaseFieldType = UNSET
    id: Unset | int = UNSET
    name: Unset | str = UNSET
    parent_type: Unset | CustomFieldBaseParentType = UNSET
    required: Unset | bool = UNSET
    updated_at: Unset | str = UNSET
    picklist_options: Unset | list["PicklistOption"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        deleted = self.deleted

        display_order = self.display_order

        displayed = self.displayed

        etag = self.etag

        field_type: Unset | str = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.value

        id = self.id

        name = self.name

        parent_type: Unset | str = UNSET
        if not isinstance(self.parent_type, Unset):
            parent_type = self.parent_type.value

        required = self.required

        updated_at = self.updated_at

        picklist_options: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.picklist_options, Unset):
            picklist_options = []
            for picklist_options_item_data in self.picklist_options:
                picklist_options_item = picklist_options_item_data.to_dict()
                picklist_options.append(picklist_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if display_order is not UNSET:
            field_dict["display_order"] = display_order
        if displayed is not UNSET:
            field_dict["displayed"] = displayed
        if etag is not UNSET:
            field_dict["etag"] = etag
        if field_type is not UNSET:
            field_dict["field_type"] = field_type
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if parent_type is not UNSET:
            field_dict["parent_type"] = parent_type
        if required is not UNSET:
            field_dict["required"] = required
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if picklist_options is not UNSET:
            field_dict["picklist_options"] = picklist_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.picklist_option import PicklistOption

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        deleted = d.pop("deleted", UNSET)

        display_order = d.pop("display_order", UNSET)

        displayed = d.pop("displayed", UNSET)

        etag = d.pop("etag", UNSET)

        _field_type = d.pop("field_type", UNSET)
        field_type: Unset | CustomFieldBaseFieldType
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = CustomFieldBaseFieldType(_field_type)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _parent_type = d.pop("parent_type", UNSET)
        parent_type: Unset | CustomFieldBaseParentType
        if isinstance(_parent_type, Unset):
            parent_type = UNSET
        else:
            parent_type = CustomFieldBaseParentType(_parent_type)

        required = d.pop("required", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        picklist_options = []
        _picklist_options = d.pop("picklist_options", UNSET)
        for picklist_options_item_data in _picklist_options or []:
            picklist_options_item = PicklistOption.from_dict(picklist_options_item_data)

            picklist_options.append(picklist_options_item)

        custom_field_extended = cls(
            created_at=created_at,
            deleted=deleted,
            display_order=display_order,
            displayed=displayed,
            etag=etag,
            field_type=field_type,
            id=id,
            name=name,
            parent_type=parent_type,
            required=required,
            updated_at=updated_at,
            picklist_options=picklist_options,
        )

        custom_field_extended.additional_properties = d
        return custom_field_extended

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
