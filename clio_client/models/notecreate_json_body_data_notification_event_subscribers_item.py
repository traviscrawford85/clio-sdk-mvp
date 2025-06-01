from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NotecreateJsonBodyDataNotificationEventSubscribersItem")


@_attrs_define
class NotecreateJsonBodyDataNotificationEventSubscribersItem:
    """
    Attributes:
        user_id (str): The unique identifier for a User to be added as a notification event subscriber to the Note.
    """

    user_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        notecreate_json_body_data_notification_event_subscribers_item = cls(
            user_id=user_id,
        )

        notecreate_json_body_data_notification_event_subscribers_item.additional_properties = d
        return notecreate_json_body_data_notification_event_subscribers_item

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
