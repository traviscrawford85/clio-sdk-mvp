from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_schedulecreate_json_body_data_frequency import (
    ReportSchedulecreateJsonBodyDataFrequency,
)
from ..models.report_schedulecreate_json_body_data_time_zone import (
    ReportSchedulecreateJsonBodyDataTimeZone,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportSchedulecreateJsonBodyData")


@_attrs_define
class ReportSchedulecreateJsonBodyData:
    """
    Attributes:
        frequency (ReportSchedulecreateJsonBodyDataFrequency): How often to run the Report Schedule.
        report_preset_id (int): What Report Preset the Report Schedule should use to generate a report.
        time_of_day (str): What time the Report Schedule should run. Although the entire datetime is sent, only the time
            information is used.
        time_zone (ReportSchedulecreateJsonBodyDataTimeZone): Used in conjunction with `time_of_day` to determine when
            the Report Schedule should be run.
        day_of_month (Union[Unset, int]): If the frequency is monthly, which day of the month the Report Schedule should
            run. 32 is used to represent the last day of the month.
        days_of_week (Union[Unset, list[int]]): If the frequency is weekly, which days of the week the Report Schedule
            should run. Values are 0 to 6, representing Sunday to Saturday.
        effective_from (Union[Unset, str]): Date the Report Schedule should be enabled. (Expects an ISO-8601 date).
        every_no_of_months (Union[Unset, int]): If the frequency is monthly, how many months between each run of the
            Report Schedule.
    """

    frequency: ReportSchedulecreateJsonBodyDataFrequency
    report_preset_id: int
    time_of_day: str
    time_zone: ReportSchedulecreateJsonBodyDataTimeZone
    day_of_month: Unset | int = UNSET
    days_of_week: Unset | list[int] = UNSET
    effective_from: Unset | str = UNSET
    every_no_of_months: Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        frequency = self.frequency.value

        report_preset_id = self.report_preset_id

        time_of_day = self.time_of_day

        time_zone = self.time_zone.value

        day_of_month = self.day_of_month

        days_of_week: Unset | list[int] = UNSET
        if not isinstance(self.days_of_week, Unset):
            days_of_week = self.days_of_week

        effective_from = self.effective_from

        every_no_of_months = self.every_no_of_months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "frequency": frequency,
                "report_preset_id": report_preset_id,
                "time_of_day": time_of_day,
                "time_zone": time_zone,
            }
        )
        if day_of_month is not UNSET:
            field_dict["day_of_month"] = day_of_month
        if days_of_week is not UNSET:
            field_dict["days_of_week"] = days_of_week
        if effective_from is not UNSET:
            field_dict["effective_from"] = effective_from
        if every_no_of_months is not UNSET:
            field_dict["every_no_of_months"] = every_no_of_months

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        frequency = ReportSchedulecreateJsonBodyDataFrequency(d.pop("frequency"))

        report_preset_id = d.pop("report_preset_id")

        time_of_day = d.pop("time_of_day")

        time_zone = ReportSchedulecreateJsonBodyDataTimeZone(d.pop("time_zone"))

        day_of_month = d.pop("day_of_month", UNSET)

        days_of_week = cast(list[int], d.pop("days_of_week", UNSET))

        effective_from = d.pop("effective_from", UNSET)

        every_no_of_months = d.pop("every_no_of_months", UNSET)

        report_schedulecreate_json_body_data = cls(
            frequency=frequency,
            report_preset_id=report_preset_id,
            time_of_day=time_of_day,
            time_zone=time_zone,
            day_of_month=day_of_month,
            days_of_week=days_of_week,
            effective_from=effective_from,
            every_no_of_months=every_no_of_months,
        )

        report_schedulecreate_json_body_data.additional_properties = d
        return report_schedulecreate_json_body_data

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
