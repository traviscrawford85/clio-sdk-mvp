from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrustRequestcreateJsonBodyDataMatterItem")


@_attrs_define
class TrustRequestcreateJsonBodyDataMatterItem:
    """
    Attributes:
        id (Union[Unset, int]): The matter id associated to the TrustRequest
        note (Union[Unset, str]): The client level TrustRequest note
        trust_amount (Union[Unset, int]): The matter level TrustRequest's amount
    """

    id: Union[Unset, int] = UNSET
    note: Union[Unset, str] = UNSET
    trust_amount: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        note = self.note

        trust_amount = self.trust_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if note is not UNSET:
            field_dict["note"] = note
        if trust_amount is not UNSET:
            field_dict["trust_amount"] = trust_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        note = d.pop("note", UNSET)

        trust_amount = d.pop("trust_amount", UNSET)

        trust_requestcreate_json_body_data_matter_item = cls(
            id=id,
            note=note,
            trust_amount=trust_amount,
        )

        trust_requestcreate_json_body_data_matter_item.additional_properties = d
        return trust_requestcreate_json_body_data_matter_item

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
