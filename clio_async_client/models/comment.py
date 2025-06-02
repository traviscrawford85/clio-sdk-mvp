from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_creator import CommentCreator
    from ..models.comment_document_version import CommentDocumentVersion


T = TypeVar("T", bound="Comment")


@_attrs_define
class Comment:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *Comment* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *Comment*
        id (Union[Unset, int]): Unique identifier for the *Comment*
        message (Union[Unset, str]): The content of the Comment
        updated_at (Union[Unset, str]): The time the *Comment* was last updated (as a ISO-8601 timestamp)
        creator (Union[Unset, CommentCreator]):
        document_version (Union[Unset, CommentDocumentVersion]):
    """

    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    creator: Union[Unset, "CommentCreator"] = UNSET
    document_version: Union[Unset, "CommentDocumentVersion"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        etag = self.etag

        id = self.id

        message = self.message

        updated_at = self.updated_at

        creator: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        document_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_version, Unset):
            document_version = self.document_version.to_dict()

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
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if creator is not UNSET:
            field_dict["creator"] = creator
        if document_version is not UNSET:
            field_dict["document_version"] = document_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment_creator import CommentCreator
        from ..models.comment_document_version import CommentDocumentVersion

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: Union[Unset, CommentCreator]
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = CommentCreator.from_dict(_creator)

        _document_version = d.pop("document_version", UNSET)
        document_version: Union[Unset, CommentDocumentVersion]
        if isinstance(_document_version, Unset):
            document_version = UNSET
        else:
            document_version = CommentDocumentVersion.from_dict(_document_version)

        comment = cls(
            created_at=created_at,
            etag=etag,
            id=id,
            message=message,
            updated_at=updated_at,
            creator=creator,
            document_version=document_version,
        )

        comment.additional_properties = d
        return comment

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
