from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.document_base_type import DocumentBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentBase")


@_attrs_define
class DocumentBase:
    """
    Attributes:
        content_type (Union[Unset, str]): The uploaded file content type
        created_at (Union[Unset, str]): The time the *Document* was created (as a ISO-8601 timestamp)
        deleted_at (Union[Unset, str]): The time the *Document* was deleted (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *Document*
        filename (Union[Unset, str]): The uploaded file name of the latest document version.
        id (Union[Unset, int]): Unique identifier for the *Document*
        locked (Union[Unset, bool]): Whether or not the Document is locked. Locked Document cannot be modified
        name (Union[Unset, str]): The name of the Document
        received_at (Union[Unset, str]): The time the last document version was received (as an ISO-8601 timestamp)
        size (Union[Unset, int]): The file size
        type_ (Union[Unset, DocumentBaseType]): The type of the *Document*
        updated_at (Union[Unset, str]): The time the *Document* was last updated (as a ISO-8601 timestamp)
    """

    content_type: Unset | str = UNSET
    created_at: Unset | str = UNSET
    deleted_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    filename: Unset | str = UNSET
    id: Unset | int = UNSET
    locked: Unset | bool = UNSET
    name: Unset | str = UNSET
    received_at: Unset | str = UNSET
    size: Unset | int = UNSET
    type_: Unset | DocumentBaseType = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        created_at = self.created_at

        deleted_at = self.deleted_at

        etag = self.etag

        filename = self.filename

        id = self.id

        locked = self.locked

        name = self.name

        received_at = self.received_at

        size = self.size

        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if filename is not UNSET:
            field_dict["filename"] = filename
        if id is not UNSET:
            field_dict["id"] = id
        if locked is not UNSET:
            field_dict["locked"] = locked
        if name is not UNSET:
            field_dict["name"] = name
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if size is not UNSET:
            field_dict["size"] = size
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("content_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        deleted_at = d.pop("deleted_at", UNSET)

        etag = d.pop("etag", UNSET)

        filename = d.pop("filename", UNSET)

        id = d.pop("id", UNSET)

        locked = d.pop("locked", UNSET)

        name = d.pop("name", UNSET)

        received_at = d.pop("received_at", UNSET)

        size = d.pop("size", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Unset | DocumentBaseType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DocumentBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        document_base = cls(
            content_type=content_type,
            created_at=created_at,
            deleted_at=deleted_at,
            etag=etag,
            filename=filename,
            id=id,
            locked=locked,
            name=name,
            received_at=received_at,
            size=size,
            type_=type_,
            updated_at=updated_at,
        )

        document_base.additional_properties = d
        return document_base

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
