from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lien_base import LienBase
    from ..models.medical_bill_matter import MedicalBillMatter


T = TypeVar("T", bound="MedicalBill")


@_attrs_define
class MedicalBill:
    """
    Attributes:
        adjustment (Union[Unset, float]): Adjustment for Medical Bill
        amount (Union[Unset, float]): Amount for Medical Bill
        bill_date (Union[Unset, str]): Bill date for Medical Bill (as a ISO-8601 date)
        bill_received_date (Union[Unset, str]): Bill received date for Medical Bill (as a ISO-8601 date)
        created_at (Union[Unset, str]): The time the *MedicalBill* was created (as a ISO-8601 timestamp)
        damage_type (Union[Unset, str]): Damage Type
        document_id (Union[Unset, int]): The id of the document associated with the Medical Bill
        etag (Union[Unset, str]): ETag for the *MedicalBill*
        id (Union[Unset, int]): Unique identifier for the *MedicalBill*
        name (Union[Unset, str]): Name of the Medical Bill
        updated_at (Union[Unset, str]): The time the *MedicalBill* was last updated (as a ISO-8601 timestamp)
        liens (Union[Unset, list['LienBase']]): Lien
        matter (Union[Unset, MedicalBillMatter]):
    """

    adjustment: Unset | float = UNSET
    amount: Unset | float = UNSET
    bill_date: Unset | str = UNSET
    bill_received_date: Unset | str = UNSET
    created_at: Unset | str = UNSET
    damage_type: Unset | str = UNSET
    document_id: Unset | int = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    name: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    liens: Unset | list["LienBase"] = UNSET
    matter: Union[Unset, "MedicalBillMatter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adjustment = self.adjustment

        amount = self.amount

        bill_date = self.bill_date

        bill_received_date = self.bill_received_date

        created_at = self.created_at

        damage_type = self.damage_type

        document_id = self.document_id

        etag = self.etag

        id = self.id

        name = self.name

        updated_at = self.updated_at

        liens: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.liens, Unset):
            liens = []
            for liens_item_data in self.liens:
                liens_item = liens_item_data.to_dict()
                liens.append(liens_item)

        matter: Unset | dict[str, Any] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adjustment is not UNSET:
            field_dict["adjustment"] = adjustment
        if amount is not UNSET:
            field_dict["amount"] = amount
        if bill_date is not UNSET:
            field_dict["bill_date"] = bill_date
        if bill_received_date is not UNSET:
            field_dict["bill_received_date"] = bill_received_date
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if damage_type is not UNSET:
            field_dict["damage_type"] = damage_type
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if liens is not UNSET:
            field_dict["liens"] = liens
        if matter is not UNSET:
            field_dict["matter"] = matter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lien_base import LienBase
        from ..models.medical_bill_matter import MedicalBillMatter

        d = dict(src_dict)
        adjustment = d.pop("adjustment", UNSET)

        amount = d.pop("amount", UNSET)

        bill_date = d.pop("bill_date", UNSET)

        bill_received_date = d.pop("bill_received_date", UNSET)

        created_at = d.pop("created_at", UNSET)

        damage_type = d.pop("damage_type", UNSET)

        document_id = d.pop("document_id", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        liens = []
        _liens = d.pop("liens", UNSET)
        for liens_item_data in _liens or []:
            liens_item = LienBase.from_dict(liens_item_data)

            liens.append(liens_item)

        _matter = d.pop("matter", UNSET)
        matter: Unset | MedicalBillMatter
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MedicalBillMatter.from_dict(_matter)

        medical_bill = cls(
            adjustment=adjustment,
            amount=amount,
            bill_date=bill_date,
            bill_received_date=bill_received_date,
            created_at=created_at,
            damage_type=damage_type,
            document_id=document_id,
            etag=etag,
            id=id,
            name=name,
            updated_at=updated_at,
            liens=liens,
            matter=matter,
        )

        medical_bill.additional_properties = d
        return medical_bill

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
