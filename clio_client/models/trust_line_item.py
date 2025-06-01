from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trust_line_item_bill import TrustLineItemBill
    from ..models.trust_line_item_client import TrustLineItemClient
    from ..models.trust_line_item_matter import TrustLineItemMatter


T = TypeVar("T", bound="TrustLineItem")


@_attrs_define
class TrustLineItem:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *TrustLineItem* was created (as a ISO-8601 timestamp)
        date (Union[Unset, str]): The date of the *TrustLineItem* (as a ISO-8601 date)
        etag (Union[Unset, str]): ETag for the *TrustLineItem*
        id (Union[Unset, int]): Unique identifier for the *TrustLineItem*
        note (Union[Unset, str]): Note for the *TrustLineItem*
        total (Union[Unset, float]): The total amount for the *TrustLineItem*
        updated_at (Union[Unset, str]): The time the *TrustLineItem* was last updated (as a ISO-8601 timestamp)
        bill (Union[Unset, TrustLineItemBill]):
        client (Union[Unset, TrustLineItemClient]):
        matter (Union[Unset, TrustLineItemMatter]):
    """

    created_at: Unset | str = UNSET
    date: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    note: Unset | str = UNSET
    total: Unset | float = UNSET
    updated_at: Unset | str = UNSET
    bill: Union[Unset, "TrustLineItemBill"] = UNSET
    client: Union[Unset, "TrustLineItemClient"] = UNSET
    matter: Union[Unset, "TrustLineItemMatter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        date = self.date

        etag = self.etag

        id = self.id

        note = self.note

        total = self.total

        updated_at = self.updated_at

        bill: Unset | dict[str, Any] = UNSET
        if not isinstance(self.bill, Unset):
            bill = self.bill.to_dict()

        client: Unset | dict[str, Any] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        matter: Unset | dict[str, Any] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if date is not UNSET:
            field_dict["date"] = date
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if note is not UNSET:
            field_dict["note"] = note
        if total is not UNSET:
            field_dict["total"] = total
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if bill is not UNSET:
            field_dict["bill"] = bill
        if client is not UNSET:
            field_dict["client"] = client
        if matter is not UNSET:
            field_dict["matter"] = matter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trust_line_item_bill import TrustLineItemBill
        from ..models.trust_line_item_client import TrustLineItemClient
        from ..models.trust_line_item_matter import TrustLineItemMatter

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        note = d.pop("note", UNSET)

        total = d.pop("total", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _bill = d.pop("bill", UNSET)
        bill: Unset | TrustLineItemBill
        if isinstance(_bill, Unset):
            bill = UNSET
        else:
            bill = TrustLineItemBill.from_dict(_bill)

        _client = d.pop("client", UNSET)
        client: Unset | TrustLineItemClient
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = TrustLineItemClient.from_dict(_client)

        _matter = d.pop("matter", UNSET)
        matter: Unset | TrustLineItemMatter
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = TrustLineItemMatter.from_dict(_matter)

        trust_line_item = cls(
            created_at=created_at,
            date=date,
            etag=etag,
            id=id,
            note=note,
            total=total,
            updated_at=updated_at,
            bill=bill,
            client=client,
            matter=matter,
        )

        trust_line_item.additional_properties = d
        return trust_line_item

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
