from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attendee_base_type import AttendeeBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttendeeBase")


@_attrs_define
class AttendeeBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *Attendee* was created (as a ISO-8601 timestamp)
        email (Union[Unset, str]): If the Attendee is a User, this is the User's email. If the Attendee is a contact,
            this is the Contact's primary email address.
        enabled (Union[Unset, bool]): If the Attendee is a user, represents whether the user is enabled or disabled.
            Returns null if attendee is a Contact.
        etag (Union[Unset, str]): ETag for the *Attendee*
        id (Union[Unset, int]): Unique identifier for the *Attendee*
        name (Union[Unset, str]): The name of the *Attendee*
        type_ (Union[Unset, AttendeeBaseType]): The class name of the *Attendee*
        updated_at (Union[Unset, str]): The time the *Attendee* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Unset | str = UNSET
    email: Unset | str = UNSET
    enabled: Unset | bool = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    name: Unset | str = UNSET
    type_: Unset | AttendeeBaseType = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        email = self.email

        enabled = self.enabled

        etag = self.etag

        id = self.id

        name = self.name

        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if email is not UNSET:
            field_dict["email"] = email
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        email = d.pop("email", UNSET)

        enabled = d.pop("enabled", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Unset | AttendeeBaseType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AttendeeBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        attendee_base = cls(
            created_at=created_at,
            email=email,
            enabled=enabled,
            etag=etag,
            id=id,
            name=name,
            type_=type_,
            updated_at=updated_at,
        )

        attendee_base.additional_properties = d
        return attendee_base

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
