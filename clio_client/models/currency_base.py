from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrencyBase")


@_attrs_define
class CurrencyBase:
    """
    Attributes:
        code (Union[Unset, str]): ISO 4217 code for the *Currency*
        created_at (Union[Unset, str]): The time the *Currency* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *Currency*
        id (Union[Unset, int]): Unique identifier for the *Currency*
        sign (Union[Unset, str]): Symbol used to denote monetary values using this *Currency*
        updated_at (Union[Unset, str]): The time the *Currency* was last updated (as a ISO-8601 timestamp)
    """

    code: Unset | str = UNSET
    created_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    sign: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        created_at = self.created_at

        etag = self.etag

        id = self.id

        sign = self.sign

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if sign is not UNSET:
            field_dict["sign"] = sign
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        sign = d.pop("sign", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        currency_base = cls(
            code=code,
            created_at=created_at,
            etag=etag,
            id=id,
            sign=sign,
            updated_at=updated_at,
        )

        currency_base.additional_properties = d
        return currency_base

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
