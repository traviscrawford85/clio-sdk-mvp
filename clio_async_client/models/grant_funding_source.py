from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grant_base import GrantBase


T = TypeVar("T", bound="GrantFundingSource")


@_attrs_define
class GrantFundingSource:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *GrantFundingSource* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *GrantFundingSource*
        id (Union[Unset, int]): Unique identifier for the *GrantFundingSource*
        name (Union[Unset, str]): The name of the *GrantFundingSource*
        updated_at (Union[Unset, str]): The time the *GrantFundingSource* was last updated (as a ISO-8601 timestamp)
        grants (Union[Unset, list['GrantBase']]): Grant
    """

    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    grants: Union[Unset, list["GrantBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        etag = self.etag

        id = self.id

        name = self.name

        updated_at = self.updated_at

        grants: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.grants, Unset):
            grants = []
            for grants_item_data in self.grants:
                grants_item = grants_item_data.to_dict()
                grants.append(grants_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if grants is not UNSET:
            field_dict["grants"] = grants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grant_base import GrantBase

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        grants = []
        _grants = d.pop("grants", UNSET)
        for grants_item_data in _grants or []:
            grants_item = GrantBase.from_dict(grants_item_data)

            grants.append(grants_item)

        grant_funding_source = cls(
            created_at=created_at,
            etag=etag,
            id=id,
            name=name,
            updated_at=updated_at,
            grants=grants,
        )

        grant_funding_source.additional_properties = d
        return grant_funding_source

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
