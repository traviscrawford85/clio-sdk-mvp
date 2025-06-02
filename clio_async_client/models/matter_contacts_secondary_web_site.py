from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.web_site_base_name import WebSiteBaseName
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatterContactsSecondaryWebSite")


@_attrs_define
class MatterContactsSecondaryWebSite:
    """
    Attributes:
        address (Union[Unset, str]): The address of the *WebSite*
        created_at (Union[Unset, str]): The time the *WebSite* was created (as a ISO-8601 timestamp)
        default_web_site (Union[Unset, bool]): Whether it is the default for this contact
        etag (Union[Unset, str]): ETag for the *WebSite*
        id (Union[Unset, int]): Unique identifier for the *WebSite*
        name (Union[Unset, WebSiteBaseName]): The type of *WebSite* it is
        updated_at (Union[Unset, str]): The time the *WebSite* was last updated (as a ISO-8601 timestamp)
    """

    address: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    default_web_site: Union[Unset, bool] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, WebSiteBaseName] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        created_at = self.created_at

        default_web_site = self.default_web_site

        etag = self.etag

        id = self.id

        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if default_web_site is not UNSET:
            field_dict["default_web_site"] = default_web_site
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        created_at = d.pop("created_at", UNSET)

        default_web_site = d.pop("default_web_site", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        _name = d.pop("name", UNSET)
        name: Union[Unset, WebSiteBaseName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = WebSiteBaseName(_name)

        updated_at = d.pop("updated_at", UNSET)

        matter_contacts_secondary_web_site = cls(
            address=address,
            created_at=created_at,
            default_web_site=default_web_site,
            etag=etag,
            id=id,
            name=name,
            updated_at=updated_at,
        )

        matter_contacts_secondary_web_site.additional_properties = d
        return matter_contacts_secondary_web_site

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
