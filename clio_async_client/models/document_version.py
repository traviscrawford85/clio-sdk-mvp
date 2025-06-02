from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_version_creator import DocumentVersionCreator
    from ..models.multipart import Multipart
    from ..models.multipart_header_base import MultipartHeaderBase


T = TypeVar("T", bound="DocumentVersion")


@_attrs_define
class DocumentVersion:
    """
    Attributes:
        content_type (Union[Unset, str]): A standard MIME type describing the format of the object data.
        created_at (Union[Unset, str]): The time the *DocumentVersion* was created (as a ISO-8601 timestamp)
        document_id (Union[Unset, int]): The ID of the parent document.
        etag (Union[Unset, str]): ETag for the *DocumentVersion*
        filename (Union[Unset, str]): The uploaded file name of the DocumentVersion.
        fully_uploaded (Union[Unset, bool]): True if the DocumentVersion is uploaded. False if the DocumentVersion is
            being uploaded.
        id (Union[Unset, int]): Unique identifier for the *DocumentVersion*
        put_url (Union[Unset, str]): A signed URL for uploading the file in a single operation. It expires in 10
            minutes. If the document is fully uploaded, the field is empty.
        received_at (Union[Unset, str]): The time the DocumentVersion was received (as an ISO-8601 timestamp)
        size (Union[Unset, int]): The size of the DocumentVersion in bytes.
        updated_at (Union[Unset, str]): The time the *DocumentVersion* was last updated (as a ISO-8601 timestamp)
        uuid (Union[Unset, str]): UUID associated with the DocumentVersion. UUID is required to mark a document fully
            uploaded.
        version_number (Union[Unset, int]): The ordered number of when this DocumentVersion was uploaded.
        creator (Union[Unset, DocumentVersionCreator]):
        multiparts (Union[Unset, list['Multipart']]): Multipart
        put_headers (Union[Unset, list['MultipartHeaderBase']]): MultipartHeader
    """

    content_type: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    document_id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    fully_uploaded: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    put_url: Union[Unset, str] = UNSET
    received_at: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    version_number: Union[Unset, int] = UNSET
    creator: Union[Unset, "DocumentVersionCreator"] = UNSET
    multiparts: Union[Unset, list["Multipart"]] = UNSET
    put_headers: Union[Unset, list["MultipartHeaderBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        created_at = self.created_at

        document_id = self.document_id

        etag = self.etag

        filename = self.filename

        fully_uploaded = self.fully_uploaded

        id = self.id

        put_url = self.put_url

        received_at = self.received_at

        size = self.size

        updated_at = self.updated_at

        uuid = self.uuid

        version_number = self.version_number

        creator: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        multiparts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.multiparts, Unset):
            multiparts = []
            for multiparts_item_data in self.multiparts:
                multiparts_item = multiparts_item_data.to_dict()
                multiparts.append(multiparts_item)

        put_headers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.put_headers, Unset):
            put_headers = []
            for put_headers_item_data in self.put_headers:
                put_headers_item = put_headers_item_data.to_dict()
                put_headers.append(put_headers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if filename is not UNSET:
            field_dict["filename"] = filename
        if fully_uploaded is not UNSET:
            field_dict["fully_uploaded"] = fully_uploaded
        if id is not UNSET:
            field_dict["id"] = id
        if put_url is not UNSET:
            field_dict["put_url"] = put_url
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if size is not UNSET:
            field_dict["size"] = size
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if version_number is not UNSET:
            field_dict["version_number"] = version_number
        if creator is not UNSET:
            field_dict["creator"] = creator
        if multiparts is not UNSET:
            field_dict["multiparts"] = multiparts
        if put_headers is not UNSET:
            field_dict["put_headers"] = put_headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_version_creator import DocumentVersionCreator
        from ..models.multipart import Multipart
        from ..models.multipart_header_base import MultipartHeaderBase

        d = dict(src_dict)
        content_type = d.pop("content_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        document_id = d.pop("document_id", UNSET)

        etag = d.pop("etag", UNSET)

        filename = d.pop("filename", UNSET)

        fully_uploaded = d.pop("fully_uploaded", UNSET)

        id = d.pop("id", UNSET)

        put_url = d.pop("put_url", UNSET)

        received_at = d.pop("received_at", UNSET)

        size = d.pop("size", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        uuid = d.pop("uuid", UNSET)

        version_number = d.pop("version_number", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: Union[Unset, DocumentVersionCreator]
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = DocumentVersionCreator.from_dict(_creator)

        multiparts = []
        _multiparts = d.pop("multiparts", UNSET)
        for multiparts_item_data in _multiparts or []:
            multiparts_item = Multipart.from_dict(multiparts_item_data)

            multiparts.append(multiparts_item)

        put_headers = []
        _put_headers = d.pop("put_headers", UNSET)
        for put_headers_item_data in _put_headers or []:
            put_headers_item = MultipartHeaderBase.from_dict(put_headers_item_data)

            put_headers.append(put_headers_item)

        document_version = cls(
            content_type=content_type,
            created_at=created_at,
            document_id=document_id,
            etag=etag,
            filename=filename,
            fully_uploaded=fully_uploaded,
            id=id,
            put_url=put_url,
            received_at=received_at,
            size=size,
            updated_at=updated_at,
            uuid=uuid,
            version_number=version_number,
            creator=creator,
            multiparts=multiparts,
            put_headers=put_headers,
        )

        document_version.additional_properties = d
        return document_version

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
