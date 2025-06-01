from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_scheduleupdate_data_body_data_frequency import (
    ReportScheduleupdateDataBodyDataFrequency,
)
from ..models.report_scheduleupdate_data_body_data_time_zone import (
    ReportScheduleupdateDataBodyDataTimeZone,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportScheduleupdateDataBodyData")


@_attrs_define
class ReportScheduleupdateDataBodyData:
    """
    Attributes:
        day_of_month (Union[Unset, int]): If the frequency is monthly, which day of the month the Report Schedule should
            run. 32 is used to represent the last day of the month.
        days_of_week (Union[Unset, list[int]]): If the frequency is weekly, which days of the week the Report Schedule
            should run. Values are 0 to 6, representing Sunday to Saturday.
        effective_from (Union[Unset, str]): Date the Report Schedule should be enabled. (Expects an ISO-8601 date).
        every_no_of_months (Union[Unset, int]): If the frequency is monthly, how many months between each run of the
            Report Schedule.
        frequency (Union[Unset, ReportScheduleupdateDataBodyDataFrequency]): How often to run the Report Schedule.
        report_preset_id (Union[Unset, int]): What Report Preset the Report Schedule should use to generate a report.
        time_of_day (Union[Unset, str]): What time the Report Schedule should run. Although the entire datetime is sent,
            only the time information is used.
        time_zone (Union[Unset, ReportScheduleupdateDataBodyDataTimeZone]): Used in conjunction with `time_of_day` to
            determine when the Report Schedule should be run.
    """

    day_of_month: Unset | int = UNSET
    days_of_week: Unset | list[int] = UNSET
    effective_from: Unset | str = UNSET
    every_no_of_months: Unset | int = UNSET
    frequency: Unset | ReportScheduleupdateDataBodyDataFrequency = UNSET
    report_preset_id: Unset | int = UNSET
    time_of_day: Unset | str = UNSET
    time_zone: Unset | ReportScheduleupdateDataBodyDataTimeZone = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day_of_month = self.day_of_month

        days_of_week: Unset | list[int] = UNSET
        if not isinstance(self.days_of_week, Unset):
            days_of_week = self.days_of_week

        effective_from = self.effective_from

        every_no_of_months = self.every_no_of_months

        frequency: Unset | str = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value

        report_preset_id = self.report_preset_id

        time_of_day = self.time_of_day

        time_zone: Unset | str = UNSET
        if not isinstance(self.time_zone, Unset):
            time_zone = self.time_zone.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day_of_month is not UNSET:
            field_dict["day_of_month"] = day_of_month
        if days_of_week is not UNSET:
            field_dict["days_of_week"] = days_of_week
        if effective_from is not UNSET:
            field_dict["effective_from"] = effective_from
        if every_no_of_months is not UNSET:
            field_dict["every_no_of_months"] = every_no_of_months
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if report_preset_id is not UNSET:
            field_dict["report_preset_id"] = report_preset_id
        if time_of_day is not UNSET:
            field_dict["time_of_day"] = time_of_day
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day_of_month = d.pop("day_of_month", UNSET)

        days_of_week = cast(list[int], d.pop("days_of_week", UNSET))

        effective_from = d.pop("effective_from", UNSET)

        every_no_of_months = d.pop("every_no_of_months", UNSET)

        _frequency = d.pop("frequency", UNSET)
        frequency: Unset | ReportScheduleupdateDataBodyDataFrequency
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = ReportScheduleupdateDataBodyDataFrequency(_frequency)

        report_preset_id = d.pop("report_preset_id", UNSET)

        time_of_day = d.pop("time_of_day", UNSET)

        _time_zone = d.pop("time_zone", UNSET)
        time_zone: Unset | ReportScheduleupdateDataBodyDataTimeZone
        if isinstance(_time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = ReportScheduleupdateDataBodyDataTimeZone(_time_zone)

        report_scheduleupdate_data_body_data = cls(
            day_of_month=day_of_month,
            days_of_week=days_of_week,
            effective_from=effective_from,
            every_no_of_months=every_no_of_months,
            frequency=frequency,
            report_preset_id=report_preset_id,
            time_of_day=time_of_day,
            time_zone=time_zone,
        )

        report_scheduleupdate_data_body_data.additional_properties = d
        return report_scheduleupdate_data_body_data

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
