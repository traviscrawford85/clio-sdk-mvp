from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatterStage")


@_attrs_define
class MatterStage:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *MatterStage* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *MatterStage*
        id (Union[Unset, int]): Unique identifier for the *MatterStage*
        name (Union[Unset, str]): The name of the *MatterStage*
        order (Union[Unset, int]): The order of the matter stage within a practice area
        practice_area_id (Union[Unset, str]): Practice Area ID
        updated_at (Union[Unset, str]): The time the *MatterStage* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, int] = UNSET
    practice_area_id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        etag = self.etag

        id = self.id

        name = self.name

        order = self.order

        practice_area_id = self.practice_area_id

        updated_at = self.updated_at

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
        if order is not UNSET:
            field_dict["order"] = order
        if practice_area_id is not UNSET:
            field_dict["practice_area_id"] = practice_area_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        practice_area_id = d.pop("practice_area_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        matter_stage = cls(
            created_at=created_at,
            etag=etag,
            id=id,
            name=name,
            order=order,
            practice_area_id=practice_area_id,
            updated_at=updated_at,
        )

        matter_stage.additional_properties = d
        return matter_stage

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
