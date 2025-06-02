from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mattercreate_data_body_data_custom_field_values_item_custom_field import (
        MattercreateDataBodyDataCustomFieldValuesItemCustomField,
    )


T = TypeVar("T", bound="MattercreateDataBodyDataCustomFieldValuesItem")


@_attrs_define
class MattercreateDataBodyDataCustomFieldValuesItem:
    """
    Attributes:
        custom_field (MattercreateDataBodyDataCustomFieldValuesItemCustomField):
        value (str): The value of the CustomFieldValue.
    """

    custom_field: "MattercreateDataBodyDataCustomFieldValuesItemCustomField"
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_field = self.custom_field.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_field": custom_field,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mattercreate_data_body_data_custom_field_values_item_custom_field import (
            MattercreateDataBodyDataCustomFieldValuesItemCustomField,
        )

        d = dict(src_dict)
        custom_field = MattercreateDataBodyDataCustomFieldValuesItemCustomField.from_dict(d.pop("custom_field"))

        value = d.pop("value")

        mattercreate_data_body_data_custom_field_values_item = cls(
            custom_field=custom_field,
            value=value,
        )

        mattercreate_data_body_data_custom_field_values_item.additional_properties = d
        return mattercreate_data_body_data_custom_field_values_item

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
