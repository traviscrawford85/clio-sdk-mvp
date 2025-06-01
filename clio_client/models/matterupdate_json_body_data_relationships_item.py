from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matterupdate_json_body_data_relationships_item_contact import (
        MatterupdateJsonBodyDataRelationshipsItemContact,
    )


T = TypeVar("T", bound="MatterupdateJsonBodyDataRelationshipsItem")


@_attrs_define
class MatterupdateJsonBodyDataRelationshipsItem:
    """
    Attributes:
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated Relationship is present, the Relationship is deleted from the Matter.
        contact (Union[Unset, MatterupdateJsonBodyDataRelationshipsItemContact]):
        description (Union[Unset, str]): Describe the relationship between a Contact and a Matter.
        id (Union[Unset, int]): The unique identifier for a single Relationship associated with the Matter. The keyword
            `null` is not valid for this field.
    """

    field_destroy: Unset | bool = UNSET
    contact: Union[Unset, "MatterupdateJsonBodyDataRelationshipsItemContact"] = UNSET
    description: Unset | str = UNSET
    id: Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_destroy = self.field_destroy

        contact: Unset | dict[str, Any] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        description = self.description

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if contact is not UNSET:
            field_dict["contact"] = contact
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matterupdate_json_body_data_relationships_item_contact import (
            MatterupdateJsonBodyDataRelationshipsItemContact,
        )

        d = dict(src_dict)
        field_destroy = d.pop("_destroy", UNSET)

        _contact = d.pop("contact", UNSET)
        contact: Unset | MatterupdateJsonBodyDataRelationshipsItemContact
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = MatterupdateJsonBodyDataRelationshipsItemContact.from_dict(
                _contact
            )

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        matterupdate_json_body_data_relationships_item = cls(
            field_destroy=field_destroy,
            contact=contact,
            description=description,
            id=id,
        )

        matterupdate_json_body_data_relationships_item.additional_properties = d
        return matterupdate_json_body_data_relationships_item

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
