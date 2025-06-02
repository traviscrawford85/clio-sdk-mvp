from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.line_item_base_kind import LineItemBaseKind
from ..models.line_item_base_type import LineItemBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LineItemBase")


@_attrs_define
class LineItemBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *LineItem* was created (as a ISO-8601 timestamp)
        date (Union[Unset, str]): The *LineItem* date (as a ISO-8601 date)
        description (Union[Unset, str]): The description for the *LineItem*
        etag (Union[Unset, str]): ETag for the *LineItem*
        group_ordering (Union[Unset, int]): The value to specify the ordering of the *LineItem* on a bill
        id (Union[Unset, int]): Unique identifier for the *LineItem*
        kind (Union[Unset, LineItemBaseKind]): The kind of *LineItem*
        note (Union[Unset, str]): The note attached to the *LineItem*
        price (Union[Unset, float]): The price of the *LineItem*
        quantity (Union[Unset, float]): The amount of hours for the *LineItem*
        secondary_tax (Union[Unset, float]): The secondary tax amount for the *LineItem*
        secondary_taxable (Union[Unset, bool]): Whether the *LineItem* is secondary taxable
        sub_total (Union[Unset, float]): The subtotal amount for the *LineItem*
        tax (Union[Unset, float]): The tax amount for the *LineItem*
        taxable (Union[Unset, bool]): Whether the *LineItem* is taxable
        total (Union[Unset, float]): The total amount for the *LineItem*
        type_ (Union[Unset, LineItemBaseType]): The type of the *LineItem*
        updated_at (Union[Unset, str]): The time the *LineItem* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    group_ordering: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    kind: Union[Unset, LineItemBaseKind] = UNSET
    note: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    secondary_tax: Union[Unset, float] = UNSET
    secondary_taxable: Union[Unset, bool] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tax: Union[Unset, float] = UNSET
    taxable: Union[Unset, bool] = UNSET
    total: Union[Unset, float] = UNSET
    type_: Union[Unset, LineItemBaseType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        date = self.date

        description = self.description

        etag = self.etag

        group_ordering = self.group_ordering

        id = self.id

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        note = self.note

        price = self.price

        quantity = self.quantity

        secondary_tax = self.secondary_tax

        secondary_taxable = self.secondary_taxable

        sub_total = self.sub_total

        tax = self.tax

        taxable = self.taxable

        total = self.total

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if etag is not UNSET:
            field_dict["etag"] = etag
        if group_ordering is not UNSET:
            field_dict["group_ordering"] = group_ordering
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if note is not UNSET:
            field_dict["note"] = note
        if price is not UNSET:
            field_dict["price"] = price
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if secondary_tax is not UNSET:
            field_dict["secondary_tax"] = secondary_tax
        if secondary_taxable is not UNSET:
            field_dict["secondary_taxable"] = secondary_taxable
        if sub_total is not UNSET:
            field_dict["sub_total"] = sub_total
        if tax is not UNSET:
            field_dict["tax"] = tax
        if taxable is not UNSET:
            field_dict["taxable"] = taxable
        if total is not UNSET:
            field_dict["total"] = total
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        group_ordering = d.pop("group_ordering", UNSET)

        id = d.pop("id", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, LineItemBaseKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = LineItemBaseKind(_kind)

        note = d.pop("note", UNSET)

        price = d.pop("price", UNSET)

        quantity = d.pop("quantity", UNSET)

        secondary_tax = d.pop("secondary_tax", UNSET)

        secondary_taxable = d.pop("secondary_taxable", UNSET)

        sub_total = d.pop("sub_total", UNSET)

        tax = d.pop("tax", UNSET)

        taxable = d.pop("taxable", UNSET)

        total = d.pop("total", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, LineItemBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = LineItemBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        line_item_base = cls(
            created_at=created_at,
            date=date,
            description=description,
            etag=etag,
            group_ordering=group_ordering,
            id=id,
            kind=kind,
            note=note,
            price=price,
            quantity=quantity,
            secondary_tax=secondary_tax,
            secondary_taxable=secondary_taxable,
            sub_total=sub_total,
            tax=tax,
            taxable=taxable,
            total=total,
            type_=type_,
            updated_at=updated_at,
        )

        line_item_base.additional_properties = d
        return line_item_base

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
