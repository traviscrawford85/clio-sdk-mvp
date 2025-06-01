from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mattercreate_data_body_data_custom_rate_rates_item_activity_description import (
        MattercreateDataBodyDataCustomRateRatesItemActivityDescription,
    )
    from ..models.mattercreate_data_body_data_custom_rate_rates_item_group import (
        MattercreateDataBodyDataCustomRateRatesItemGroup,
    )
    from ..models.mattercreate_data_body_data_custom_rate_rates_item_user import (
        MattercreateDataBodyDataCustomRateRatesItemUser,
    )


T = TypeVar("T", bound="MattercreateDataBodyDataCustomRateRatesItem")


@_attrs_define
class MattercreateDataBodyDataCustomRateRatesItem:
    """
    Attributes:
        rate (float): If `type` is `HourlyRate`, it is the dollar amount of the custom rate of the User or Group for the
            Matter.

            If `type` is `FlatRate`, it is the dollar amount of the custom flat rate for the Matter.

            If `type` is `ContingencyFee`, it is the percentage of the contingency fee awarded to the user for the Matter.
        user (MattercreateDataBodyDataCustomRateRatesItemUser):
        activity_description (Union[Unset, MattercreateDataBodyDataCustomRateRatesItemActivityDescription]):
        award (Union[Unset, float]): The full amount of the award given. Only valid for ContingencyFee. If given as an
            empty string, it will reset the ContingencyFee into the unawarded state.
        date (Union[Unset, str]): The date the rate is for. Only valid for ContingencyFee. (Expects an ISO-8601 date).
        group (Union[Unset, MattercreateDataBodyDataCustomRateRatesItemGroup]):
        note (Union[Unset, str]): Detailed description of the rate. Only valid for ContingencyFee.
    """

    rate: float
    user: "MattercreateDataBodyDataCustomRateRatesItemUser"
    activity_description: Union[
        Unset, "MattercreateDataBodyDataCustomRateRatesItemActivityDescription"
    ] = UNSET
    award: Unset | float = UNSET
    date: Unset | str = UNSET
    group: Union[Unset, "MattercreateDataBodyDataCustomRateRatesItemGroup"] = UNSET
    note: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate = self.rate

        user = self.user.to_dict()

        activity_description: Unset | dict[str, Any] = UNSET
        if not isinstance(self.activity_description, Unset):
            activity_description = self.activity_description.to_dict()

        award = self.award

        date = self.date

        group: Unset | dict[str, Any] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rate": rate,
                "user": user,
            }
        )
        if activity_description is not UNSET:
            field_dict["activity_description"] = activity_description
        if award is not UNSET:
            field_dict["award"] = award
        if date is not UNSET:
            field_dict["date"] = date
        if group is not UNSET:
            field_dict["group"] = group
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mattercreate_data_body_data_custom_rate_rates_item_activity_description import (
            MattercreateDataBodyDataCustomRateRatesItemActivityDescription,
        )
        from ..models.mattercreate_data_body_data_custom_rate_rates_item_group import (
            MattercreateDataBodyDataCustomRateRatesItemGroup,
        )
        from ..models.mattercreate_data_body_data_custom_rate_rates_item_user import (
            MattercreateDataBodyDataCustomRateRatesItemUser,
        )

        d = dict(src_dict)
        rate = d.pop("rate")

        user = MattercreateDataBodyDataCustomRateRatesItemUser.from_dict(d.pop("user"))

        _activity_description = d.pop("activity_description", UNSET)
        activity_description: (
            Unset | MattercreateDataBodyDataCustomRateRatesItemActivityDescription
        )
        if isinstance(_activity_description, Unset):
            activity_description = UNSET
        else:
            activity_description = MattercreateDataBodyDataCustomRateRatesItemActivityDescription.from_dict(
                _activity_description
            )

        award = d.pop("award", UNSET)

        date = d.pop("date", UNSET)

        _group = d.pop("group", UNSET)
        group: Unset | MattercreateDataBodyDataCustomRateRatesItemGroup
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = MattercreateDataBodyDataCustomRateRatesItemGroup.from_dict(_group)

        note = d.pop("note", UNSET)

        mattercreate_data_body_data_custom_rate_rates_item = cls(
            rate=rate,
            user=user,
            activity_description=activity_description,
            award=award,
            date=date,
            group=group,
            note=note,
        )

        mattercreate_data_body_data_custom_rate_rates_item.additional_properties = d
        return mattercreate_data_body_data_custom_rate_rates_item

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
