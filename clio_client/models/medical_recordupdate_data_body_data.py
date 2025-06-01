from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MedicalRecordupdateDataBodyData")


@_attrs_define
class MedicalRecordupdateDataBodyData:
    """
    Attributes:
        end_date (Union[Unset, str]): End date for Medical Record.
        start_date (Union[Unset, str]): Start date for Medical Record.
    """

    end_date: Unset | str = UNSET
    start_date: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date = self.end_date

        start_date = self.start_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_date = d.pop("end_date", UNSET)

        start_date = d.pop("start_date", UNSET)

        medical_recordupdate_data_body_data = cls(
            end_date=end_date,
            start_date=start_date,
        )

        medical_recordupdate_data_body_data.additional_properties = d
        return medical_recordupdate_data_body_data

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
