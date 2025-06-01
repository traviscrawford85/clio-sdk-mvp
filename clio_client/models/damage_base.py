from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.damage_base_damage_type import DamageBaseDamageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DamageBase")


@_attrs_define
class DamageBase:
    """
    Attributes:
        amount (Union[Unset, float]): Amount for Damage
        created_at (Union[Unset, str]): The time the *Damage* was created (as a ISO-8601 timestamp)
        damage_type (Union[Unset, DamageBaseDamageType]): Damage type of the record
        description (Union[Unset, str]): Description for Damage
        etag (Union[Unset, str]): ETag for the *Damage*
        id (Union[Unset, int]): Unique identifier for the *Damage*
        updated_at (Union[Unset, str]): The time the *Damage* was last updated (as a ISO-8601 timestamp)
    """

    amount: Unset | float = UNSET
    created_at: Unset | str = UNSET
    damage_type: Unset | DamageBaseDamageType = UNSET
    description: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        created_at = self.created_at

        damage_type: Unset | str = UNSET
        if not isinstance(self.damage_type, Unset):
            damage_type = self.damage_type.value

        description = self.description

        etag = self.etag

        id = self.id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if damage_type is not UNSET:
            field_dict["damage_type"] = damage_type
        if description is not UNSET:
            field_dict["description"] = description
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        created_at = d.pop("created_at", UNSET)

        _damage_type = d.pop("damage_type", UNSET)
        damage_type: Unset | DamageBaseDamageType
        if isinstance(_damage_type, Unset):
            damage_type = UNSET
        else:
            damage_type = DamageBaseDamageType(_damage_type)

        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        damage_base = cls(
            amount=amount,
            created_at=created_at,
            damage_type=damage_type,
            description=description,
            etag=etag,
            id=id,
            updated_at=updated_at,
        )

        damage_base.additional_properties = d
        return damage_base

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
