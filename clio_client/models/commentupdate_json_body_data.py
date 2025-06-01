from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commentupdate_json_body_data_item import CommentupdateJsonBodyDataItem


T = TypeVar("T", bound="CommentupdateJsonBodyData")


@_attrs_define
class CommentupdateJsonBodyData:
    """
    Attributes:
        item (Union[Unset, CommentupdateJsonBodyDataItem]):
        message (Union[Unset, str]): The content of the Comment.
    """

    item: Union[Unset, "CommentupdateJsonBodyDataItem"] = UNSET
    message: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item: Unset | dict[str, Any] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item is not UNSET:
            field_dict["item"] = item
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commentupdate_json_body_data_item import (
            CommentupdateJsonBodyDataItem,
        )

        d = dict(src_dict)
        _item = d.pop("item", UNSET)
        item: Unset | CommentupdateJsonBodyDataItem
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = CommentupdateJsonBodyDataItem.from_dict(_item)

        message = d.pop("message", UNSET)

        commentupdate_json_body_data = cls(
            item=item,
            message=message,
        )

        commentupdate_json_body_data.additional_properties = d
        return commentupdate_json_body_data

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
