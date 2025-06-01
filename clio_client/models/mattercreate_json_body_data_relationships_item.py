from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mattercreate_json_body_data_relationships_item_contact import (
        MattercreateJsonBodyDataRelationshipsItemContact,
    )


T = TypeVar("T", bound="MattercreateJsonBodyDataRelationshipsItem")


@_attrs_define
class MattercreateJsonBodyDataRelationshipsItem:
    """
    Attributes:
        contact (MattercreateJsonBodyDataRelationshipsItemContact):
        description (str): Describe the relationship between a Contact and a Matter.
    """

    contact: "MattercreateJsonBodyDataRelationshipsItemContact"
    description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact = self.contact.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contact": contact,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mattercreate_json_body_data_relationships_item_contact import (
            MattercreateJsonBodyDataRelationshipsItemContact,
        )

        d = dict(src_dict)
        contact = MattercreateJsonBodyDataRelationshipsItemContact.from_dict(
            d.pop("contact")
        )

        description = d.pop("description")

        mattercreate_json_body_data_relationships_item = cls(
            contact=contact,
            description=description,
        )

        mattercreate_json_body_data_relationships_item.additional_properties = d
        return mattercreate_json_body_data_relationships_item

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
