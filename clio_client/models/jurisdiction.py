from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_type_base import ServiceTypeBase


T = TypeVar("T", bound="Jurisdiction")


@_attrs_define
class Jurisdiction:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *Jurisdiction* was created (as a ISO-8601 timestamp)
        default (Union[Unset, bool]): Whether the *Jurisdiction* is default for the current user
        description (Union[Unset, str]): Description
        display_timezone (Union[Unset, str]): Formatted IANA timezone with UTC offset
        etag (Union[Unset, str]): ETag for the *Jurisdiction*
        id (Union[Unset, int]): Unique identifier for the *Jurisdiction*
        is_local_timezone (Union[Unset, bool]): Boolean value for when the timezone is in the local users timezone
        system_id (Union[Unset, int]): Server ID
        updated_at (Union[Unset, str]): The time the *Jurisdiction* was last updated (as a ISO-8601 timestamp)
        valid_subscription (Union[Unset, bool]): Boolean value for whether the user has the jurisdictions
        service_types (Union[Unset, list['ServiceTypeBase']]): ServiceType
    """

    created_at: Unset | str = UNSET
    default: Unset | bool = UNSET
    description: Unset | str = UNSET
    display_timezone: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    is_local_timezone: Unset | bool = UNSET
    system_id: Unset | int = UNSET
    updated_at: Unset | str = UNSET
    valid_subscription: Unset | bool = UNSET
    service_types: Unset | list["ServiceTypeBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        default = self.default

        description = self.description

        display_timezone = self.display_timezone

        etag = self.etag

        id = self.id

        is_local_timezone = self.is_local_timezone

        system_id = self.system_id

        updated_at = self.updated_at

        valid_subscription = self.valid_subscription

        service_types: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.service_types, Unset):
            service_types = []
            for service_types_item_data in self.service_types:
                service_types_item = service_types_item_data.to_dict()
                service_types.append(service_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if display_timezone is not UNSET:
            field_dict["display_timezone"] = display_timezone
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if is_local_timezone is not UNSET:
            field_dict["is_local_timezone"] = is_local_timezone
        if system_id is not UNSET:
            field_dict["system_id"] = system_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if valid_subscription is not UNSET:
            field_dict["valid_subscription"] = valid_subscription
        if service_types is not UNSET:
            field_dict["service_types"] = service_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_type_base import ServiceTypeBase

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        display_timezone = d.pop("display_timezone", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        is_local_timezone = d.pop("is_local_timezone", UNSET)

        system_id = d.pop("system_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        valid_subscription = d.pop("valid_subscription", UNSET)

        service_types = []
        _service_types = d.pop("service_types", UNSET)
        for service_types_item_data in _service_types or []:
            service_types_item = ServiceTypeBase.from_dict(service_types_item_data)

            service_types.append(service_types_item)

        jurisdiction = cls(
            created_at=created_at,
            default=default,
            description=description,
            display_timezone=display_timezone,
            etag=etag,
            id=id,
            is_local_timezone=is_local_timezone,
            system_id=system_id,
            updated_at=updated_at,
            valid_subscription=valid_subscription,
            service_types=service_types,
        )

        jurisdiction.additional_properties = d
        return jurisdiction

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
