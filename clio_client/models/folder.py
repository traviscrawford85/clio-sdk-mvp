from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.folder_base_type import FolderBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_property_base import ExternalPropertyBase
    from ..models.folder_contact import FolderContact
    from ..models.folder_creator import FolderCreator
    from ..models.folder_document_category import FolderDocumentCategory
    from ..models.folder_group import FolderGroup
    from ..models.folder_latest_document_version import FolderLatestDocumentVersion
    from ..models.folder_matter import FolderMatter
    from ..models.folder_parent import FolderParent


T = TypeVar("T", bound="Folder")


@_attrs_define
class Folder:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *Folder* was created (as a ISO-8601 timestamp)
        deleted_at (Union[Unset, str]): The time the *Folder* was deleted (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *Folder*
        id (Union[Unset, int]): Unique identifier for the *Folder*
        locked (Union[Unset, bool]): Whether or not the Folder is locked. Locked Folder cannot be modified
        name (Union[Unset, str]): The name of the Folder
        root (Union[Unset, bool]): Whether or not the Folder is the root folder. There is only one root folder per
            account
        type_ (Union[Unset, FolderBaseType]): The type of the *Folder*
        updated_at (Union[Unset, str]): The time the *Folder* was last updated (as a ISO-8601 timestamp)
        contact (Union[Unset, FolderContact]):
        creator (Union[Unset, FolderCreator]):
        document_category (Union[Unset, FolderDocumentCategory]):
        external_properties (Union[Unset, list['ExternalPropertyBase']]): ExternalProperty
        group (Union[Unset, FolderGroup]):
        latest_document_version (Union[Unset, FolderLatestDocumentVersion]):
        matter (Union[Unset, FolderMatter]):
        parent (Union[Unset, FolderParent]):
    """

    created_at: Unset | str = UNSET
    deleted_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    locked: Unset | bool = UNSET
    name: Unset | str = UNSET
    root: Unset | bool = UNSET
    type_: Unset | FolderBaseType = UNSET
    updated_at: Unset | str = UNSET
    contact: Union[Unset, "FolderContact"] = UNSET
    creator: Union[Unset, "FolderCreator"] = UNSET
    document_category: Union[Unset, "FolderDocumentCategory"] = UNSET
    external_properties: Unset | list["ExternalPropertyBase"] = UNSET
    group: Union[Unset, "FolderGroup"] = UNSET
    latest_document_version: Union[Unset, "FolderLatestDocumentVersion"] = UNSET
    matter: Union[Unset, "FolderMatter"] = UNSET
    parent: Union[Unset, "FolderParent"] = UNSET
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

        contact: Unset | dict[str, Any] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        creator: Unset | dict[str, Any] = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        document_category: Unset | dict[str, Any] = UNSET
        if not isinstance(self.document_category, Unset):
            document_category = self.document_category.to_dict()

        external_properties: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.external_properties, Unset):
            external_properties = []
            for external_properties_item_data in self.external_properties:
                external_properties_item = external_properties_item_data.to_dict()
                external_properties.append(external_properties_item)

        group: Unset | dict[str, Any] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        latest_document_version: Unset | dict[str, Any] = UNSET
        if not isinstance(self.latest_document_version, Unset):
            latest_document_version = self.latest_document_version.to_dict()

        matter: Unset | dict[str, Any] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        parent: Unset | dict[str, Any] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

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
        if contact is not UNSET:
            field_dict["contact"] = contact
        if creator is not UNSET:
            field_dict["creator"] = creator
        if document_category is not UNSET:
            field_dict["document_category"] = document_category
        if external_properties is not UNSET:
            field_dict["external_properties"] = external_properties
        if group is not UNSET:
            field_dict["group"] = group
        if latest_document_version is not UNSET:
            field_dict["latest_document_version"] = latest_document_version
        if matter is not UNSET:
            field_dict["matter"] = matter
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_property_base import ExternalPropertyBase
        from ..models.folder_contact import FolderContact
        from ..models.folder_creator import FolderCreator
        from ..models.folder_document_category import FolderDocumentCategory
        from ..models.folder_group import FolderGroup
        from ..models.folder_latest_document_version import FolderLatestDocumentVersion
        from ..models.folder_matter import FolderMatter
        from ..models.folder_parent import FolderParent

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        deleted_at = d.pop("deleted_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        locked = d.pop("locked", UNSET)

        name = d.pop("name", UNSET)

        root = d.pop("root", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Unset | FolderBaseType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FolderBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        _contact = d.pop("contact", UNSET)
        contact: Unset | FolderContact
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = FolderContact.from_dict(_contact)

        _creator = d.pop("creator", UNSET)
        creator: Unset | FolderCreator
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = FolderCreator.from_dict(_creator)

        _document_category = d.pop("document_category", UNSET)
        document_category: Unset | FolderDocumentCategory
        if isinstance(_document_category, Unset):
            document_category = UNSET
        else:
            document_category = FolderDocumentCategory.from_dict(_document_category)

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = ExternalPropertyBase.from_dict(
                external_properties_item_data
            )

            external_properties.append(external_properties_item)

        _group = d.pop("group", UNSET)
        group: Unset | FolderGroup
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = FolderGroup.from_dict(_group)

        _latest_document_version = d.pop("latest_document_version", UNSET)
        latest_document_version: Unset | FolderLatestDocumentVersion
        if isinstance(_latest_document_version, Unset):
            latest_document_version = UNSET
        else:
            latest_document_version = FolderLatestDocumentVersion.from_dict(
                _latest_document_version
            )

        _matter = d.pop("matter", UNSET)
        matter: Unset | FolderMatter
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = FolderMatter.from_dict(_matter)

        _parent = d.pop("parent", UNSET)
        parent: Unset | FolderParent
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = FolderParent.from_dict(_parent)

        folder = cls(
            created_at=created_at,
            deleted_at=deleted_at,
            etag=etag,
            id=id,
            locked=locked,
            name=name,
            root=root,
            type_=type_,
            updated_at=updated_at,
            contact=contact,
            creator=creator,
            document_category=document_category,
            external_properties=external_properties,
            group=group,
            latest_document_version=latest_document_version,
            matter=matter,
            parent=parent,
        )

        folder.additional_properties = d
        return folder

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
