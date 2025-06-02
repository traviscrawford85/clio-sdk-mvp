from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_base_type import ContactBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatterBillRecipientRecipient")


@_attrs_define
class MatterBillRecipientRecipient:
    """
    Attributes:
        client_connect_user_id (Union[Unset, int]): The ID for the Clio Connect user associated with this *Contact*
        clio_connect_email (Union[Unset, str]): Clio Connect email if the *Contact* is a ClioConnect User
        created_at (Union[Unset, str]): The time the *Contact* was created (as a ISO-8601 timestamp)
        date_of_birth (Union[Unset, str]): Date of birth
        etag (Union[Unset, str]): ETag for the *Contact*
        first_name (Union[Unset, str]): First name of the Person
        has_clio_for_clients_permission (Union[Unset, bool]): True if at least one resource has been shared with the
            contact using Clio for Clients.
        id (Union[Unset, int]): Unique identifier for the *Contact*
        initials (Union[Unset, str]): The initials of the *Contact*
        is_bill_recipient (Union[Unset, bool]): Whether the Contact is a bill recipient on at least one matter.
        is_client (Union[Unset, bool]): Whether or not the Contact is a client
        is_clio_for_client_user (Union[Unset, bool]): Whether or not this contact has client_login and client_user (can
            be created due to addition to client portal or client_share_permissions)
        is_co_counsel (Union[Unset, bool]): Whether or not the Contact has matters shared as co-counsel
        last_name (Union[Unset, str]): Last name of the Person
        ledes_client_id (Union[Unset, str]): LEDES client id of the Contact
        locked_clio_connect_email (Union[Unset, bool]): A boolean indicating if the ability to modify this *Contacts
            Clio connect email is locked.
        middle_name (Union[Unset, str]): Middle name of the Person
        name (Union[Unset, str]): The full name of the *Contact*
        prefix (Union[Unset, str]): The prefix of the *Contact* (Mr, Mrs, etc)
        primary_email_address (Union[Unset, str]): The primary email address associated with this *Contact*.
        primary_phone_number (Union[Unset, str]): The primary phone number associated with this *Contact*.
        sales_tax_number (Union[Unset, str]): The sales tax number of the *Contact*
        secondary_email_address (Union[Unset, str]): The secondary email address associated with this *Contact*.
        secondary_phone_number (Union[Unset, str]): The secondary phone number of the *Contact*.
        title (Union[Unset, str]): The designated title of the *Contact*
        type_ (Union[Unset, ContactBaseType]): The type of the *Contact*
        updated_at (Union[Unset, str]): The time the *Contact* was last updated (as a ISO-8601 timestamp)
    """

    client_connect_user_id: Union[Unset, int] = UNSET
    clio_connect_email: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    date_of_birth: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    has_clio_for_clients_permission: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    initials: Union[Unset, str] = UNSET
    is_bill_recipient: Union[Unset, bool] = UNSET
    is_client: Union[Unset, bool] = UNSET
    is_clio_for_client_user: Union[Unset, bool] = UNSET
    is_co_counsel: Union[Unset, bool] = UNSET
    last_name: Union[Unset, str] = UNSET
    ledes_client_id: Union[Unset, str] = UNSET
    locked_clio_connect_email: Union[Unset, bool] = UNSET
    middle_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    primary_email_address: Union[Unset, str] = UNSET
    primary_phone_number: Union[Unset, str] = UNSET
    sales_tax_number: Union[Unset, str] = UNSET
    secondary_email_address: Union[Unset, str] = UNSET
    secondary_phone_number: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, ContactBaseType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_connect_user_id = self.client_connect_user_id

        clio_connect_email = self.clio_connect_email

        created_at = self.created_at

        date_of_birth = self.date_of_birth

        etag = self.etag

        first_name = self.first_name

        has_clio_for_clients_permission = self.has_clio_for_clients_permission

        id = self.id

        initials = self.initials

        is_bill_recipient = self.is_bill_recipient

        is_client = self.is_client

        is_clio_for_client_user = self.is_clio_for_client_user

        is_co_counsel = self.is_co_counsel

        last_name = self.last_name

        ledes_client_id = self.ledes_client_id

        locked_clio_connect_email = self.locked_clio_connect_email

        middle_name = self.middle_name

        name = self.name

        prefix = self.prefix

        primary_email_address = self.primary_email_address

        primary_phone_number = self.primary_phone_number

        sales_tax_number = self.sales_tax_number

        secondary_email_address = self.secondary_email_address

        secondary_phone_number = self.secondary_phone_number

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
        if clio_connect_email is not UNSET:
            field_dict["clio_connect_email"] = clio_connect_email
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if etag is not UNSET:
            field_dict["etag"] = etag
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if has_clio_for_clients_permission is not UNSET:
            field_dict["has_clio_for_clients_permission"] = has_clio_for_clients_permission
        if id is not UNSET:
            field_dict["id"] = id
        if initials is not UNSET:
            field_dict["initials"] = initials
        if is_bill_recipient is not UNSET:
            field_dict["is_bill_recipient"] = is_bill_recipient
        if is_client is not UNSET:
            field_dict["is_client"] = is_client
        if is_clio_for_client_user is not UNSET:
            field_dict["is_clio_for_client_user"] = is_clio_for_client_user
        if is_co_counsel is not UNSET:
            field_dict["is_co_counsel"] = is_co_counsel
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if ledes_client_id is not UNSET:
            field_dict["ledes_client_id"] = ledes_client_id
        if locked_clio_connect_email is not UNSET:
            field_dict["locked_clio_connect_email"] = locked_clio_connect_email
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
        if sales_tax_number is not UNSET:
            field_dict["sales_tax_number"] = sales_tax_number
        if secondary_email_address is not UNSET:
            field_dict["secondary_email_address"] = secondary_email_address
        if secondary_phone_number is not UNSET:
            field_dict["secondary_phone_number"] = secondary_phone_number
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

        clio_connect_email = d.pop("clio_connect_email", UNSET)

        created_at = d.pop("created_at", UNSET)

        date_of_birth = d.pop("date_of_birth", UNSET)

        etag = d.pop("etag", UNSET)

        first_name = d.pop("first_name", UNSET)

        has_clio_for_clients_permission = d.pop("has_clio_for_clients_permission", UNSET)

        id = d.pop("id", UNSET)

        initials = d.pop("initials", UNSET)

        is_bill_recipient = d.pop("is_bill_recipient", UNSET)

        is_client = d.pop("is_client", UNSET)

        is_clio_for_client_user = d.pop("is_clio_for_client_user", UNSET)

        is_co_counsel = d.pop("is_co_counsel", UNSET)

        last_name = d.pop("last_name", UNSET)

        ledes_client_id = d.pop("ledes_client_id", UNSET)

        locked_clio_connect_email = d.pop("locked_clio_connect_email", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        name = d.pop("name", UNSET)

        prefix = d.pop("prefix", UNSET)

        primary_email_address = d.pop("primary_email_address", UNSET)

        primary_phone_number = d.pop("primary_phone_number", UNSET)

        sales_tax_number = d.pop("sales_tax_number", UNSET)

        secondary_email_address = d.pop("secondary_email_address", UNSET)

        secondary_phone_number = d.pop("secondary_phone_number", UNSET)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ContactBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ContactBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        matter_bill_recipient_recipient = cls(
            client_connect_user_id=client_connect_user_id,
            clio_connect_email=clio_connect_email,
            created_at=created_at,
            date_of_birth=date_of_birth,
            etag=etag,
            first_name=first_name,
            has_clio_for_clients_permission=has_clio_for_clients_permission,
            id=id,
            initials=initials,
            is_bill_recipient=is_bill_recipient,
            is_client=is_client,
            is_clio_for_client_user=is_clio_for_client_user,
            is_co_counsel=is_co_counsel,
            last_name=last_name,
            ledes_client_id=ledes_client_id,
            locked_clio_connect_email=locked_clio_connect_email,
            middle_name=middle_name,
            name=name,
            prefix=prefix,
            primary_email_address=primary_email_address,
            primary_phone_number=primary_phone_number,
            sales_tax_number=sales_tax_number,
            secondary_email_address=secondary_email_address,
            secondary_phone_number=secondary_phone_number,
            title=title,
            type_=type_,
            updated_at=updated_at,
        )

        matter_bill_recipient_recipient.additional_properties = d
        return matter_bill_recipient_recipient

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
