from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calendar_entryupdate_files_body_data_conference_meeting_type import (
    CalendarEntryupdateFilesBodyDataConferenceMeetingType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarEntryupdateFilesBodyDataConferenceMeeting")


@_attrs_define
class CalendarEntryupdateFilesBodyDataConferenceMeeting:
    """
    Attributes:
        type_ (Union[Unset, CalendarEntryupdateFilesBodyDataConferenceMeetingType]): The type of conference meeting. If
            no conference meeting is present or the user is in an ineligible pricing tier for this feature, it will be null.
    """

    type_: Unset | CalendarEntryupdateFilesBodyDataConferenceMeetingType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Unset | CalendarEntryupdateFilesBodyDataConferenceMeetingType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CalendarEntryupdateFilesBodyDataConferenceMeetingType(_type_)

        calendar_entryupdate_files_body_data_conference_meeting = cls(
            type_=type_,
        )

        calendar_entryupdate_files_body_data_conference_meeting.additional_properties = d
        return calendar_entryupdate_files_body_data_conference_meeting

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
