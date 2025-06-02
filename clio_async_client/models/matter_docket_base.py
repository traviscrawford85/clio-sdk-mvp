from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatterDocketBase")


@_attrs_define
class MatterDocketBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *MatterDocket* was created (as a ISO-8601 timestamp)
        deleted_at (Union[Unset, str]): The time the *MatterDocket* was deleted (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *MatterDocket*
        id (Union[Unset, int]): Unique identifier for the *MatterDocket*
        name (Union[Unset, str]): The name of the *MatterDocket*
        start_date (Union[Unset, str]): The date the *MatterDocket* will start (as a ISO-8601 date)
        start_time (Union[Unset, str]): The time the *MatterDocket* will start, required for specific triggers (as a
            ISO-8601 timestamp)
        status (Union[Unset, str]): The status of the *MatterDocket* creation
        updated_at (Union[Unset, str]): The time the *MatterDocket* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Union[Unset, str] = UNSET
    deleted_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    start_time: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        deleted_at = self.deleted_at

        etag = self.etag

        id = self.id

        name = self.name

        start_date = self.start_date

        start_time = self.start_time

        status = self.status

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        deleted_at = d.pop("deleted_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        start_date = d.pop("start_date", UNSET)

        start_time = d.pop("start_time", UNSET)

        status = d.pop("status", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        matter_docket_base = cls(
            created_at=created_at,
            deleted_at=deleted_at,
            etag=etag,
            id=id,
            name=name,
            start_date=start_date,
            start_time=start_time,
            status=status,
            updated_at=updated_at,
        )

        matter_docket_base.additional_properties = d
        return matter_docket_base

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
