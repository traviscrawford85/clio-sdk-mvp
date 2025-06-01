from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_base import ActivityBase
    from ..models.attendee_base import AttendeeBase
    from ..models.calendar_base import CalendarBase
    from ..models.calendar_entry_calendar_entry_event_type import (
        CalendarEntryCalendarEntryEventType,
    )
    from ..models.calendar_entry_calendar_owner import CalendarEntryCalendarOwner
    from ..models.calendar_entry_conference_meeting import (
        CalendarEntryConferenceMeeting,
    )
    from ..models.calendar_entry_matter import CalendarEntryMatter
    from ..models.calendar_entry_matter_docket import CalendarEntryMatterDocket
    from ..models.calendar_entry_parent_calendar_entry import (
        CalendarEntryParentCalendarEntry,
    )
    from ..models.external_property_base import ExternalPropertyBase
    from ..models.reminder_base import ReminderBase


T = TypeVar("T", bound="CalendarEntry")


@_attrs_define
class CalendarEntry:
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
        attendees (Union[Unset, list['AttendeeBase']]): Attendee
        calendar_entry_event_type (Union[Unset, CalendarEntryCalendarEntryEventType]):
        calendar_owner (Union[Unset, CalendarEntryCalendarOwner]):
        calendars (Union[Unset, list['CalendarBase']]): Calendar
        conference_meeting (Union[Unset, CalendarEntryConferenceMeeting]):
        external_properties (Union[Unset, list['ExternalPropertyBase']]): ExternalProperty
        matter (Union[Unset, CalendarEntryMatter]):
        matter_docket (Union[Unset, CalendarEntryMatterDocket]):
        parent_calendar_entry (Union[Unset, CalendarEntryParentCalendarEntry]):
        reminders (Union[Unset, list['ReminderBase']]): Reminder
        time_entries (Union[Unset, list['ActivityBase']]): Activity
    """

    all_day: Unset | bool = UNSET
    calendar_owner_id: Unset | int = UNSET
    court_rule: Unset | bool = UNSET
    created_at: Unset | str = UNSET
    description: Unset | str = UNSET
    end_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | str = UNSET
    location: Unset | str = UNSET
    parent_calendar_entry_id: Unset | int = UNSET
    permission: Unset | str = UNSET
    recurrence_rule: Unset | str = UNSET
    start_at: Unset | str = UNSET
    start_at_time_zone: Unset | str = UNSET
    summary: Unset | str = UNSET
    time_entries_count: Unset | int = UNSET
    updated_at: Unset | str = UNSET
    attendees: Unset | list["AttendeeBase"] = UNSET
    calendar_entry_event_type: Union[Unset, "CalendarEntryCalendarEntryEventType"] = (
        UNSET
    )
    calendar_owner: Union[Unset, "CalendarEntryCalendarOwner"] = UNSET
    calendars: Unset | list["CalendarBase"] = UNSET
    conference_meeting: Union[Unset, "CalendarEntryConferenceMeeting"] = UNSET
    external_properties: Unset | list["ExternalPropertyBase"] = UNSET
    matter: Union[Unset, "CalendarEntryMatter"] = UNSET
    matter_docket: Union[Unset, "CalendarEntryMatterDocket"] = UNSET
    parent_calendar_entry: Union[Unset, "CalendarEntryParentCalendarEntry"] = UNSET
    reminders: Unset | list["ReminderBase"] = UNSET
    time_entries: Unset | list["ActivityBase"] = UNSET
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

        attendees: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.attendees, Unset):
            attendees = []
            for attendees_item_data in self.attendees:
                attendees_item = attendees_item_data.to_dict()
                attendees.append(attendees_item)

        calendar_entry_event_type: Unset | dict[str, Any] = UNSET
        if not isinstance(self.calendar_entry_event_type, Unset):
            calendar_entry_event_type = self.calendar_entry_event_type.to_dict()

        calendar_owner: Unset | dict[str, Any] = UNSET
        if not isinstance(self.calendar_owner, Unset):
            calendar_owner = self.calendar_owner.to_dict()

        calendars: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.calendars, Unset):
            calendars = []
            for calendars_item_data in self.calendars:
                calendars_item = calendars_item_data.to_dict()
                calendars.append(calendars_item)

        conference_meeting: Unset | dict[str, Any] = UNSET
        if not isinstance(self.conference_meeting, Unset):
            conference_meeting = self.conference_meeting.to_dict()

        external_properties: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.external_properties, Unset):
            external_properties = []
            for external_properties_item_data in self.external_properties:
                external_properties_item = external_properties_item_data.to_dict()
                external_properties.append(external_properties_item)

        matter: Unset | dict[str, Any] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        matter_docket: Unset | dict[str, Any] = UNSET
        if not isinstance(self.matter_docket, Unset):
            matter_docket = self.matter_docket.to_dict()

        parent_calendar_entry: Unset | dict[str, Any] = UNSET
        if not isinstance(self.parent_calendar_entry, Unset):
            parent_calendar_entry = self.parent_calendar_entry.to_dict()

        reminders: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.reminders, Unset):
            reminders = []
            for reminders_item_data in self.reminders:
                reminders_item = reminders_item_data.to_dict()
                reminders.append(reminders_item)

        time_entries: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.time_entries, Unset):
            time_entries = []
            for time_entries_item_data in self.time_entries:
                time_entries_item = time_entries_item_data.to_dict()
                time_entries.append(time_entries_item)

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
        if attendees is not UNSET:
            field_dict["attendees"] = attendees
        if calendar_entry_event_type is not UNSET:
            field_dict["calendar_entry_event_type"] = calendar_entry_event_type
        if calendar_owner is not UNSET:
            field_dict["calendar_owner"] = calendar_owner
        if calendars is not UNSET:
            field_dict["calendars"] = calendars
        if conference_meeting is not UNSET:
            field_dict["conference_meeting"] = conference_meeting
        if external_properties is not UNSET:
            field_dict["external_properties"] = external_properties
        if matter is not UNSET:
            field_dict["matter"] = matter
        if matter_docket is not UNSET:
            field_dict["matter_docket"] = matter_docket
        if parent_calendar_entry is not UNSET:
            field_dict["parent_calendar_entry"] = parent_calendar_entry
        if reminders is not UNSET:
            field_dict["reminders"] = reminders
        if time_entries is not UNSET:
            field_dict["time_entries"] = time_entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_base import ActivityBase
        from ..models.attendee_base import AttendeeBase
        from ..models.calendar_base import CalendarBase
        from ..models.calendar_entry_calendar_entry_event_type import (
            CalendarEntryCalendarEntryEventType,
        )
        from ..models.calendar_entry_calendar_owner import CalendarEntryCalendarOwner
        from ..models.calendar_entry_conference_meeting import (
            CalendarEntryConferenceMeeting,
        )
        from ..models.calendar_entry_matter import CalendarEntryMatter
        from ..models.calendar_entry_matter_docket import CalendarEntryMatterDocket
        from ..models.calendar_entry_parent_calendar_entry import (
            CalendarEntryParentCalendarEntry,
        )
        from ..models.external_property_base import ExternalPropertyBase
        from ..models.reminder_base import ReminderBase

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

        attendees = []
        _attendees = d.pop("attendees", UNSET)
        for attendees_item_data in _attendees or []:
            attendees_item = AttendeeBase.from_dict(attendees_item_data)

            attendees.append(attendees_item)

        _calendar_entry_event_type = d.pop("calendar_entry_event_type", UNSET)
        calendar_entry_event_type: Unset | CalendarEntryCalendarEntryEventType
        if isinstance(_calendar_entry_event_type, Unset):
            calendar_entry_event_type = UNSET
        else:
            calendar_entry_event_type = CalendarEntryCalendarEntryEventType.from_dict(
                _calendar_entry_event_type
            )

        _calendar_owner = d.pop("calendar_owner", UNSET)
        calendar_owner: Unset | CalendarEntryCalendarOwner
        if isinstance(_calendar_owner, Unset):
            calendar_owner = UNSET
        else:
            calendar_owner = CalendarEntryCalendarOwner.from_dict(_calendar_owner)

        calendars = []
        _calendars = d.pop("calendars", UNSET)
        for calendars_item_data in _calendars or []:
            calendars_item = CalendarBase.from_dict(calendars_item_data)

            calendars.append(calendars_item)

        _conference_meeting = d.pop("conference_meeting", UNSET)
        conference_meeting: Unset | CalendarEntryConferenceMeeting
        if isinstance(_conference_meeting, Unset):
            conference_meeting = UNSET
        else:
            conference_meeting = CalendarEntryConferenceMeeting.from_dict(
                _conference_meeting
            )

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = ExternalPropertyBase.from_dict(
                external_properties_item_data
            )

            external_properties.append(external_properties_item)

        _matter = d.pop("matter", UNSET)
        matter: Unset | CalendarEntryMatter
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = CalendarEntryMatter.from_dict(_matter)

        _matter_docket = d.pop("matter_docket", UNSET)
        matter_docket: Unset | CalendarEntryMatterDocket
        if isinstance(_matter_docket, Unset):
            matter_docket = UNSET
        else:
            matter_docket = CalendarEntryMatterDocket.from_dict(_matter_docket)

        _parent_calendar_entry = d.pop("parent_calendar_entry", UNSET)
        parent_calendar_entry: Unset | CalendarEntryParentCalendarEntry
        if isinstance(_parent_calendar_entry, Unset):
            parent_calendar_entry = UNSET
        else:
            parent_calendar_entry = CalendarEntryParentCalendarEntry.from_dict(
                _parent_calendar_entry
            )

        reminders = []
        _reminders = d.pop("reminders", UNSET)
        for reminders_item_data in _reminders or []:
            reminders_item = ReminderBase.from_dict(reminders_item_data)

            reminders.append(reminders_item)

        time_entries = []
        _time_entries = d.pop("time_entries", UNSET)
        for time_entries_item_data in _time_entries or []:
            time_entries_item = ActivityBase.from_dict(time_entries_item_data)

            time_entries.append(time_entries_item)

        calendar_entry = cls(
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
            attendees=attendees,
            calendar_entry_event_type=calendar_entry_event_type,
            calendar_owner=calendar_owner,
            calendars=calendars,
            conference_meeting=conference_meeting,
            external_properties=external_properties,
            matter=matter,
            matter_docket=matter_docket,
            parent_calendar_entry=parent_calendar_entry,
            reminders=reminders,
            time_entries=time_entries,
        )

        calendar_entry.additional_properties = d
        return calendar_entry

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
