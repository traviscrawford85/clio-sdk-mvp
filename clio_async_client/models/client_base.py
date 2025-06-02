from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_base_type import ClientBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientBase")


@_attrs_define
class ClientBase:
    """
    Attributes:
        client_connect_user_id (Union[Unset, int]): The client connect ID of the contacts associated user
        created_at (Union[Unset, str]): The time the *Client* was created (as a ISO-8601 timestamp)
        date_of_birth (Union[Unset, str]): Date of Birth
        first_name (Union[Unset, str]): First name of the Person
        id (Union[Unset, int]): Unique identifier for the *Client*
        initials (Union[Unset, str]): The initials of the *Client*
        is_matter_client (Union[Unset, bool]): Whether or not the Client is also the client of the matter
        last_name (Union[Unset, str]): Last name of the Person
        middle_name (Union[Unset, str]): Middle name of the Person
        name (Union[Unset, str]): The full name of the *Client*
        prefix (Union[Unset, str]): The prefix of the *Client* (Mr, Mrs, etc)
        primary_email_address (Union[Unset, str]): The primary email address of client
        primary_phone_number (Union[Unset, str]): The primary phone number of client
        title (Union[Unset, str]): The designated title of the *Client*
        type_ (Union[Unset, ClientBaseType]): The type of the *Client*
        updated_at (Union[Unset, str]): The time the *Client* was last updated (as a ISO-8601 timestamp)
    """

    client_connect_user_id: Union[Unset, int] = UNSET
    created_at: Union[Unset, str] = UNSET
    date_of_birth: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    initials: Union[Unset, str] = UNSET
    is_matter_client: Union[Unset, bool] = UNSET
    last_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    primary_email_address: Union[Unset, str] = UNSET
    primary_phone_number: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, ClientBaseType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_connect_user_id = self.client_connect_user_id

        created_at = self.created_at

        date_of_birth = self.date_of_birth

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

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_connect_user_id is not UNSET:
            field_dict["client_connect_user_id"] = client_connect_user_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
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

        created_at = d.pop("created_at", UNSET)

        date_of_birth = d.pop("date_of_birth", UNSET)

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
        type_: Union[Unset, ClientBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ClientBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        client_base = cls(
            client_connect_user_id=client_connect_user_id,
            created_at=created_at,
            date_of_birth=date_of_birth,
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

        client_base.additional_properties = d
        return client_base

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
