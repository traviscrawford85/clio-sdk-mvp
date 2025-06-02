from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_method_base_type import NotificationMethodBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationMethodBase")


@_attrs_define
class NotificationMethodBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *NotificationMethod* was created (as a ISO-8601 timestamp)
        email_address (Union[Unset, str]): Email address to send the notification to (only for email type)
        etag (Union[Unset, str]): ETag for the *NotificationMethod*
        id (Union[Unset, int]): Unique identifier for the *NotificationMethod*
        is_default_email_address (Union[Unset, bool]): A boolean that is returned only on notification method objects
            that are relevant e.g. Email notification or Alternative Email
        type_ (Union[Unset, NotificationMethodBaseType]): Human readable description of the type of notification
        updated_at (Union[Unset, str]): The time the *NotificationMethod* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    is_default_email_address: Union[Unset, bool] = UNSET
    type_: Union[Unset, NotificationMethodBaseType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        email_address = self.email_address

        etag = self.etag

        id = self.id

        is_default_email_address = self.is_default_email_address

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if email_address is not UNSET:
            field_dict["email_address"] = email_address
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if is_default_email_address is not UNSET:
            field_dict["is_default_email_address"] = is_default_email_address
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        email_address = d.pop("email_address", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        is_default_email_address = d.pop("is_default_email_address", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, NotificationMethodBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = NotificationMethodBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        notification_method_base = cls(
            created_at=created_at,
            email_address=email_address,
            etag=etag,
            id=id,
            is_default_email_address=is_default_email_address,
            type_=type_,
            updated_at=updated_at,
        )

        notification_method_base.additional_properties = d
        return notification_method_base

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
