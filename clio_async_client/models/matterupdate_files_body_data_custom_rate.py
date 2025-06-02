from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.matterupdate_files_body_data_custom_rate_type import (
    MatterupdateFilesBodyDataCustomRateType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matterupdate_files_body_data_custom_rate_rates_item import (
        MatterupdateFilesBodyDataCustomRateRatesItem,
    )


T = TypeVar("T", bound="MatterupdateFilesBodyDataCustomRate")


@_attrs_define
class MatterupdateFilesBodyDataCustomRate:
    """
    Attributes:
        rates (Union[Unset, list['MatterupdateFilesBodyDataCustomRateRatesItem']]):
        type_ (Union[Unset, MatterupdateFilesBodyDataCustomRateType]): The type of custom rate for the Matter.
    """

    rates: Union[Unset, list["MatterupdateFilesBodyDataCustomRateRatesItem"]] = UNSET
    type_: Union[Unset, MatterupdateFilesBodyDataCustomRateType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rates, Unset):
            rates = []
            for rates_item_data in self.rates:
                rates_item = rates_item_data.to_dict()
                rates.append(rates_item)

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rates is not UNSET:
            field_dict["rates"] = rates
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matterupdate_files_body_data_custom_rate_rates_item import (
            MatterupdateFilesBodyDataCustomRateRatesItem,
        )

        d = dict(src_dict)
        rates = []
        _rates = d.pop("rates", UNSET)
        for rates_item_data in _rates or []:
            rates_item = MatterupdateFilesBodyDataCustomRateRatesItem.from_dict(rates_item_data)

            rates.append(rates_item)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, MatterupdateFilesBodyDataCustomRateType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MatterupdateFilesBodyDataCustomRateType(_type_)

        matterupdate_files_body_data_custom_rate = cls(
            rates=rates,
            type_=type_,
        )

        matterupdate_files_body_data_custom_rate.additional_properties = d
        return matterupdate_files_body_data_custom_rate

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
