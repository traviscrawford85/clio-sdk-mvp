from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.matterupdate_files_body_data_statute_of_limitations_status import (
    MatterupdateFilesBodyDataStatuteOfLimitationsStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matterupdate_files_body_data_statute_of_limitations_reminders_item import (
        MatterupdateFilesBodyDataStatuteOfLimitationsRemindersItem,
    )


T = TypeVar("T", bound="MatterupdateFilesBodyDataStatuteOfLimitations")


@_attrs_define
class MatterupdateFilesBodyDataStatuteOfLimitations:
    """
    Attributes:
        due_at (Union[Unset, str]): The due date of Statute of Limitations. (Expects an ISO-8601 date).
        reminders (Union[Unset, list['MatterupdateFilesBodyDataStatuteOfLimitationsRemindersItem']]):
        status (Union[Unset, MatterupdateFilesBodyDataStatuteOfLimitationsStatus]): The task status of Statue of
            Limitations. Users without advanced tasks are allowed to select `Complete' or `Pending` only.
    """

    due_at: Union[Unset, str] = UNSET
    reminders: Union[Unset, list["MatterupdateFilesBodyDataStatuteOfLimitationsRemindersItem"]] = UNSET
    status: Union[Unset, MatterupdateFilesBodyDataStatuteOfLimitationsStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        due_at = self.due_at

        reminders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.reminders, Unset):
            reminders = []
            for reminders_item_data in self.reminders:
                reminders_item = reminders_item_data.to_dict()
                reminders.append(reminders_item)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if reminders is not UNSET:
            field_dict["reminders"] = reminders
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matterupdate_files_body_data_statute_of_limitations_reminders_item import (
            MatterupdateFilesBodyDataStatuteOfLimitationsRemindersItem,
        )

        d = dict(src_dict)
        due_at = d.pop("due_at", UNSET)

        reminders = []
        _reminders = d.pop("reminders", UNSET)
        for reminders_item_data in _reminders or []:
            reminders_item = MatterupdateFilesBodyDataStatuteOfLimitationsRemindersItem.from_dict(reminders_item_data)

            reminders.append(reminders_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, MatterupdateFilesBodyDataStatuteOfLimitationsStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MatterupdateFilesBodyDataStatuteOfLimitationsStatus(_status)

        matterupdate_files_body_data_statute_of_limitations = cls(
            due_at=due_at,
            reminders=reminders,
            status=status,
        )

        matterupdate_files_body_data_statute_of_limitations.additional_properties = d
        return matterupdate_files_body_data_statute_of_limitations

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
