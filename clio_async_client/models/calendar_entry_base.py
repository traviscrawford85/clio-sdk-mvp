from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarEntryBase")


@_attrs_define
class CalendarEntryBase:
    """
    Attributes:
        all_day (Union[Unset, bool]): Whether the event is all day
        calendar_owner_id (Union[Unset, int]): The id of the calendar owner.
        court_rule (Union[Unset, bool]): Whether this event is associated with a Court Rule
        created_at (Union[Unset, str]): The time the *CalendarEntry* was created (as a ISO-8601 timestamp)
        description (Union[Unset, str]): A detailed description of the *CalendarEntry*
        end_at (Union[Unset, str]): The time the *CalendarEntry* ends (as an ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *CalendarEntry*
        id (Union[Unset, str]): Unique identifier for the *CalendarEntry*
        location (Union[Unset, str]): The geographic location of the *CalendarEntry*
        parent_calendar_entry_id (Union[Unset, int]): Identifier for the parent *CalendarEntry*
        permission (Union[Unset, str]): The view permission for the current user, will return 'viewer' when permission
            is 'limited_viewer' and the user is an attendee.
        recurrence_rule (Union[Unset, str]): Recurrence rule for expanding
        start_at (Union[Unset, str]): The time the *CalendarEntry* starts (as an ISO-8601 timestamp)
        start_at_time_zone (Union[Unset, str]): Original start at time zone of the event.
        summary (Union[Unset, str]): A short summary of the *CalendarEntry*
        time_entries_count (Union[Unset, int]): The number of `TimeEntry` activities associated with the *CalendarEntry*
        updated_at (Union[Unset, str]): The time the *CalendarEntry* was last updated (as a ISO-8601 timestamp)
    """

    all_day: Union[Unset, bool] = UNSET
    calendar_owner_id: Union[Unset, int] = UNSET
    court_rule: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    end_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    parent_calendar_entry_id: Union[Unset, int] = UNSET
    permission: Union[Unset, str] = UNSET
    recurrence_rule: Union[Unset, str] = UNSET
    start_at: Union[Unset, str] = UNSET
    start_at_time_zone: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    time_entries_count: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_day = self.all_day

        calendar_owner_id = self.calendar_owner_id

        court_rule = self.court_rule

        created_at = self.created_at

        description = self.description

        end_at = self.end_at

        etag = self.etag

        id = self.id

        location = self.location

        parent_calendar_entry_id = self.parent_calendar_entry_id

        permission = self.permission

        recurrence_rule = self.recurrence_rule

        start_at = self.start_at

        start_at_time_zone = self.start_at_time_zone

        summary = self.summary

        time_entries_count = self.time_entries_count

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_day is not UNSET:
            field_dict["all_day"] = all_day
        if calendar_owner_id is not UNSET:
            field_dict["calendar_owner_id"] = calendar_owner_id
        if court_rule is not UNSET:
            field_dict["court_rule"] = court_rule
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if location is not UNSET:
            field_dict["location"] = location
        if parent_calendar_entry_id is not UNSET:
            field_dict["parent_calendar_entry_id"] = parent_calendar_entry_id
        if permission is not UNSET:
            field_dict["permission"] = permission
        if recurrence_rule is not UNSET:
            field_dict["recurrence_rule"] = recurrence_rule
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if start_at_time_zone is not UNSET:
            field_dict["start_at_time_zone"] = start_at_time_zone
        if summary is not UNSET:
            field_dict["summary"] = summary
        if time_entries_count is not UNSET:
            field_dict["time_entries_count"] = time_entries_count
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_day = d.pop("all_day", UNSET)

        calendar_owner_id = d.pop("calendar_owner_id", UNSET)

        court_rule = d.pop("court_rule", UNSET)

        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        end_at = d.pop("end_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        location = d.pop("location", UNSET)

        parent_calendar_entry_id = d.pop("parent_calendar_entry_id", UNSET)

        permission = d.pop("permission", UNSET)

        recurrence_rule = d.pop("recurrence_rule", UNSET)

        start_at = d.pop("start_at", UNSET)

        start_at_time_zone = d.pop("start_at_time_zone", UNSET)

        summary = d.pop("summary", UNSET)

        time_entries_count = d.pop("time_entries_count", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        calendar_entry_base = cls(
            all_day=all_day,
            calendar_owner_id=calendar_owner_id,
            court_rule=court_rule,
            created_at=created_at,
            description=description,
            end_at=end_at,
            etag=etag,
            id=id,
            location=location,
            parent_calendar_entry_id=parent_calendar_entry_id,
            permission=permission,
            recurrence_rule=recurrence_rule,
            start_at=start_at,
            start_at_time_zone=start_at_time_zone,
            summary=summary,
            time_entries_count=time_entries_count,
            updated_at=updated_at,
        )

        calendar_entry_base.additional_properties = d
        return calendar_entry_base

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
