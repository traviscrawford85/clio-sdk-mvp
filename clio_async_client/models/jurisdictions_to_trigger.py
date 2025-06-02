from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JurisdictionsToTrigger")


@_attrs_define
class JurisdictionsToTrigger:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *JurisdictionsToTrigger* was created (as a ISO-8601 timestamp)
        description (Union[Unset, str]): A detailed description of the *JurisdictionsToTrigger*
        do_not_recalculate (Union[Unset, bool]): Whether the associated dates should not be recalculated
        etag (Union[Unset, str]): ETag for the *JurisdictionsToTrigger*
        id (Union[Unset, int]): Unique identifier for the *JurisdictionsToTrigger*
        is_requirements_required (Union[Unset, bool]): Whether the trigger has requirements
        is_served (Union[Unset, bool]): Whether the user must select a Date Offset (Service Type)
        system_id (Union[Unset, int]): Server id
        updated_at (Union[Unset, str]): The time the *JurisdictionsToTrigger* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    do_not_recalculate: Union[Unset, bool] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    is_requirements_required: Union[Unset, bool] = UNSET
    is_served: Union[Unset, bool] = UNSET
    system_id: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        description = self.description

        do_not_recalculate = self.do_not_recalculate

        etag = self.etag

        id = self.id

        is_requirements_required = self.is_requirements_required

        is_served = self.is_served

        system_id = self.system_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if do_not_recalculate is not UNSET:
            field_dict["do_not_recalculate"] = do_not_recalculate
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if is_requirements_required is not UNSET:
            field_dict["is_requirements_required"] = is_requirements_required
        if is_served is not UNSET:
            field_dict["is_served"] = is_served
        if system_id is not UNSET:
            field_dict["system_id"] = system_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        do_not_recalculate = d.pop("do_not_recalculate", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        is_requirements_required = d.pop("is_requirements_required", UNSET)

        is_served = d.pop("is_served", UNSET)

        system_id = d.pop("system_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        jurisdictions_to_trigger = cls(
            created_at=created_at,
            description=description,
            do_not_recalculate=do_not_recalculate,
            etag=etag,
            id=id,
            is_requirements_required=is_requirements_required,
            is_served=is_served,
            system_id=system_id,
            updated_at=updated_at,
        )

        jurisdictions_to_trigger.additional_properties = d
        return jurisdictions_to_trigger

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
