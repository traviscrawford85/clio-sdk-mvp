from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matterupdate_data_body_data_statute_of_limitations_reminders_item_notification_method import (
        MatterupdateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod,
    )


T = TypeVar("T", bound="MatterupdateDataBodyDataStatuteOfLimitationsRemindersItem")


@_attrs_define
class MatterupdateDataBodyDataStatuteOfLimitationsRemindersItem:
    """
    Attributes:
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated Reminder is present, the Reminder is deleted from the Matter.
        duration_unit (Union[Unset, str]): Unit to measure the duration value in.
        duration_value (Union[Unset, int]): Time measured in `duration_unit` to remind user before the subject.
        id (Union[Unset, int]): The unique identifier for a single Reminder associated with the Matter. The keyword
            `null` is not valid for this field.
        notification_method (Union[Unset, MatterupdateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod]):
    """

    field_destroy: Union[Unset, bool] = UNSET
    duration_unit: Union[Unset, str] = UNSET
    duration_value: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    notification_method: Union[Unset, "MatterupdateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod"] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_destroy = self.field_destroy

        duration_unit = self.duration_unit

        duration_value = self.duration_value

        id = self.id

        notification_method: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.notification_method, Unset):
            notification_method = self.notification_method.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if duration_unit is not UNSET:
            field_dict["duration_unit"] = duration_unit
        if duration_value is not UNSET:
            field_dict["duration_value"] = duration_value
        if id is not UNSET:
            field_dict["id"] = id
        if notification_method is not UNSET:
            field_dict["notification_method"] = notification_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matterupdate_data_body_data_statute_of_limitations_reminders_item_notification_method import (
            MatterupdateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod,
        )

        d = dict(src_dict)
        field_destroy = d.pop("_destroy", UNSET)

        duration_unit = d.pop("duration_unit", UNSET)

        duration_value = d.pop("duration_value", UNSET)

        id = d.pop("id", UNSET)

        _notification_method = d.pop("notification_method", UNSET)
        notification_method: Union[Unset, MatterupdateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod]
        if isinstance(_notification_method, Unset):
            notification_method = UNSET
        else:
            notification_method = MatterupdateDataBodyDataStatuteOfLimitationsRemindersItemNotificationMethod.from_dict(
                _notification_method
            )

        matterupdate_data_body_data_statute_of_limitations_reminders_item = cls(
            field_destroy=field_destroy,
            duration_unit=duration_unit,
            duration_value=duration_value,
            id=id,
            notification_method=notification_method,
        )

        matterupdate_data_body_data_statute_of_limitations_reminders_item.additional_properties = d
        return matterupdate_data_body_data_statute_of_limitations_reminders_item

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
