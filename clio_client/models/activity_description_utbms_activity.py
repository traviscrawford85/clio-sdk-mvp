from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.utbms_code_base_type import UtbmsCodeBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityDescriptionUtbmsActivity")


@_attrs_define
class ActivityDescriptionUtbmsActivity:
    """
    Attributes:
        code (Union[Unset, str]): The UTBMS code for the *UtbmsCode*
        created_at (Union[Unset, str]): The time the *UtbmsCode* was created (as a ISO-8601 timestamp)
        description (Union[Unset, str]): The UTBMS description for the *UtbmsCode*
        etag (Union[Unset, str]): ETag for the *UtbmsCode*
        id (Union[Unset, int]): Unique identifier for the *UtbmsCode*
        name (Union[Unset, str]): The name of the *UtbmsCode*
        type_ (Union[Unset, UtbmsCodeBaseType]): The type of the *UtbmsCode*
        updated_at (Union[Unset, str]): The time the *UtbmsCode* was last updated (as a ISO-8601 timestamp)
        utbms_set_id (Union[Unset, int]): Set id for the *UtbmsCode*
    """

    code: Unset | str = UNSET
    created_at: Unset | str = UNSET
    description: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    name: Unset | str = UNSET
    type_: Unset | UtbmsCodeBaseType = UNSET
    updated_at: Unset | str = UNSET
    utbms_set_id: Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        created_at = self.created_at

        description = self.description

        etag = self.etag

        id = self.id

        name = self.name

        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        utbms_set_id = self.utbms_set_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
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
        if utbms_set_id is not UNSET:
            field_dict["utbms_set_id"] = utbms_set_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Unset | UtbmsCodeBaseType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UtbmsCodeBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        utbms_set_id = d.pop("utbms_set_id", UNSET)

        activity_description_utbms_activity = cls(
            code=code,
            created_at=created_at,
            description=description,
            etag=etag,
            id=id,
            name=name,
            type_=type_,
            updated_at=updated_at,
            utbms_set_id=utbms_set_id,
        )

        activity_description_utbms_activity.additional_properties = d
        return activity_description_utbms_activity

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
