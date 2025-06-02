from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matter_docketcreate_data_body_data_jurisdiction import (
        MatterDocketcreateDataBodyDataJurisdiction,
    )
    from ..models.matter_docketcreate_data_body_data_trigger import (
        MatterDocketcreateDataBodyDataTrigger,
    )


T = TypeVar("T", bound="MatterDocketcreateDataBodyData")


@_attrs_define
class MatterDocketcreateDataBodyData:
    """
    Attributes:
        jurisdiction (MatterDocketcreateDataBodyDataJurisdiction):
        name (str): Name of the MatterDocket.
        start_date (str): Start date of the MatterDocket. (Expects an ISO-8601 date).
        trigger (MatterDocketcreateDataBodyDataTrigger):
        start_time (Union[Unset, str]): Start time of the MatterDocket. Required for some triggers.  (Expects an
            ISO-8601 timestamp).
    """

    jurisdiction: "MatterDocketcreateDataBodyDataJurisdiction"
    name: str
    start_date: str
    trigger: "MatterDocketcreateDataBodyDataTrigger"
    start_time: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jurisdiction = self.jurisdiction.to_dict()

        name = self.name

        start_date = self.start_date

        trigger = self.trigger.to_dict()

        start_time = self.start_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jurisdiction": jurisdiction,
                "name": name,
                "start_date": start_date,
                "trigger": trigger,
            }
        )
        if start_time is not UNSET:
            field_dict["start_time"] = start_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matter_docketcreate_data_body_data_jurisdiction import (
            MatterDocketcreateDataBodyDataJurisdiction,
        )
        from ..models.matter_docketcreate_data_body_data_trigger import (
            MatterDocketcreateDataBodyDataTrigger,
        )

        d = dict(src_dict)
        jurisdiction = MatterDocketcreateDataBodyDataJurisdiction.from_dict(d.pop("jurisdiction"))

        name = d.pop("name")

        start_date = d.pop("start_date")

        trigger = MatterDocketcreateDataBodyDataTrigger.from_dict(d.pop("trigger"))

        start_time = d.pop("start_time", UNSET)

        matter_docketcreate_data_body_data = cls(
            jurisdiction=jurisdiction,
            name=name,
            start_date=start_date,
            trigger=trigger,
            start_time=start_time,
        )

        matter_docketcreate_data_body_data.additional_properties = d
        return matter_docketcreate_data_body_data

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
