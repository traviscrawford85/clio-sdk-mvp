from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.balance_base import BalanceBase
    from ..models.interest_charge_bill import InterestChargeBill
    from ..models.matter_base import MatterBase


T = TypeVar("T", bound="InterestCharge")


@_attrs_define
class InterestCharge:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *InterestCharge* was created (as a ISO-8601 timestamp)
        date (Union[Unset, str]): The *InterestCharge* date (as a ISO-8601 date)
        description (Union[Unset, str]): The description for the *InterestCharge*
        etag (Union[Unset, str]): ETag for the *InterestCharge*
        id (Union[Unset, int]): Unique identifier for the *InterestCharge*
        total (Union[Unset, float]): The total amount for the *InterestCharge*
        updated_at (Union[Unset, str]): The time the *InterestCharge* was last updated (as a ISO-8601 timestamp)
        balances (Union[Unset, list['BalanceBase']]): Balance
        bill (Union[Unset, InterestChargeBill]):
        matters (Union[Unset, list['MatterBase']]): Matter
    """

    created_at: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    total: Union[Unset, float] = UNSET
    updated_at: Union[Unset, str] = UNSET
    balances: Union[Unset, list["BalanceBase"]] = UNSET
    bill: Union[Unset, "InterestChargeBill"] = UNSET
    matters: Union[Unset, list["MatterBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        date = self.date

        description = self.description

        etag = self.etag

        id = self.id

        total = self.total

        updated_at = self.updated_at

        balances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.balances, Unset):
            balances = []
            for balances_item_data in self.balances:
                balances_item = balances_item_data.to_dict()
                balances.append(balances_item)

        bill: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bill, Unset):
            bill = self.bill.to_dict()

        matters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matters, Unset):
            matters = []
            for matters_item_data in self.matters:
                matters_item = matters_item_data.to_dict()
                matters.append(matters_item)

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
        if id is not UNSET:
            field_dict["id"] = id
        if total is not UNSET:
            field_dict["total"] = total
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if balances is not UNSET:
            field_dict["balances"] = balances
        if bill is not UNSET:
            field_dict["bill"] = bill
        if matters is not UNSET:
            field_dict["matters"] = matters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.balance_base import BalanceBase
        from ..models.interest_charge_bill import InterestChargeBill
        from ..models.matter_base import MatterBase

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        total = d.pop("total", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        balances = []
        _balances = d.pop("balances", UNSET)
        for balances_item_data in _balances or []:
            balances_item = BalanceBase.from_dict(balances_item_data)

            balances.append(balances_item)

        _bill = d.pop("bill", UNSET)
        bill: Union[Unset, InterestChargeBill]
        if isinstance(_bill, Unset):
            bill = UNSET
        else:
            bill = InterestChargeBill.from_dict(_bill)

        matters = []
        _matters = d.pop("matters", UNSET)
        for matters_item_data in _matters or []:
            matters_item = MatterBase.from_dict(matters_item_data)

            matters.append(matters_item)

        interest_charge = cls(
            created_at=created_at,
            date=date,
            description=description,
            etag=etag,
            id=id,
            total=total,
            updated_at=updated_at,
            balances=balances,
            bill=bill,
            matters=matters,
        )

        interest_charge.additional_properties = d
        return interest_charge

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
