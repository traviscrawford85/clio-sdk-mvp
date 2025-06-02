from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grant_grant_funding_source import GrantGrantFundingSource


T = TypeVar("T", bound="Grant")


@_attrs_define
class Grant:
    """
    Attributes:
        balance (Union[Unset, str]): Balance of the grant
        created_at (Union[Unset, str]): The time the *Grant* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *Grant*
        funding_code (Union[Unset, str]): Funding code of the grant
        funding_code_and_name (Union[Unset, str]): Funding code and name of the grant
        funding_source_name (Union[Unset, str]): Name of the funding source of the grant
        id (Union[Unset, int]): Unique identifier for the *Grant*
        name (Union[Unset, str]): The name of the *Grant*
        updated_at (Union[Unset, str]): The time the *Grant* was last updated (as a ISO-8601 timestamp)
        grant_funding_source (Union[Unset, GrantGrantFundingSource]):
    """

    balance: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    funding_code: Union[Unset, str] = UNSET
    funding_code_and_name: Union[Unset, str] = UNSET
    funding_source_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    grant_funding_source: Union[Unset, "GrantGrantFundingSource"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance = self.balance

        created_at = self.created_at

        etag = self.etag

        funding_code = self.funding_code

        funding_code_and_name = self.funding_code_and_name

        funding_source_name = self.funding_source_name

        id = self.id

        name = self.name

        updated_at = self.updated_at

        grant_funding_source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.grant_funding_source, Unset):
            grant_funding_source = self.grant_funding_source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if balance is not UNSET:
            field_dict["balance"] = balance
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if funding_code is not UNSET:
            field_dict["funding_code"] = funding_code
        if funding_code_and_name is not UNSET:
            field_dict["funding_code_and_name"] = funding_code_and_name
        if funding_source_name is not UNSET:
            field_dict["funding_source_name"] = funding_source_name
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if grant_funding_source is not UNSET:
            field_dict["grant_funding_source"] = grant_funding_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grant_grant_funding_source import GrantGrantFundingSource

        d = dict(src_dict)
        balance = d.pop("balance", UNSET)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        funding_code = d.pop("funding_code", UNSET)

        funding_code_and_name = d.pop("funding_code_and_name", UNSET)

        funding_source_name = d.pop("funding_source_name", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _grant_funding_source = d.pop("grant_funding_source", UNSET)
        grant_funding_source: Union[Unset, GrantGrantFundingSource]
        if isinstance(_grant_funding_source, Unset):
            grant_funding_source = UNSET
        else:
            grant_funding_source = GrantGrantFundingSource.from_dict(_grant_funding_source)

        grant = cls(
            balance=balance,
            created_at=created_at,
            etag=etag,
            funding_code=funding_code,
            funding_code_and_name=funding_code_and_name,
            funding_source_name=funding_source_name,
            id=id,
            name=name,
            updated_at=updated_at,
            grant_funding_source=grant_funding_source,
        )

        grant.additional_properties = d
        return grant

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
