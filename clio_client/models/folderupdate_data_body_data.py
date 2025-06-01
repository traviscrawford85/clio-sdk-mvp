from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.folderupdate_data_body_data_document_category import (
        FolderupdateDataBodyDataDocumentCategory,
    )
    from ..models.folderupdate_data_body_data_external_properties_item import (
        FolderupdateDataBodyDataExternalPropertiesItem,
    )
    from ..models.folderupdate_data_body_data_parent import (
        FolderupdateDataBodyDataParent,
    )


T = TypeVar("T", bound="FolderupdateDataBodyData")


@_attrs_define
class FolderupdateDataBodyData:
    """
    Attributes:
        document_category (Union[Unset, FolderupdateDataBodyDataDocumentCategory]):
        external_properties (Union[Unset, list['FolderupdateDataBodyDataExternalPropertiesItem']]):
        name (Union[Unset, str]): Name of the Folder
        parent (Union[Unset, FolderupdateDataBodyDataParent]):
        restore (Union[Unset, bool]): Whether or not a trashed Folder should be restored.
    """

    document_category: Union[Unset, "FolderupdateDataBodyDataDocumentCategory"] = UNSET
    external_properties: (
        Unset | list["FolderupdateDataBodyDataExternalPropertiesItem"]
    ) = UNSET
    name: Unset | str = UNSET
    parent: Union[Unset, "FolderupdateDataBodyDataParent"] = UNSET
    restore: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_category: Unset | dict[str, Any] = UNSET
        if not isinstance(self.document_category, Unset):
            document_category = self.document_category.to_dict()

        external_properties: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.external_properties, Unset):
            external_properties = []
            for external_properties_item_data in self.external_properties:
                external_properties_item = external_properties_item_data.to_dict()
                external_properties.append(external_properties_item)

        name = self.name

        parent: Unset | dict[str, Any] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        restore = self.restore

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_category is not UNSET:
            field_dict["document_category"] = document_category
        if external_properties is not UNSET:
            field_dict["external_properties"] = external_properties
        if name is not UNSET:
            field_dict["name"] = name
        if parent is not UNSET:
            field_dict["parent"] = parent
        if restore is not UNSET:
            field_dict["restore"] = restore

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.folderupdate_data_body_data_document_category import (
            FolderupdateDataBodyDataDocumentCategory,
        )
        from ..models.folderupdate_data_body_data_external_properties_item import (
            FolderupdateDataBodyDataExternalPropertiesItem,
        )
        from ..models.folderupdate_data_body_data_parent import (
            FolderupdateDataBodyDataParent,
        )

        d = dict(src_dict)
        _document_category = d.pop("document_category", UNSET)
        document_category: Unset | FolderupdateDataBodyDataDocumentCategory
        if isinstance(_document_category, Unset):
            document_category = UNSET
        else:
            document_category = FolderupdateDataBodyDataDocumentCategory.from_dict(
                _document_category
            )

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = (
                FolderupdateDataBodyDataExternalPropertiesItem.from_dict(
                    external_properties_item_data
                )
            )

            external_properties.append(external_properties_item)

        name = d.pop("name", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Unset | FolderupdateDataBodyDataParent
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = FolderupdateDataBodyDataParent.from_dict(_parent)

        restore = d.pop("restore", UNSET)

        folderupdate_data_body_data = cls(
            document_category=document_category,
            external_properties=external_properties,
            name=name,
            parent=parent,
            restore=restore,
        )

        folderupdate_data_body_data.additional_properties = d
        return folderupdate_data_body_data

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
