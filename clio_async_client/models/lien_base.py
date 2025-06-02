from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lien_base_lien_type import LienBaseLienType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LienBase")


@_attrs_define
class LienBase:
    """
    Attributes:
        amount (Union[Unset, float]): The amount for Lien
        created_at (Union[Unset, str]): The time the *Lien* was created (as a ISO-8601 timestamp)
        description (Union[Unset, str]): Lien description
        etag (Union[Unset, str]): ETag for the *Lien*
        id (Union[Unset, int]): Unique identifier for the *Lien*
        lien_type (Union[Unset, LienBaseLienType]): Lien type
        mark_as_lien (Union[Unset, bool]): Mark item as Lien
        updated_at (Union[Unset, str]): The time the *Lien* was last updated (as a ISO-8601 timestamp)
    """

    amount: Union[Unset, float] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    lien_type: Union[Unset, LienBaseLienType] = UNSET
    mark_as_lien: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        created_at = self.created_at

        description = self.description

        etag = self.etag

        id = self.id

        lien_type: Union[Unset, str] = UNSET
        if not isinstance(self.lien_type, Unset):
            lien_type = self.lien_type.value

        mark_as_lien = self.mark_as_lien

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if lien_type is not UNSET:
            field_dict["lien_type"] = lien_type
        if mark_as_lien is not UNSET:
            field_dict["mark_as_lien"] = mark_as_lien
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        _lien_type = d.pop("lien_type", UNSET)
        lien_type: Union[Unset, LienBaseLienType]
        if isinstance(_lien_type, Unset):
            lien_type = UNSET
        else:
            lien_type = LienBaseLienType(_lien_type)

        mark_as_lien = d.pop("mark_as_lien", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        lien_base = cls(
            amount=amount,
            created_at=created_at,
            description=description,
            etag=etag,
            id=id,
            lien_type=lien_type,
            mark_as_lien=mark_as_lien,
            updated_at=updated_at,
        )

        lien_base.additional_properties = d
        return lien_base

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
