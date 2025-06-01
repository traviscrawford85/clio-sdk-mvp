from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.matter_custom_rate_base_type import MatterCustomRateBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatterCustomRateBase")


@_attrs_define
class MatterCustomRateBase:
    """
    Attributes:
        on_invoice (Union[Unset, bool]): Specifies if the matter's associated activity is posted or on a bill.
        type_ (Union[Unset, MatterCustomRateBaseType]): The type of the *MatterCustomRate*
    """

    on_invoice: Unset | bool = UNSET
    type_: Unset | MatterCustomRateBaseType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        on_invoice = self.on_invoice

        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if on_invoice is not UNSET:
            field_dict["on_invoice"] = on_invoice
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        on_invoice = d.pop("on_invoice", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Unset | MatterCustomRateBaseType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MatterCustomRateBaseType(_type_)

        matter_custom_rate_base = cls(
            on_invoice=on_invoice,
            type_=type_,
        )

        matter_custom_rate_base.additional_properties = d
        return matter_custom_rate_base

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
