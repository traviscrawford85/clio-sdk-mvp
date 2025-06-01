from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatuteOfLimitationsComputeRequest")


@_attrs_define
class StatuteOfLimitationsComputeRequest:
    """
    Attributes:
        date_of_incident (str): The date when the incident occurred.
    """

    date_of_incident: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_of_incident = self.date_of_incident

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date_of_incident": date_of_incident,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date_of_incident = d.pop("date_of_incident")

        statute_of_limitations_compute_request = cls(
            date_of_incident=date_of_incident,
        )

        statute_of_limitations_compute_request.additional_properties = d
        return statute_of_limitations_compute_request

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
