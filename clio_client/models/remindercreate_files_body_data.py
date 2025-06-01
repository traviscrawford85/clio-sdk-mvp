from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.remindercreate_files_body_data_duration_unit import (
    RemindercreateFilesBodyDataDurationUnit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.remindercreate_files_body_data_notification_method import (
        RemindercreateFilesBodyDataNotificationMethod,
    )
    from ..models.remindercreate_files_body_data_subject import (
        RemindercreateFilesBodyDataSubject,
    )


T = TypeVar("T", bound="RemindercreateFilesBodyData")


@_attrs_define
class RemindercreateFilesBodyData:
    """
    Attributes:
        notification_method (RemindercreateFilesBodyDataNotificationMethod):
        subject (RemindercreateFilesBodyDataSubject):
        duration_unit (Union[Unset, RemindercreateFilesBodyDataDurationUnit]): Unit to measure the duration value in.
        duration_value (Union[Unset, int]): Time measured in `duration_unit` to remind user before the subject.
    """

    notification_method: "RemindercreateFilesBodyDataNotificationMethod"
    subject: "RemindercreateFilesBodyDataSubject"
    duration_unit: Unset | RemindercreateFilesBodyDataDurationUnit = UNSET
    duration_value: Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification_method = self.notification_method.to_dict()

        subject = self.subject.to_dict()

        duration_unit: Unset | str = UNSET
        if not isinstance(self.duration_unit, Unset):
            duration_unit = self.duration_unit.value

        duration_value = self.duration_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notification_method": notification_method,
                "subject": subject,
            }
        )
        if duration_unit is not UNSET:
            field_dict["duration_unit"] = duration_unit
        if duration_value is not UNSET:
            field_dict["duration_value"] = duration_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.remindercreate_files_body_data_notification_method import (
            RemindercreateFilesBodyDataNotificationMethod,
        )
        from ..models.remindercreate_files_body_data_subject import (
            RemindercreateFilesBodyDataSubject,
        )

        d = dict(src_dict)
        notification_method = RemindercreateFilesBodyDataNotificationMethod.from_dict(
            d.pop("notification_method")
        )

        subject = RemindercreateFilesBodyDataSubject.from_dict(d.pop("subject"))

        _duration_unit = d.pop("duration_unit", UNSET)
        duration_unit: Unset | RemindercreateFilesBodyDataDurationUnit
        if isinstance(_duration_unit, Unset):
            duration_unit = UNSET
        else:
            duration_unit = RemindercreateFilesBodyDataDurationUnit(_duration_unit)

        duration_value = d.pop("duration_value", UNSET)

        remindercreate_files_body_data = cls(
            notification_method=notification_method,
            subject=subject,
            duration_unit=duration_unit,
            duration_value=duration_value,
        )

        remindercreate_files_body_data.additional_properties = d
        return remindercreate_files_body_data

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
