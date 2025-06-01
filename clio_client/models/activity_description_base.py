from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityDescriptionBase")


@_attrs_define
class ActivityDescriptionBase:
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        activity_description_base = cls(
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
        )

        activity_description_base.additional_properties = d
        return activity_description_base

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
