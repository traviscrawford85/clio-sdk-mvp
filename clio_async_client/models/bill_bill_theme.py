from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillBillTheme")


@_attrs_define
class BillBillTheme:
    """
    Attributes:
        account_id (Union[Unset, int]): The account number the *BillTheme* belongs to
        config (Union[Unset, str]): The configuration of the *BillTheme*
        created_at (Union[Unset, str]): The time the *BillTheme* was created (as a ISO-8601 timestamp)
        default (Union[Unset, bool]): Whether the *BillTheme* is the default for its account
        etag (Union[Unset, str]): ETag for the *BillTheme*
        id (Union[Unset, int]): Unique identifier for the *BillTheme*
        name (Union[Unset, str]): The name of the *BillTheme*
        updated_at (Union[Unset, str]): The time the *BillTheme* was last updated (as a ISO-8601 timestamp)
    """

    account_id: Union[Unset, int] = UNSET
    config: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    default: Union[Unset, bool] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        config = self.config

        created_at = self.created_at

        default = self.default

        etag = self.etag

        id = self.id

        name = self.name

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if config is not UNSET:
            field_dict["config"] = config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if default is not UNSET:
            field_dict["default"] = default
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
        account_id = d.pop("account_id", UNSET)

        config = d.pop("config", UNSET)

        created_at = d.pop("created_at", UNSET)

        default = d.pop("default", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        bill_bill_theme = cls(
            account_id=account_id,
            config=config,
            created_at=created_at,
            default=default,
            etag=etag,
            id=id,
            name=name,
            updated_at=updated_at,
        )

        bill_bill_theme.additional_properties = d
        return bill_bill_theme

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
