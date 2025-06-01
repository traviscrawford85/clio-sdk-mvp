from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.line_itemupdate_files_body_data_kind import (
    LineItemupdateFilesBodyDataKind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_itemupdate_files_body_data_activity import (
        LineItemupdateFilesBodyDataActivity,
    )
    from ..models.line_itemupdate_files_body_data_bill import (
        LineItemupdateFilesBodyDataBill,
    )
    from ..models.line_itemupdate_files_body_data_discount import (
        LineItemupdateFilesBodyDataDiscount,
    )
    from ..models.line_itemupdate_files_body_data_matter import (
        LineItemupdateFilesBodyDataMatter,
    )


T = TypeVar("T", bound="LineItemupdateFilesBodyData")


@_attrs_define
class LineItemupdateFilesBodyData:
    """
    Attributes:
        activity (Union[Unset, LineItemupdateFilesBodyDataActivity]):
        bill (Union[Unset, LineItemupdateFilesBodyDataBill]):
        date (Union[Unset, str]): The LineItem date.
        description (Union[Unset, str]): Description of the LineItem.
        discount (Union[Unset, LineItemupdateFilesBodyDataDiscount]):
        group_ordering (Union[Unset, int]): The LineItem group ordering.
        kind (Union[Unset, LineItemupdateFilesBodyDataKind]): The specific type of activity which is associated with the
            LineItem.
        matter (Union[Unset, LineItemupdateFilesBodyDataMatter]):
        note (Union[Unset, str]): The note attached to the LineItem.
        price (Union[Unset, float]): The price of the LineItem.
        quantity (Union[Unset, float]): Quantity of the LineItem.
        secondary_taxable (Union[Unset, bool]): Whether the LineItem is secondary taxable.
        taxable (Union[Unset, bool]): Whether the LineItem taxable.
        update_original_record (Union[Unset, bool]): Whether the associated activity will be updated.
    """

    activity: Union[Unset, "LineItemupdateFilesBodyDataActivity"] = UNSET
    bill: Union[Unset, "LineItemupdateFilesBodyDataBill"] = UNSET
    date: Unset | str = UNSET
    description: Unset | str = UNSET
    discount: Union[Unset, "LineItemupdateFilesBodyDataDiscount"] = UNSET
    group_ordering: Unset | int = UNSET
    kind: Unset | LineItemupdateFilesBodyDataKind = UNSET
    matter: Union[Unset, "LineItemupdateFilesBodyDataMatter"] = UNSET
    note: Unset | str = UNSET
    price: Unset | float = UNSET
    quantity: Unset | float = UNSET
    secondary_taxable: Unset | bool = UNSET
    taxable: Unset | bool = UNSET
    update_original_record: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity: Unset | dict[str, Any] = UNSET
        if not isinstance(self.activity, Unset):
            activity = self.activity.to_dict()

        bill: Unset | dict[str, Any] = UNSET
        if not isinstance(self.bill, Unset):
            bill = self.bill.to_dict()

        date = self.date

        description = self.description

        discount: Unset | dict[str, Any] = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        group_ordering = self.group_ordering

        kind: Unset | str = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        matter: Unset | dict[str, Any] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        note = self.note

        price = self.price

        quantity = self.quantity

        secondary_taxable = self.secondary_taxable

        taxable = self.taxable

        update_original_record = self.update_original_record

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity is not UNSET:
            field_dict["activity"] = activity
        if bill is not UNSET:
            field_dict["bill"] = bill
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if discount is not UNSET:
            field_dict["discount"] = discount
        if group_ordering is not UNSET:
            field_dict["group_ordering"] = group_ordering
        if kind is not UNSET:
            field_dict["kind"] = kind
        if matter is not UNSET:
            field_dict["matter"] = matter
        if note is not UNSET:
            field_dict["note"] = note
        if price is not UNSET:
            field_dict["price"] = price
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if secondary_taxable is not UNSET:
            field_dict["secondary_taxable"] = secondary_taxable
        if taxable is not UNSET:
            field_dict["taxable"] = taxable
        if update_original_record is not UNSET:
            field_dict["update_original_record"] = update_original_record

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.line_itemupdate_files_body_data_activity import (
            LineItemupdateFilesBodyDataActivity,
        )
        from ..models.line_itemupdate_files_body_data_bill import (
            LineItemupdateFilesBodyDataBill,
        )
        from ..models.line_itemupdate_files_body_data_discount import (
            LineItemupdateFilesBodyDataDiscount,
        )
        from ..models.line_itemupdate_files_body_data_matter import (
            LineItemupdateFilesBodyDataMatter,
        )

        d = dict(src_dict)
        _activity = d.pop("activity", UNSET)
        activity: Unset | LineItemupdateFilesBodyDataActivity
        if isinstance(_activity, Unset):
            activity = UNSET
        else:
            activity = LineItemupdateFilesBodyDataActivity.from_dict(_activity)

        _bill = d.pop("bill", UNSET)
        bill: Unset | LineItemupdateFilesBodyDataBill
        if isinstance(_bill, Unset):
            bill = UNSET
        else:
            bill = LineItemupdateFilesBodyDataBill.from_dict(_bill)

        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        _discount = d.pop("discount", UNSET)
        discount: Unset | LineItemupdateFilesBodyDataDiscount
        if isinstance(_discount, Unset):
            discount = UNSET
        else:
            discount = LineItemupdateFilesBodyDataDiscount.from_dict(_discount)

        group_ordering = d.pop("group_ordering", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Unset | LineItemupdateFilesBodyDataKind
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = LineItemupdateFilesBodyDataKind(_kind)

        _matter = d.pop("matter", UNSET)
        matter: Unset | LineItemupdateFilesBodyDataMatter
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = LineItemupdateFilesBodyDataMatter.from_dict(_matter)

        note = d.pop("note", UNSET)

        price = d.pop("price", UNSET)

        quantity = d.pop("quantity", UNSET)

        secondary_taxable = d.pop("secondary_taxable", UNSET)

        taxable = d.pop("taxable", UNSET)

        update_original_record = d.pop("update_original_record", UNSET)

        line_itemupdate_files_body_data = cls(
            activity=activity,
            bill=bill,
            date=date,
            description=description,
            discount=discount,
            group_ordering=group_ordering,
            kind=kind,
            matter=matter,
            note=note,
            price=price,
            quantity=quantity,
            secondary_taxable=secondary_taxable,
            taxable=taxable,
            update_original_record=update_original_record,
        )

        line_itemupdate_files_body_data.additional_properties = d
        return line_itemupdate_files_body_data

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
