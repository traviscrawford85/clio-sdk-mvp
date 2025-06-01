from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.linked_folder_base_type import LinkedFolderBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedFolderBase")


@_attrs_define
class LinkedFolderBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *Folder* was created (as a ISO-8601 timestamp)
        deleted_at (Union[Unset, str]): The time the *Folder* was deleted (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *Folder*
        id (Union[Unset, int]): Unique identifier for the *Folder*
        locked (Union[Unset, bool]): Whether or not the Folder is locked. Locked Folder cannot be modified
        name (Union[Unset, str]): The name of the *Folder*
        root (Union[Unset, bool]): Whether or not the Folder is the root folder. There is only one root folder per
            account
        type_ (Union[Unset, LinkedFolderBaseType]): The type of the *Folder*
        updated_at (Union[Unset, str]): The time the *Folder* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Unset | str = UNSET
    deleted_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    locked: Unset | bool = UNSET
    name: Unset | str = UNSET
    root: Unset | bool = UNSET
    type_: Unset | LinkedFolderBaseType = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        deleted_at = self.deleted_at

        etag = self.etag

        id = self.id

        locked = self.locked

        name = self.name

        root = self.root

        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if locked is not UNSET:
            field_dict["locked"] = locked
        if name is not UNSET:
            field_dict["name"] = name
        if root is not UNSET:
            field_dict["root"] = root
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        deleted_at = d.pop("deleted_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        locked = d.pop("locked", UNSET)

        name = d.pop("name", UNSET)

        root = d.pop("root", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Unset | LinkedFolderBaseType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = LinkedFolderBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        linked_folder_base = cls(
            created_at=created_at,
            deleted_at=deleted_at,
            etag=etag,
            id=id,
            locked=locked,
            name=name,
            root=root,
            type_=type_,
            updated_at=updated_at,
        )

        linked_folder_base.additional_properties = d
        return linked_folder_base

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
