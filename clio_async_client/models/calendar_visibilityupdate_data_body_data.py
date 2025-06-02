from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calendar_visibilityupdate_data_body_data_color import (
    CalendarVisibilityupdateDataBodyDataColor,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarVisibilityupdateDataBodyData")


@_attrs_define
class CalendarVisibilityupdateDataBodyData:
    """
    Attributes:
        color (Union[Unset, CalendarVisibilityupdateDataBodyDataColor]): Calendar color as seen in the Clio Web UI.
        visible (Union[Unset, str]): Whether or not the CalendarVisibility should be visible by default in the Clio Web
            UI.
    """

    color: Union[Unset, CalendarVisibilityupdateDataBodyDataColor] = UNSET
    visible: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color: Union[Unset, str] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        visible = self.visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _color = d.pop("color", UNSET)
        color: Union[Unset, CalendarVisibilityupdateDataBodyDataColor]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = CalendarVisibilityupdateDataBodyDataColor(_color)

        visible = d.pop("visible", UNSET)

        calendar_visibilityupdate_data_body_data = cls(
            color=color,
            visible=visible,
        )

        calendar_visibilityupdate_data_body_data.additional_properties = d
        return calendar_visibilityupdate_data_body_data

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
