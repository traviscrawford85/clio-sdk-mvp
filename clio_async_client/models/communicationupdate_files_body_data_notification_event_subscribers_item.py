from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommunicationupdateFilesBodyDataNotificationEventSubscribersItem")


@_attrs_define
class CommunicationupdateFilesBodyDataNotificationEventSubscribersItem:
    """
    Attributes:
        field_destroy (Union[Unset, bool]): Whether or not the notification event subscriber should be deleted. Note:
            Only applicable to Phone Log Communications, invalid for other communication types.
        id (Union[Unset, int]): Unique id of this Communication. Note: Only applicable to Phone Log Communications,
            invalid for other communication types.
        user_id (Union[Unset, str]): The unique identifier for a User to be added as a notification event subscriber to
            the Phone Log Communication. Note: Only applicable to Phone Log Communications, invalid for other communication
            types.
    """

    field_destroy: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_destroy = self.field_destroy

        id = self.id

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_destroy = d.pop("_destroy", UNSET)

        id = d.pop("id", UNSET)

        user_id = d.pop("user_id", UNSET)

        communicationupdate_files_body_data_notification_event_subscribers_item = cls(
            field_destroy=field_destroy,
            id=id,
            user_id=user_id,
        )

        communicationupdate_files_body_data_notification_event_subscribers_item.additional_properties = d
        return communicationupdate_files_body_data_notification_event_subscribers_item

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
