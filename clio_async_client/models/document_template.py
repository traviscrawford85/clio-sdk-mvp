from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_template_document_category import (
        DocumentTemplateDocumentCategory,
    )
    from ..models.document_template_last_modified_by import (
        DocumentTemplateLastModifiedBy,
    )


T = TypeVar("T", bound="DocumentTemplate")


@_attrs_define
class DocumentTemplate:
    """
    Attributes:
        content_type (Union[Unset, str]): A standard MIME type describing the format of the object data.
        created_at (Union[Unset, str]): The time the *DocumentTemplate* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *DocumentTemplate*
        filename (Union[Unset, str]): The name of the original file that was uploaded
        id (Union[Unset, int]): Unique identifier for the *DocumentTemplate*
        size (Union[Unset, int]): The size in bytes of the template
        updated_at (Union[Unset, str]): The time the *DocumentTemplate* was last updated (as a ISO-8601 timestamp)
        document_category (Union[Unset, DocumentTemplateDocumentCategory]):
        last_modified_by (Union[Unset, DocumentTemplateLastModifiedBy]):
    """

    content_type: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    size: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    document_category: Union[Unset, "DocumentTemplateDocumentCategory"] = UNSET
    last_modified_by: Union[Unset, "DocumentTemplateLastModifiedBy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        created_at = self.created_at

        etag = self.etag

        filename = self.filename

        id = self.id

        size = self.size

        updated_at = self.updated_at

        document_category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_category, Unset):
            document_category = self.document_category.to_dict()

        last_modified_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_modified_by, Unset):
            last_modified_by = self.last_modified_by.to_dict()

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
        if document_category is not UNSET:
            field_dict["document_category"] = document_category
        if last_modified_by is not UNSET:
            field_dict["last_modified_by"] = last_modified_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_template_document_category import (
            DocumentTemplateDocumentCategory,
        )
        from ..models.document_template_last_modified_by import (
            DocumentTemplateLastModifiedBy,
        )

        d = dict(src_dict)
        content_type = d.pop("content_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        filename = d.pop("filename", UNSET)

        id = d.pop("id", UNSET)

        size = d.pop("size", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _document_category = d.pop("document_category", UNSET)
        document_category: Union[Unset, DocumentTemplateDocumentCategory]
        if isinstance(_document_category, Unset):
            document_category = UNSET
        else:
            document_category = DocumentTemplateDocumentCategory.from_dict(_document_category)

        _last_modified_by = d.pop("last_modified_by", UNSET)
        last_modified_by: Union[Unset, DocumentTemplateLastModifiedBy]
        if isinstance(_last_modified_by, Unset):
            last_modified_by = UNSET
        else:
            last_modified_by = DocumentTemplateLastModifiedBy.from_dict(_last_modified_by)

        document_template = cls(
            content_type=content_type,
            created_at=created_at,
            etag=etag,
            filename=filename,
            id=id,
            size=size,
            updated_at=updated_at,
            document_category=document_category,
            last_modified_by=last_modified_by,
        )

        document_template.additional_properties = d
        return document_template

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
