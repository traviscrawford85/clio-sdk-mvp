from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DocumentArchivecreateJsonBodyDataItemsItem")


@_attrs_define
class DocumentArchivecreateJsonBodyDataItemsItem:
    """
    Attributes:
        id (int): The unique identifier for a single Document or Folder associated with the DocumentArchive. Use the
            keyword `null` to specify no association.
        type_ (int): The type of the item to download
    """

    id: int
    type_: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        document_archivecreate_json_body_data_items_item = cls(
            id=id,
            type_=type_,
        )

        document_archivecreate_json_body_data_items_item.additional_properties = d
        return document_archivecreate_json_body_data_items_item

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
