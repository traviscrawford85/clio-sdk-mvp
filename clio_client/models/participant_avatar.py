from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParticipantAvatar")


@_attrs_define
class ParticipantAvatar:
    """
    Attributes:
        field_destroy (Union[Unset, bool]): Whether to destroy the *Avatar*
        created_at (Union[Unset, str]): The time the *Avatar* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *Avatar*
        id (Union[Unset, int]): Unique identifier for the *Avatar*
        updated_at (Union[Unset, str]): The time the *Avatar* was last updated (as a ISO-8601 timestamp)
        url (Union[Unset, str]): The URL for the *Avatar*
    """

    field_destroy: Unset | bool = UNSET
    created_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    updated_at: Unset | str = UNSET
    url: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_destroy = self.field_destroy

        created_at = self.created_at

        etag = self.etag

        id = self.id

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_destroy = d.pop("_destroy", UNSET)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        participant_avatar = cls(
            field_destroy=field_destroy,
            created_at=created_at,
            etag=etag,
            id=id,
            updated_at=updated_at,
            url=url,
        )

        participant_avatar.additional_properties = d
        return participant_avatar

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
