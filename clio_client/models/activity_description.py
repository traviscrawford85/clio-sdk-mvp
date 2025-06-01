from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_description_rate import ActivityDescriptionRate
    from ..models.activity_description_utbms_activity import (
        ActivityDescriptionUtbmsActivity,
    )
    from ..models.activity_description_utbms_task import ActivityDescriptionUtbmsTask
    from ..models.group_base import GroupBase


T = TypeVar("T", bound="ActivityDescription")


@_attrs_define
class ActivityDescription:
    """
    Attributes:
        accessible_to_user (Union[Unset, bool]): Determines if activity description is accessible to user
        category_type (Union[Unset, str]): Activity category rate type. Either hourly or flat fee
        created_at (Union[Unset, str]): The time the *ActivityDescription* was created (as a ISO-8601 timestamp)
        default (Union[Unset, bool]): Whether it is the user's default activity description
        etag (Union[Unset, str]): ETag for the *ActivityDescription*
        id (Union[Unset, int]): Unique identifier for the *ActivityDescription*
        name (Union[Unset, str]): The name of the *ActivityDescription*
        type_ (Union[Unset, str]): The type of the *ActivityDescription*
        updated_at (Union[Unset, str]): The time the *ActivityDescription* was last updated (as a ISO-8601 timestamp)
        utbms_activity_id (Union[Unset, int]): The UTBMS activity id if the *ActivityDescription* is a UTBMS activity
            description
        utbms_task_id (Union[Unset, int]): The UTBMS activity task id if attached to a UTBMS activity description
        utbms_task_name (Union[Unset, str]): The UTBMS activity task name if attached to a UTBMS activity description
        visible_to_co_counsel (Union[Unset, bool]): A toggle that determines if a co-counsel user of the firm can have
            access to this activity description
        xero_service_code (Union[Unset, str]): Custom Xero service code for this activity description
        groups (Union[Unset, list['GroupBase']]): Group
        rate (Union[Unset, ActivityDescriptionRate]):
        utbms_activity (Union[Unset, ActivityDescriptionUtbmsActivity]):
        utbms_task (Union[Unset, ActivityDescriptionUtbmsTask]):
    """

    accessible_to_user: Unset | bool = UNSET
    category_type: Unset | str = UNSET
    created_at: Unset | str = UNSET
    default: Unset | bool = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    name: Unset | str = UNSET
    type_: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    utbms_activity_id: Unset | int = UNSET
    utbms_task_id: Unset | int = UNSET
    utbms_task_name: Unset | str = UNSET
    visible_to_co_counsel: Unset | bool = UNSET
    xero_service_code: Unset | str = UNSET
    groups: Unset | list["GroupBase"] = UNSET
    rate: Union[Unset, "ActivityDescriptionRate"] = UNSET
    utbms_activity: Union[Unset, "ActivityDescriptionUtbmsActivity"] = UNSET
    utbms_task: Union[Unset, "ActivityDescriptionUtbmsTask"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accessible_to_user = self.accessible_to_user

        category_type = self.category_type

        created_at = self.created_at

        default = self.default

        etag = self.etag

        id = self.id

        name = self.name

        type_ = self.type_

        updated_at = self.updated_at

        utbms_activity_id = self.utbms_activity_id

        utbms_task_id = self.utbms_task_id

        utbms_task_name = self.utbms_task_name

        visible_to_co_counsel = self.visible_to_co_counsel

        xero_service_code = self.xero_service_code

        groups: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        rate: Unset | dict[str, Any] = UNSET
        if not isinstance(self.rate, Unset):
            rate = self.rate.to_dict()

        utbms_activity: Unset | dict[str, Any] = UNSET
        if not isinstance(self.utbms_activity, Unset):
            utbms_activity = self.utbms_activity.to_dict()

        utbms_task: Unset | dict[str, Any] = UNSET
        if not isinstance(self.utbms_task, Unset):
            utbms_task = self.utbms_task.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accessible_to_user is not UNSET:
            field_dict["accessible_to_user"] = accessible_to_user
        if category_type is not UNSET:
            field_dict["category_type"] = category_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if default is not UNSET:
            field_dict["default"] = default
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
        if utbms_activity_id is not UNSET:
            field_dict["utbms_activity_id"] = utbms_activity_id
        if utbms_task_id is not UNSET:
            field_dict["utbms_task_id"] = utbms_task_id
        if utbms_task_name is not UNSET:
            field_dict["utbms_task_name"] = utbms_task_name
        if visible_to_co_counsel is not UNSET:
            field_dict["visible_to_co_counsel"] = visible_to_co_counsel
        if xero_service_code is not UNSET:
            field_dict["xero_service_code"] = xero_service_code
        if groups is not UNSET:
            field_dict["groups"] = groups
        if rate is not UNSET:
            field_dict["rate"] = rate
        if utbms_activity is not UNSET:
            field_dict["utbms_activity"] = utbms_activity
        if utbms_task is not UNSET:
            field_dict["utbms_task"] = utbms_task

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_description_rate import ActivityDescriptionRate
        from ..models.activity_description_utbms_activity import (
            ActivityDescriptionUtbmsActivity,
        )
        from ..models.activity_description_utbms_task import (
            ActivityDescriptionUtbmsTask,
        )
        from ..models.group_base import GroupBase

        d = dict(src_dict)
        accessible_to_user = d.pop("accessible_to_user", UNSET)

        category_type = d.pop("category_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        default = d.pop("default", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        utbms_activity_id = d.pop("utbms_activity_id", UNSET)

        utbms_task_id = d.pop("utbms_task_id", UNSET)

        utbms_task_name = d.pop("utbms_task_name", UNSET)

        visible_to_co_counsel = d.pop("visible_to_co_counsel", UNSET)

        xero_service_code = d.pop("xero_service_code", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = GroupBase.from_dict(groups_item_data)

            groups.append(groups_item)

        _rate = d.pop("rate", UNSET)
        rate: Unset | ActivityDescriptionRate
        if isinstance(_rate, Unset):
            rate = UNSET
        else:
            rate = ActivityDescriptionRate.from_dict(_rate)

        _utbms_activity = d.pop("utbms_activity", UNSET)
        utbms_activity: Unset | ActivityDescriptionUtbmsActivity
        if isinstance(_utbms_activity, Unset):
            utbms_activity = UNSET
        else:
            utbms_activity = ActivityDescriptionUtbmsActivity.from_dict(_utbms_activity)

        _utbms_task = d.pop("utbms_task", UNSET)
        utbms_task: Unset | ActivityDescriptionUtbmsTask
        if isinstance(_utbms_task, Unset):
            utbms_task = UNSET
        else:
            utbms_task = ActivityDescriptionUtbmsTask.from_dict(_utbms_task)

        activity_description = cls(
            accessible_to_user=accessible_to_user,
            category_type=category_type,
            created_at=created_at,
            default=default,
            etag=etag,
            id=id,
            name=name,
            type_=type_,
            updated_at=updated_at,
            utbms_activity_id=utbms_activity_id,
            utbms_task_id=utbms_task_id,
            utbms_task_name=utbms_task_name,
            visible_to_co_counsel=visible_to_co_counsel,
            xero_service_code=xero_service_code,
            groups=groups,
            rate=rate,
            utbms_activity=utbms_activity,
            utbms_task=utbms_task,
        )

        activity_description.additional_properties = d
        return activity_description

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
