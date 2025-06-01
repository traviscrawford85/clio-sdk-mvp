from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentAutomationDocumentTemplate")


@_attrs_define
class DocumentAutomationDocumentTemplate:
    """
    Attributes:
        content_type (Union[Unset, str]): A standard MIME type describing the format of the object data.
        created_at (Union[Unset, str]): The time the *DocumentTemplate* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *DocumentTemplate*
        filename (Union[Unset, str]): The name of the original file that was uploaded
        id (Union[Unset, int]): Unique identifier for the *DocumentTemplate*
        size (Union[Unset, int]): The size in bytes of the template
        updated_at (Union[Unset, str]): The time the *DocumentTemplate* was last updated (as a ISO-8601 timestamp)
    """

    content_type: Unset | str = UNSET
    created_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    filename: Unset | str = UNSET
    id: Unset | int = UNSET
    size: Unset | int = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        created_at = self.created_at

        etag = self.etag

        filename = self.filename

        id = self.id

        size = self.size

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if filename is not UNSET:
            field_dict["filename"] = filename
        if id is not UNSET:
            field_dict["id"] = id
        if size is not UNSET:
            field_dict["size"] = size
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("content_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        filename = d.pop("filename", UNSET)

        id = d.pop("id", UNSET)

        size = d.pop("size", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        document_automation_document_template = cls(
            content_type=content_type,
            created_at=created_at,
            etag=etag,
            filename=filename,
            id=id,
            size=size,
            updated_at=updated_at,
        )

        document_automation_document_template.additional_properties = d
        return document_automation_document_template

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
