from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.calendar_entry_base import CalendarEntryBase
    from ..models.matter_docket_jurisdiction import MatterDocketJurisdiction
    from ..models.matter_docket_matter import MatterDocketMatter
    from ..models.matter_docket_service_type import MatterDocketServiceType
    from ..models.matter_docket_trigger import MatterDocketTrigger


T = TypeVar("T", bound="MatterDocket")


@_attrs_define
class MatterDocket:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *MatterDocket* was created (as a ISO-8601 timestamp)
        deleted_at (Union[Unset, str]): The time the *MatterDocket* was deleted (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *MatterDocket*
        id (Union[Unset, int]): Unique identifier for the *MatterDocket*
        name (Union[Unset, str]): The name of the *MatterDocket*
        start_date (Union[Unset, str]): The date the *MatterDocket* will start (as a ISO-8601 date)
        start_time (Union[Unset, str]): The time the *MatterDocket* will start, required for specific triggers (as a
            ISO-8601 timestamp)
        status (Union[Unset, str]): The status of the *MatterDocket* creation
        updated_at (Union[Unset, str]): The time the *MatterDocket* was last updated (as a ISO-8601 timestamp)
        calendar_entries (Union[Unset, list['CalendarEntryBase']]): CalendarEntry
        jurisdiction (Union[Unset, MatterDocketJurisdiction]):
        matter (Union[Unset, MatterDocketMatter]):
        service_type (Union[Unset, MatterDocketServiceType]):
        trigger (Union[Unset, MatterDocketTrigger]):
    """

    created_at: Unset | str = UNSET
    deleted_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    name: Unset | str = UNSET
    start_date: Unset | str = UNSET
    start_time: Unset | str = UNSET
    status: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    calendar_entries: Unset | list["CalendarEntryBase"] = UNSET
    jurisdiction: Union[Unset, "MatterDocketJurisdiction"] = UNSET
    matter: Union[Unset, "MatterDocketMatter"] = UNSET
    service_type: Union[Unset, "MatterDocketServiceType"] = UNSET
    trigger: Union[Unset, "MatterDocketTrigger"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        deleted_at = self.deleted_at

        etag = self.etag

        id = self.id

        name = self.name

        start_date = self.start_date

        start_time = self.start_time

        status = self.status

        updated_at = self.updated_at

        calendar_entries: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.calendar_entries, Unset):
            calendar_entries = []
            for calendar_entries_item_data in self.calendar_entries:
                calendar_entries_item = calendar_entries_item_data.to_dict()
                calendar_entries.append(calendar_entries_item)

        jurisdiction: Unset | dict[str, Any] = UNSET
        if not isinstance(self.jurisdiction, Unset):
            jurisdiction = self.jurisdiction.to_dict()

        matter: Unset | dict[str, Any] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        service_type: Unset | dict[str, Any] = UNSET
        if not isinstance(self.service_type, Unset):
            service_type = self.service_type.to_dict()

        trigger: Unset | dict[str, Any] = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if calendar_entries is not UNSET:
            field_dict["calendar_entries"] = calendar_entries
        if jurisdiction is not UNSET:
            field_dict["jurisdiction"] = jurisdiction
        if matter is not UNSET:
            field_dict["matter"] = matter
        if service_type is not UNSET:
            field_dict["service_type"] = service_type
        if trigger is not UNSET:
            field_dict["trigger"] = trigger

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.calendar_entry_base import CalendarEntryBase
        from ..models.matter_docket_jurisdiction import MatterDocketJurisdiction
        from ..models.matter_docket_matter import MatterDocketMatter
        from ..models.matter_docket_service_type import MatterDocketServiceType
        from ..models.matter_docket_trigger import MatterDocketTrigger

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        deleted_at = d.pop("deleted_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        start_date = d.pop("start_date", UNSET)

        start_time = d.pop("start_time", UNSET)

        status = d.pop("status", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        calendar_entries = []
        _calendar_entries = d.pop("calendar_entries", UNSET)
        for calendar_entries_item_data in _calendar_entries or []:
            calendar_entries_item = CalendarEntryBase.from_dict(
                calendar_entries_item_data
            )

            calendar_entries.append(calendar_entries_item)

        _jurisdiction = d.pop("jurisdiction", UNSET)
        jurisdiction: Unset | MatterDocketJurisdiction
        if isinstance(_jurisdiction, Unset):
            jurisdiction = UNSET
        else:
            jurisdiction = MatterDocketJurisdiction.from_dict(_jurisdiction)

        _matter = d.pop("matter", UNSET)
        matter: Unset | MatterDocketMatter
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MatterDocketMatter.from_dict(_matter)

        _service_type = d.pop("service_type", UNSET)
        service_type: Unset | MatterDocketServiceType
        if isinstance(_service_type, Unset):
            service_type = UNSET
        else:
            service_type = MatterDocketServiceType.from_dict(_service_type)

        _trigger = d.pop("trigger", UNSET)
        trigger: Unset | MatterDocketTrigger
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = MatterDocketTrigger.from_dict(_trigger)

        matter_docket = cls(
            created_at=created_at,
            deleted_at=deleted_at,
            etag=etag,
            id=id,
            name=name,
            start_date=start_date,
            start_time=start_time,
            status=status,
            updated_at=updated_at,
            calendar_entries=calendar_entries,
            jurisdiction=jurisdiction,
            matter=matter,
            service_type=service_type,
            trigger=trigger,
        )

        matter_docket.additional_properties = d
        return matter_docket

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
