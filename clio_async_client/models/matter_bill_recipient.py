from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matter_bill_recipient_recipient import MatterBillRecipientRecipient


T = TypeVar("T", bound="MatterBillRecipient")


@_attrs_define
class MatterBillRecipient:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *MatterBillRecipient* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *MatterBillRecipient*
        id (Union[Unset, int]): Unique identifier for the *MatterBillRecipient*
        updated_at (Union[Unset, str]): The time the *MatterBillRecipient* was last updated (as a ISO-8601 timestamp)
        recipient (Union[Unset, MatterBillRecipientRecipient]):
    """

    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    recipient: Union[Unset, "MatterBillRecipientRecipient"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        etag = self.etag

        id = self.id

        updated_at = self.updated_at

        recipient: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recipient, Unset):
            recipient = self.recipient.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if recipient is not UNSET:
            field_dict["recipient"] = recipient

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matter_bill_recipient_recipient import (
            MatterBillRecipientRecipient,
        )

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _recipient = d.pop("recipient", UNSET)
        recipient: Union[Unset, MatterBillRecipientRecipient]
        if isinstance(_recipient, Unset):
            recipient = UNSET
        else:
            recipient = MatterBillRecipientRecipient.from_dict(_recipient)

        matter_bill_recipient = cls(
            created_at=created_at,
            etag=etag,
            id=id,
            updated_at=updated_at,
            recipient=recipient,
        )

        matter_bill_recipient.additional_properties = d
        return matter_bill_recipient

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
