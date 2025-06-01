from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatterDocketServiceType")


@_attrs_define
class MatterDocketServiceType:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *ServiceType* was created (as a ISO-8601 timestamp)
        default (Union[Unset, bool]): Whether *ServiceType* is default for the current user
        description (Union[Unset, str]): A detailed description of the *ServiceType*
        etag (Union[Unset, str]): ETag for the *ServiceType*
        id (Union[Unset, int]): Unique identifier for the *ServiceType*
        system_id (Union[Unset, int]): Server ID
        updated_at (Union[Unset, str]): The time the *ServiceType* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Unset | str = UNSET
    default: Unset | bool = UNSET
    description: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    system_id: Unset | int = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        default = self.default

        description = self.description

        etag = self.etag

        id = self.id

        system_id = self.system_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if system_id is not UNSET:
            field_dict["system_id"] = system_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        system_id = d.pop("system_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        matter_docket_service_type = cls(
            created_at=created_at,
            default=default,
            description=description,
            etag=etag,
            id=id,
            system_id=system_id,
            updated_at=updated_at,
        )

        matter_docket_service_type.additional_properties = d
        return matter_docket_service_type

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
