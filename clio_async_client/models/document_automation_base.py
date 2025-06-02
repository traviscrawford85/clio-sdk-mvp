from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.document_automation_base_export_formats import (
    DocumentAutomationBaseExportFormats,
)
from ..models.document_automation_base_state import DocumentAutomationBaseState
from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentAutomationBase")


@_attrs_define
class DocumentAutomationBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *DocumentAutomation* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *DocumentAutomation*
        export_formats (Union[Unset, DocumentAutomationBaseExportFormats]): An array of what formats were requested
        filename (Union[Unset, str]): The name of the file being generated.
        id (Union[Unset, int]): Unique identifier for the *DocumentAutomation*
        state (Union[Unset, DocumentAutomationBaseState]): A text description of what the automation is currently doing
        updated_at (Union[Unset, str]): The time the *DocumentAutomation* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    export_formats: Union[Unset, DocumentAutomationBaseExportFormats] = UNSET
    filename: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    state: Union[Unset, DocumentAutomationBaseState] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        etag = self.etag

        export_formats: Union[Unset, str] = UNSET
        if not isinstance(self.export_formats, Unset):
            export_formats = self.export_formats.value

        filename = self.filename

        id = self.id

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if export_formats is not UNSET:
            field_dict["export_formats"] = export_formats
        if filename is not UNSET:
            field_dict["filename"] = filename
        if id is not UNSET:
            field_dict["id"] = id
        if state is not UNSET:
            field_dict["state"] = state
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        _export_formats = d.pop("export_formats", UNSET)
        export_formats: Union[Unset, DocumentAutomationBaseExportFormats]
        if isinstance(_export_formats, Unset):
            export_formats = UNSET
        else:
            export_formats = DocumentAutomationBaseExportFormats(_export_formats)

        filename = d.pop("filename", UNSET)

        id = d.pop("id", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, DocumentAutomationBaseState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DocumentAutomationBaseState(_state)

        updated_at = d.pop("updated_at", UNSET)

        document_automation_base = cls(
            created_at=created_at,
            etag=etag,
            export_formats=export_formats,
            filename=filename,
            id=id,
            state=state,
            updated_at=updated_at,
        )

        document_automation_base.additional_properties = d
        return document_automation_base

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
