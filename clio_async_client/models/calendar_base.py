from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calendar_base_color import CalendarBaseColor
from ..models.calendar_base_light_color import CalendarBaseLightColor
from ..models.calendar_base_permission import CalendarBasePermission
from ..models.calendar_base_source import CalendarBaseSource
from ..models.calendar_base_type import CalendarBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarBase")


@_attrs_define
class CalendarBase:
    """
    Attributes:
        color (Union[Unset, CalendarBaseColor]): Color
        court_rules_default_calendar (Union[Unset, bool]): Whether the calendar is default court rules calendar for
            current user
        created_at (Union[Unset, str]): The time the *Calendar* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *Calendar*
        id (Union[Unset, int]): Unique identifier for the *Calendar*
        light_color (Union[Unset, CalendarBaseLightColor]): Accent color to complement the main calendar color.
        name (Union[Unset, str]): The name of the *Calendar*
        permission (Union[Unset, CalendarBasePermission]): The user's permission to the *Calendar*
        source (Union[Unset, CalendarBaseSource]): The source that visible applies to, by default the Clio Web UI
            (Expects 'mobile' or 'web').
        type_ (Union[Unset, CalendarBaseType]): The type of the *Calendar*
        updated_at (Union[Unset, str]): The time the *Calendar* was last updated (as a ISO-8601 timestamp)
        visible (Union[Unset, bool]): Whether the *Calendar* will be shown by default in the Clio Web UI (assuming no
            source is provided).
    """

    color: Union[Unset, CalendarBaseColor] = UNSET
    court_rules_default_calendar: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    light_color: Union[Unset, CalendarBaseLightColor] = UNSET
    name: Union[Unset, str] = UNSET
    permission: Union[Unset, CalendarBasePermission] = UNSET
    source: Union[Unset, CalendarBaseSource] = UNSET
    type_: Union[Unset, CalendarBaseType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    visible: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color: Union[Unset, str] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        court_rules_default_calendar = self.court_rules_default_calendar

        created_at = self.created_at

        etag = self.etag

        id = self.id

        light_color: Union[Unset, str] = UNSET
        if not isinstance(self.light_color, Unset):
            light_color = self.light_color.value

        name = self.name

        permission: Union[Unset, str] = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        visible = self.visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if court_rules_default_calendar is not UNSET:
            field_dict["court_rules_default_calendar"] = court_rules_default_calendar
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if light_color is not UNSET:
            field_dict["light_color"] = light_color
        if name is not UNSET:
            field_dict["name"] = name
        if permission is not UNSET:
            field_dict["permission"] = permission
        if source is not UNSET:
            field_dict["source"] = source
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _color = d.pop("color", UNSET)
        color: Union[Unset, CalendarBaseColor]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = CalendarBaseColor(_color)

        court_rules_default_calendar = d.pop("court_rules_default_calendar", UNSET)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        _light_color = d.pop("light_color", UNSET)
        light_color: Union[Unset, CalendarBaseLightColor]
        if isinstance(_light_color, Unset):
            light_color = UNSET
        else:
            light_color = CalendarBaseLightColor(_light_color)

        name = d.pop("name", UNSET)

        _permission = d.pop("permission", UNSET)
        permission: Union[Unset, CalendarBasePermission]
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = CalendarBasePermission(_permission)

        _source = d.pop("source", UNSET)
        source: Union[Unset, CalendarBaseSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = CalendarBaseSource(_source)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CalendarBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CalendarBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        visible = d.pop("visible", UNSET)

        calendar_base = cls(
            color=color,
            court_rules_default_calendar=court_rules_default_calendar,
            created_at=created_at,
            etag=etag,
            id=id,
            light_color=light_color,
            name=name,
            permission=permission,
            source=source,
            type_=type_,
            updated_at=updated_at,
            visible=visible,
        )

        calendar_base.additional_properties = d
        return calendar_base

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
