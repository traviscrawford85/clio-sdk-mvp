from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.line_item_base_kind import LineItemBaseKind
from ..models.line_item_base_type import LineItemBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_item_activity import LineItemActivity
    from ..models.line_item_bill import LineItemBill
    from ..models.line_item_discount import LineItemDiscount
    from ..models.line_item_included_line_item_totals import (
        LineItemIncludedLineItemTotals,
    )
    from ..models.line_item_matter import LineItemMatter
    from ..models.line_item_user import LineItemUser


T = TypeVar("T", bound="LineItem")


@_attrs_define
class LineItem:
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
        activity (Union[Unset, LineItemActivity]):
        bill (Union[Unset, LineItemBill]):
        discount (Union[Unset, LineItemDiscount]):
        included_line_item_totals (Union[Unset, LineItemIncludedLineItemTotals]):
        matter (Union[Unset, LineItemMatter]):
        user (Union[Unset, LineItemUser]):
    """

    created_at: Unset | str = UNSET
    date: Unset | str = UNSET
    description: Unset | str = UNSET
    etag: Unset | str = UNSET
    group_ordering: Unset | int = UNSET
    id: Unset | int = UNSET
    kind: Unset | LineItemBaseKind = UNSET
    note: Unset | str = UNSET
    price: Unset | float = UNSET
    quantity: Unset | float = UNSET
    secondary_tax: Unset | float = UNSET
    secondary_taxable: Unset | bool = UNSET
    sub_total: Unset | float = UNSET
    tax: Unset | float = UNSET
    taxable: Unset | bool = UNSET
    total: Unset | float = UNSET
    type_: Unset | LineItemBaseType = UNSET
    updated_at: Unset | str = UNSET
    activity: Union[Unset, "LineItemActivity"] = UNSET
    bill: Union[Unset, "LineItemBill"] = UNSET
    discount: Union[Unset, "LineItemDiscount"] = UNSET
    included_line_item_totals: Union[Unset, "LineItemIncludedLineItemTotals"] = UNSET
    matter: Union[Unset, "LineItemMatter"] = UNSET
    user: Union[Unset, "LineItemUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        date = self.date

        description = self.description

        etag = self.etag

        group_ordering = self.group_ordering

        id = self.id

        kind: Unset | str = UNSET
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

        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        activity: Unset | dict[str, Any] = UNSET
        if not isinstance(self.activity, Unset):
            activity = self.activity.to_dict()

        bill: Unset | dict[str, Any] = UNSET
        if not isinstance(self.bill, Unset):
            bill = self.bill.to_dict()

        discount: Unset | dict[str, Any] = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        included_line_item_totals: Unset | dict[str, Any] = UNSET
        if not isinstance(self.included_line_item_totals, Unset):
            included_line_item_totals = self.included_line_item_totals.to_dict()

        matter: Unset | dict[str, Any] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        user: Unset | dict[str, Any] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

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
        if activity is not UNSET:
            field_dict["activity"] = activity
        if bill is not UNSET:
            field_dict["bill"] = bill
        if discount is not UNSET:
            field_dict["discount"] = discount
        if included_line_item_totals is not UNSET:
            field_dict["included_line_item_totals"] = included_line_item_totals
        if matter is not UNSET:
            field_dict["matter"] = matter
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.line_item_activity import LineItemActivity
        from ..models.line_item_bill import LineItemBill
        from ..models.line_item_discount import LineItemDiscount
        from ..models.line_item_included_line_item_totals import (
            LineItemIncludedLineItemTotals,
        )
        from ..models.line_item_matter import LineItemMatter
        from ..models.line_item_user import LineItemUser

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        group_ordering = d.pop("group_ordering", UNSET)

        id = d.pop("id", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Unset | LineItemBaseKind
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
        type_: Unset | LineItemBaseType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = LineItemBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        _activity = d.pop("activity", UNSET)
        activity: Unset | LineItemActivity
        if isinstance(_activity, Unset):
            activity = UNSET
        else:
            activity = LineItemActivity.from_dict(_activity)

        _bill = d.pop("bill", UNSET)
        bill: Unset | LineItemBill
        if isinstance(_bill, Unset):
            bill = UNSET
        else:
            bill = LineItemBill.from_dict(_bill)

        _discount = d.pop("discount", UNSET)
        discount: Unset | LineItemDiscount
        if isinstance(_discount, Unset):
            discount = UNSET
        else:
            discount = LineItemDiscount.from_dict(_discount)

        _included_line_item_totals = d.pop("included_line_item_totals", UNSET)
        included_line_item_totals: Unset | LineItemIncludedLineItemTotals
        if isinstance(_included_line_item_totals, Unset):
            included_line_item_totals = UNSET
        else:
            included_line_item_totals = LineItemIncludedLineItemTotals.from_dict(
                _included_line_item_totals
            )

        _matter = d.pop("matter", UNSET)
        matter: Unset | LineItemMatter
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = LineItemMatter.from_dict(_matter)

        _user = d.pop("user", UNSET)
        user: Unset | LineItemUser
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = LineItemUser.from_dict(_user)

        line_item = cls(
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
            activity=activity,
            bill=bill,
            discount=discount,
            included_line_item_totals=included_line_item_totals,
            matter=matter,
            user=user,
        )

        line_item.additional_properties = d
        return line_item

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
