from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_schedule_base_frequency import ReportScheduleBaseFrequency
from ..models.report_schedule_base_status import ReportScheduleBaseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportScheduleBase")


@_attrs_define
class ReportScheduleBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *ReportSchedule* was created (as a ISO-8601 timestamp)
        day_of_month (Union[Unset, int]): If the frequency is monthly, which day of the month the Report Schedule is
            run. 32 is used to represent the last day of the month.
        days_of_week (Union[Unset, list[int]]): If the frequency is weekly, which days of the week the Report Schedule
            is run. Values are 0 to 6, representing Sunday to Saturday.
        effective_from (Union[Unset, str]): The date the Report Schedule will become enabled (a ISO-8601 date)
        etag (Union[Unset, str]): ETag for the *ReportSchedule*
        every_no_of_months (Union[Unset, int]): If the frequency is monthly, how many months between each run of the
            Report Schedule
        frequency (Union[Unset, ReportScheduleBaseFrequency]): How often the Report Schedule is run
        id (Union[Unset, int]): Unique identifier for the *ReportSchedule*
        next_scheduled_date (Union[Unset, str]): The next time the Report Schedule should run
        report_preset_id (Union[Unset, int]): The unique identifier of the Report Preset to use when generating the
            scheduled report
        status (Union[Unset, ReportScheduleBaseStatus]): The status of the Report Schedule
        status_updated_at (Union[Unset, str]): When the status of the Report Schedule was last updated
        time_of_day (Union[Unset, str]): What time the Report Schedule is run
        time_zone (Union[Unset, str]): Used in conjunction with `time_of_day` to determine when the Report Schedule
            should run
        updated_at (Union[Unset, str]): The time the *ReportSchedule* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Union[Unset, str] = UNSET
    day_of_month: Union[Unset, int] = UNSET
    days_of_week: Union[Unset, list[int]] = UNSET
    effective_from: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    every_no_of_months: Union[Unset, int] = UNSET
    frequency: Union[Unset, ReportScheduleBaseFrequency] = UNSET
    id: Union[Unset, int] = UNSET
    next_scheduled_date: Union[Unset, str] = UNSET
    report_preset_id: Union[Unset, int] = UNSET
    status: Union[Unset, ReportScheduleBaseStatus] = UNSET
    status_updated_at: Union[Unset, str] = UNSET
    time_of_day: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        day_of_month = self.day_of_month

        days_of_week: Union[Unset, list[int]] = UNSET
        if not isinstance(self.days_of_week, Unset):
            days_of_week = self.days_of_week

        effective_from = self.effective_from

        etag = self.etag

        every_no_of_months = self.every_no_of_months

        frequency: Union[Unset, str] = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value

        id = self.id

        next_scheduled_date = self.next_scheduled_date

        report_preset_id = self.report_preset_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_updated_at = self.status_updated_at

        time_of_day = self.time_of_day

        time_zone = self.time_zone

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if day_of_month is not UNSET:
            field_dict["day_of_month"] = day_of_month
        if days_of_week is not UNSET:
            field_dict["days_of_week"] = days_of_week
        if effective_from is not UNSET:
            field_dict["effective_from"] = effective_from
        if etag is not UNSET:
            field_dict["etag"] = etag
        if every_no_of_months is not UNSET:
            field_dict["every_no_of_months"] = every_no_of_months
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if id is not UNSET:
            field_dict["id"] = id
        if next_scheduled_date is not UNSET:
            field_dict["next_scheduled_date"] = next_scheduled_date
        if report_preset_id is not UNSET:
            field_dict["report_preset_id"] = report_preset_id
        if status is not UNSET:
            field_dict["status"] = status
        if status_updated_at is not UNSET:
            field_dict["status_updated_at"] = status_updated_at
        if time_of_day is not UNSET:
            field_dict["time_of_day"] = time_of_day
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        day_of_month = d.pop("day_of_month", UNSET)

        days_of_week = cast(list[int], d.pop("days_of_week", UNSET))

        effective_from = d.pop("effective_from", UNSET)

        etag = d.pop("etag", UNSET)

        every_no_of_months = d.pop("every_no_of_months", UNSET)

        _frequency = d.pop("frequency", UNSET)
        frequency: Union[Unset, ReportScheduleBaseFrequency]
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = ReportScheduleBaseFrequency(_frequency)

        id = d.pop("id", UNSET)

        next_scheduled_date = d.pop("next_scheduled_date", UNSET)

        report_preset_id = d.pop("report_preset_id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ReportScheduleBaseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ReportScheduleBaseStatus(_status)

        status_updated_at = d.pop("status_updated_at", UNSET)

        time_of_day = d.pop("time_of_day", UNSET)

        time_zone = d.pop("time_zone", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        report_schedule_base = cls(
            created_at=created_at,
            day_of_month=day_of_month,
            days_of_week=days_of_week,
            effective_from=effective_from,
            etag=etag,
            every_no_of_months=every_no_of_months,
            frequency=frequency,
            id=id,
            next_scheduled_date=next_scheduled_date,
            report_preset_id=report_preset_id,
            status=status,
            status_updated_at=status_updated_at,
            time_of_day=time_of_day,
            time_zone=time_zone,
            updated_at=updated_at,
        )

        report_schedule_base.additional_properties = d
        return report_schedule_base

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
