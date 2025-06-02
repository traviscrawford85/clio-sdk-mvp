from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_transfer_client import BankTransferClient
    from ..models.bank_transfer_destination_account import (
        BankTransferDestinationAccount,
    )
    from ..models.bank_transfer_matter import BankTransferMatter
    from ..models.bank_transfer_source_account import BankTransferSourceAccount


T = TypeVar("T", bound="BankTransfer")


@_attrs_define
class BankTransfer:
    """
    Attributes:
        amount (Union[Unset, float]): The amount of the transfer.
        created_at (Union[Unset, str]): The time the *BankTransfer* was created (as a ISO-8601 timestamp)
        date (Union[Unset, str]): The date of the transfer.
        description (Union[Unset, str]): The description of the transfer.
        etag (Union[Unset, str]): ETag for the *BankTransfer*
        id (Union[Unset, int]): Unique identifier for the *BankTransfer*
        primary_authorizer (Union[Unset, str]): The primary authorizer of the transfer.
        secondary_authorizer (Union[Unset, str]): The secondary authorizer of the transfer.
        updated_at (Union[Unset, str]): The time the *BankTransfer* was last updated (as a ISO-8601 timestamp)
        client (Union[Unset, BankTransferClient]):
        destination_account (Union[Unset, BankTransferDestinationAccount]):
        matter (Union[Unset, BankTransferMatter]):
        source_account (Union[Unset, BankTransferSourceAccount]):
    """

    amount: Union[Unset, float] = UNSET
    created_at: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    primary_authorizer: Union[Unset, str] = UNSET
    secondary_authorizer: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    client: Union[Unset, "BankTransferClient"] = UNSET
    destination_account: Union[Unset, "BankTransferDestinationAccount"] = UNSET
    matter: Union[Unset, "BankTransferMatter"] = UNSET
    source_account: Union[Unset, "BankTransferSourceAccount"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        created_at = self.created_at

        date = self.date

        description = self.description

        etag = self.etag

        id = self.id

        primary_authorizer = self.primary_authorizer

        secondary_authorizer = self.secondary_authorizer

        updated_at = self.updated_at

        client: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        destination_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.destination_account, Unset):
            destination_account = self.destination_account.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        source_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source_account, Unset):
            source_account = self.source_account.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if primary_authorizer is not UNSET:
            field_dict["primary_authorizer"] = primary_authorizer
        if secondary_authorizer is not UNSET:
            field_dict["secondary_authorizer"] = secondary_authorizer
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if client is not UNSET:
            field_dict["client"] = client
        if destination_account is not UNSET:
            field_dict["destination_account"] = destination_account
        if matter is not UNSET:
            field_dict["matter"] = matter
        if source_account is not UNSET:
            field_dict["source_account"] = source_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bank_transfer_client import BankTransferClient
        from ..models.bank_transfer_destination_account import (
            BankTransferDestinationAccount,
        )
        from ..models.bank_transfer_matter import BankTransferMatter
        from ..models.bank_transfer_source_account import BankTransferSourceAccount

        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        primary_authorizer = d.pop("primary_authorizer", UNSET)

        secondary_authorizer = d.pop("secondary_authorizer", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _client = d.pop("client", UNSET)
        client: Union[Unset, BankTransferClient]
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = BankTransferClient.from_dict(_client)

        _destination_account = d.pop("destination_account", UNSET)
        destination_account: Union[Unset, BankTransferDestinationAccount]
        if isinstance(_destination_account, Unset):
            destination_account = UNSET
        else:
            destination_account = BankTransferDestinationAccount.from_dict(_destination_account)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, BankTransferMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = BankTransferMatter.from_dict(_matter)

        _source_account = d.pop("source_account", UNSET)
        source_account: Union[Unset, BankTransferSourceAccount]
        if isinstance(_source_account, Unset):
            source_account = UNSET
        else:
            source_account = BankTransferSourceAccount.from_dict(_source_account)

        bank_transfer = cls(
            amount=amount,
            created_at=created_at,
            date=date,
            description=description,
            etag=etag,
            id=id,
            primary_authorizer=primary_authorizer,
            secondary_authorizer=secondary_authorizer,
            updated_at=updated_at,
            client=client,
            destination_account=destination_account,
            matter=matter,
            source_account=source_account,
        )

        bank_transfer.additional_properties = d
        return bank_transfer

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
