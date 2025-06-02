from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matterupdate_json_body_data_custom_rate_rates_item_activity_description import (
        MatterupdateJsonBodyDataCustomRateRatesItemActivityDescription,
    )
    from ..models.matterupdate_json_body_data_custom_rate_rates_item_group import (
        MatterupdateJsonBodyDataCustomRateRatesItemGroup,
    )
    from ..models.matterupdate_json_body_data_custom_rate_rates_item_user import (
        MatterupdateJsonBodyDataCustomRateRatesItemUser,
    )


T = TypeVar("T", bound="MatterupdateJsonBodyDataCustomRateRatesItem")


@_attrs_define
class MatterupdateJsonBodyDataCustomRateRatesItem:
    """
    Attributes:
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated Rate is present, the Rate is deleted from the Matter.
        activity_description (Union[Unset, MatterupdateJsonBodyDataCustomRateRatesItemActivityDescription]):
        award (Union[Unset, float]): The full amount of the award given. Only valid for ContingencyFee. If given as an
            empty string, it will reset the ContingencyFee into the unawarded state.
        date (Union[Unset, str]): The date the rate is for. Only valid for ContingencyFee. (Expects an ISO-8601 date).
        group (Union[Unset, MatterupdateJsonBodyDataCustomRateRatesItemGroup]):
        id (Union[Unset, int]): The unique identifier for a single Rate associated with the Matter. The keyword `null`
            is not valid for this field.
        note (Union[Unset, str]): Detailed description of the rate. Only valid for ContingencyFee.
        rate (Union[Unset, float]): If `type` is `HourlyRate`, it is the dollar amount of the custom rate of the User or
            Group for the Matter.

            If `type` is `FlatRate`, it is the dollar amount of the custom flat rate for the Matter.

            If `type` is `ContingencyFee`, it is the percentage of the contingency fee awarded to the user for the Matter.
        user (Union[Unset, MatterupdateJsonBodyDataCustomRateRatesItemUser]):
    """

    field_destroy: Union[Unset, bool] = UNSET
    activity_description: Union[Unset, "MatterupdateJsonBodyDataCustomRateRatesItemActivityDescription"] = UNSET
    award: Union[Unset, float] = UNSET
    date: Union[Unset, str] = UNSET
    group: Union[Unset, "MatterupdateJsonBodyDataCustomRateRatesItemGroup"] = UNSET
    id: Union[Unset, int] = UNSET
    note: Union[Unset, str] = UNSET
    rate: Union[Unset, float] = UNSET
    user: Union[Unset, "MatterupdateJsonBodyDataCustomRateRatesItemUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_destroy = self.field_destroy

        activity_description: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.activity_description, Unset):
            activity_description = self.activity_description.to_dict()

        award = self.award

        date = self.date

        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        id = self.id

        note = self.note

        rate = self.rate

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if activity_description is not UNSET:
            field_dict["activity_description"] = activity_description
        if award is not UNSET:
            field_dict["award"] = award
        if date is not UNSET:
            field_dict["date"] = date
        if group is not UNSET:
            field_dict["group"] = group
        if id is not UNSET:
            field_dict["id"] = id
        if note is not UNSET:
            field_dict["note"] = note
        if rate is not UNSET:
            field_dict["rate"] = rate
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matterupdate_json_body_data_custom_rate_rates_item_activity_description import (
            MatterupdateJsonBodyDataCustomRateRatesItemActivityDescription,
        )
        from ..models.matterupdate_json_body_data_custom_rate_rates_item_group import (
            MatterupdateJsonBodyDataCustomRateRatesItemGroup,
        )
        from ..models.matterupdate_json_body_data_custom_rate_rates_item_user import (
            MatterupdateJsonBodyDataCustomRateRatesItemUser,
        )

        d = dict(src_dict)
        field_destroy = d.pop("_destroy", UNSET)

        _activity_description = d.pop("activity_description", UNSET)
        activity_description: Union[Unset, MatterupdateJsonBodyDataCustomRateRatesItemActivityDescription]
        if isinstance(_activity_description, Unset):
            activity_description = UNSET
        else:
            activity_description = MatterupdateJsonBodyDataCustomRateRatesItemActivityDescription.from_dict(
                _activity_description
            )

        award = d.pop("award", UNSET)

        date = d.pop("date", UNSET)

        _group = d.pop("group", UNSET)
        group: Union[Unset, MatterupdateJsonBodyDataCustomRateRatesItemGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = MatterupdateJsonBodyDataCustomRateRatesItemGroup.from_dict(_group)

        id = d.pop("id", UNSET)

        note = d.pop("note", UNSET)

        rate = d.pop("rate", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, MatterupdateJsonBodyDataCustomRateRatesItemUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = MatterupdateJsonBodyDataCustomRateRatesItemUser.from_dict(_user)

        matterupdate_json_body_data_custom_rate_rates_item = cls(
            field_destroy=field_destroy,
            activity_description=activity_description,
            award=award,
            date=date,
            group=group,
            id=id,
            note=note,
            rate=rate,
            user=user,
        )

        matterupdate_json_body_data_custom_rate_rates_item.additional_properties = d
        return matterupdate_json_body_data_custom_rate_rates_item

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
