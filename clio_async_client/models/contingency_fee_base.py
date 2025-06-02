from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContingencyFeeBase")


@_attrs_define
class ContingencyFeeBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *ContingencyFee* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *ContingencyFee*
        id (Union[Unset, int]): Unique identifier for the *ContingencyFee*
        show_contingency_award (Union[Unset, bool]): Whether the *ContingencyFee* is posted or on a bill
        ed_at (Union[Unset, str]): The time the *ContingencyFee* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    show_contingency_award: Union[Unset, bool] = UNSET
    ed_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        etag = self.etag

        id = self.id

        show_contingency_award = self.show_contingency_award

        ed_at = self.ed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if show_contingency_award is not UNSET:
            field_dict["show_contingency_award"] = show_contingency_award
        if ed_at is not UNSET:
            field_dict["ed_at"] = ed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        show_contingency_award = d.pop("show_contingency_award", UNSET)

        ed_at = d.pop("ed_at", UNSET)

        contingency_fee_base = cls(
            created_at=created_at,
            etag=etag,
            id=id,
            show_contingency_award=show_contingency_award,
            ed_at=ed_at,
        )

        contingency_fee_base.additional_properties = d
        return contingency_fee_base

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
