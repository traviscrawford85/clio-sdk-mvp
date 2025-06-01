from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relationship_contact import RelationshipContact
    from ..models.relationship_matter import RelationshipMatter


T = TypeVar("T", bound="Relationship")


@_attrs_define
class Relationship:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *Relationship* was created (as a ISO-8601 timestamp)
        description (Union[Unset, str]): A detailed description of the *Relationship*
        etag (Union[Unset, str]): ETag for the *Relationship*
        id (Union[Unset, int]): Unique identifier for the *Relationship*
        updated_at (Union[Unset, str]): The time the *Relationship* was last updated (as a ISO-8601 timestamp)
        contact (Union[Unset, RelationshipContact]):
        matter (Union[Unset, RelationshipMatter]):
    """

    created_at: Unset | str = UNSET
    description: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    updated_at: Unset | str = UNSET
    contact: Union[Unset, "RelationshipContact"] = UNSET
    matter: Union[Unset, "RelationshipMatter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        description = self.description

        etag = self.etag

        id = self.id

        updated_at = self.updated_at

        contact: Unset | dict[str, Any] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        matter: Unset | dict[str, Any] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if contact is not UNSET:
            field_dict["contact"] = contact
        if matter is not UNSET:
            field_dict["matter"] = matter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.relationship_contact import RelationshipContact
        from ..models.relationship_matter import RelationshipMatter

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _contact = d.pop("contact", UNSET)
        contact: Unset | RelationshipContact
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = RelationshipContact.from_dict(_contact)

        _matter = d.pop("matter", UNSET)
        matter: Unset | RelationshipMatter
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = RelationshipMatter.from_dict(_matter)

        relationship = cls(
            created_at=created_at,
            description=description,
            etag=etag,
            id=id,
            updated_at=updated_at,
            contact=contact,
            matter=matter,
        )

        relationship.additional_properties = d
        return relationship

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
