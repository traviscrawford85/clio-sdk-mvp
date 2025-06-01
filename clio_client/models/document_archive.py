from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.document_archive_base_state import DocumentArchiveBaseState
from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentArchive")


@_attrs_define
class DocumentArchive:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *DocumentArchive* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *DocumentArchive*
        id (Union[Unset, int]): Unique identifier for the *DocumentArchive*
        message (Union[Unset, str]): A message to indicate why the DocumentArchive didn't complete.
        progress (Union[Unset, float]): The percent completion of the DocumentArchive.
        size (Union[Unset, int]): The size of the DocumentArchive in bytes.
        state (Union[Unset, DocumentArchiveBaseState]): The current state of the DocumentArchive.
        updated_at (Union[Unset, str]): The time the *DocumentArchive* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    message: Unset | str = UNSET
    progress: Unset | float = UNSET
    size: Unset | int = UNSET
    state: Unset | DocumentArchiveBaseState = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        etag = self.etag

        id = self.id

        message = self.message

        progress = self.progress

        size = self.size

        state: Unset | str = UNSET
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
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if progress is not UNSET:
            field_dict["progress"] = progress
        if size is not UNSET:
            field_dict["size"] = size
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

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        progress = d.pop("progress", UNSET)

        size = d.pop("size", UNSET)

        _state = d.pop("state", UNSET)
        state: Unset | DocumentArchiveBaseState
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DocumentArchiveBaseState(_state)

        updated_at = d.pop("updated_at", UNSET)

        document_archive = cls(
            created_at=created_at,
            etag=etag,
            id=id,
            message=message,
            progress=progress,
            size=size,
            state=state,
            updated_at=updated_at,
        )

        document_archive.additional_properties = d
        return document_archive

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
