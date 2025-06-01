from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.related_contacts_base_type import RelatedContactsBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RelatedContactsBase")


@_attrs_define
class RelatedContactsBase:
    """
    Attributes:
        client_connect_user_id (Union[Unset, int]): The client connect ID of the contacts associated user
        contact_id (Union[Unset, int]): The id of the *RelatedContacts*
        created_at (Union[Unset, str]): The time the *RelatedContacts* was created (as a ISO-8601 timestamp)
        first_name (Union[Unset, str]): First name of the Person
        id (Union[Unset, int]): Unique identifier for the *RelatedContacts*
        initials (Union[Unset, str]): The initials of the *RelatedContacts*
        is_matter_client (Union[Unset, bool]): Whether or not the RelatedContacts is also the client of the matter
        last_name (Union[Unset, str]): Last name of the Person
        middle_name (Union[Unset, str]): Middle name of the Person
        name (Union[Unset, str]): The full name of the *RelatedContacts*
        prefix (Union[Unset, str]): The prefix of the *RelatedContacts* (Mr, Mrs, etc)
        primary_email_address (Union[Unset, str]): The primary email address of related contact
        primary_phone_number (Union[Unset, str]): The primary phone number of related contact
        title (Union[Unset, str]): The designated title of the *RelatedContacts*
        type_ (Union[Unset, RelatedContactsBaseType]): The type of the *RelatedContacts*
        updated_at (Union[Unset, str]): The time the *RelatedContacts* was last updated (as a ISO-8601 timestamp)
    """

    client_connect_user_id: Unset | int = UNSET
    contact_id: Unset | int = UNSET
    created_at: Unset | str = UNSET
    first_name: Unset | str = UNSET
    id: Unset | int = UNSET
    initials: Unset | str = UNSET
    is_matter_client: Unset | bool = UNSET
    last_name: Unset | str = UNSET
    middle_name: Unset | str = UNSET
    name: Unset | str = UNSET
    prefix: Unset | str = UNSET
    primary_email_address: Unset | str = UNSET
    primary_phone_number: Unset | str = UNSET
    title: Unset | str = UNSET
    type_: Unset | RelatedContactsBaseType = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_connect_user_id = self.client_connect_user_id

        contact_id = self.contact_id

        created_at = self.created_at

        first_name = self.first_name

        id = self.id

        initials = self.initials

        is_matter_client = self.is_matter_client

        last_name = self.last_name

        middle_name = self.middle_name

        name = self.name

        prefix = self.prefix

        primary_email_address = self.primary_email_address

        primary_phone_number = self.primary_phone_number

        title = self.title

        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_connect_user_id is not UNSET:
            field_dict["client_connect_user_id"] = client_connect_user_id
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if initials is not UNSET:
            field_dict["initials"] = initials
        if is_matter_client is not UNSET:
            field_dict["is_matter_client"] = is_matter_client
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if name is not UNSET:
            field_dict["name"] = name
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if primary_email_address is not UNSET:
            field_dict["primary_email_address"] = primary_email_address
        if primary_phone_number is not UNSET:
            field_dict["primary_phone_number"] = primary_phone_number
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_connect_user_id = d.pop("client_connect_user_id", UNSET)

        contact_id = d.pop("contact_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        first_name = d.pop("first_name", UNSET)

        id = d.pop("id", UNSET)

        initials = d.pop("initials", UNSET)

        is_matter_client = d.pop("is_matter_client", UNSET)

        last_name = d.pop("last_name", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        name = d.pop("name", UNSET)

        prefix = d.pop("prefix", UNSET)

        primary_email_address = d.pop("primary_email_address", UNSET)

        primary_phone_number = d.pop("primary_phone_number", UNSET)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Unset | RelatedContactsBaseType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RelatedContactsBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        related_contacts_base = cls(
            client_connect_user_id=client_connect_user_id,
            contact_id=contact_id,
            created_at=created_at,
            first_name=first_name,
            id=id,
            initials=initials,
            is_matter_client=is_matter_client,
            last_name=last_name,
            middle_name=middle_name,
            name=name,
            prefix=prefix,
            primary_email_address=primary_email_address,
            primary_phone_number=primary_phone_number,
            title=title,
            type_=type_,
            updated_at=updated_at,
        )

        related_contacts_base.additional_properties = d
        return related_contacts_base

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
