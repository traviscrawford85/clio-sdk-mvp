from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allocation_base import AllocationBase
    from ..models.credit_memo_contact import CreditMemoContact
    from ..models.credit_memo_user import CreditMemoUser


T = TypeVar("T", bound="CreditMemo")


@_attrs_define
class CreditMemo:
    """
    Attributes:
        amount (Union[Unset, float]): Total amount credited
        created_at (Union[Unset, str]): The time the *CreditMemo* was created (as a ISO-8601 timestamp)
        date (Union[Unset, str]): Date the *CreditMemo* was recorded (as a ISO-8601 date)
        description (Union[Unset, str]): A detailed description for the *CreditMemo*
        discount (Union[Unset, bool]): Whether the *CreditMemo* is applied as discount
        etag (Union[Unset, str]): ETag for the *CreditMemo*
        id (Union[Unset, int]): Unique identifier for the *CreditMemo*
        updated_at (Union[Unset, str]): The time the *CreditMemo* was last updated (as a ISO-8601 timestamp)
        voided_at (Union[Unset, str]): Time the *CreditMemo* was voided (as a ISO-8601 timestamp)
        allocations (Union[Unset, list['AllocationBase']]): Allocation
        contact (Union[Unset, CreditMemoContact]):
        user (Union[Unset, CreditMemoUser]):
    """

    amount: Union[Unset, float] = UNSET
    created_at: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    discount: Union[Unset, bool] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    updated_at: Union[Unset, str] = UNSET
    voided_at: Union[Unset, str] = UNSET
    allocations: Union[Unset, list["AllocationBase"]] = UNSET
    contact: Union[Unset, "CreditMemoContact"] = UNSET
    user: Union[Unset, "CreditMemoUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        created_at = self.created_at

        date = self.date

        description = self.description

        discount = self.discount

        etag = self.etag

        id = self.id

        updated_at = self.updated_at

        voided_at = self.voided_at

        allocations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.allocations, Unset):
            allocations = []
            for allocations_item_data in self.allocations:
                allocations_item = allocations_item_data.to_dict()
                allocations.append(allocations_item)

        contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

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
        if discount is not UNSET:
            field_dict["discount"] = discount
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if voided_at is not UNSET:
            field_dict["voided_at"] = voided_at
        if allocations is not UNSET:
            field_dict["allocations"] = allocations
        if contact is not UNSET:
            field_dict["contact"] = contact
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allocation_base import AllocationBase
        from ..models.credit_memo_contact import CreditMemoContact
        from ..models.credit_memo_user import CreditMemoUser

        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        discount = d.pop("discount", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        voided_at = d.pop("voided_at", UNSET)

        allocations = []
        _allocations = d.pop("allocations", UNSET)
        for allocations_item_data in _allocations or []:
            allocations_item = AllocationBase.from_dict(allocations_item_data)

            allocations.append(allocations_item)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, CreditMemoContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = CreditMemoContact.from_dict(_contact)

        _user = d.pop("user", UNSET)
        user: Union[Unset, CreditMemoUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = CreditMemoUser.from_dict(_user)

        credit_memo = cls(
            amount=amount,
            created_at=created_at,
            date=date,
            description=description,
            discount=discount,
            etag=etag,
            id=id,
            updated_at=updated_at,
            voided_at=voided_at,
            allocations=allocations,
            contact=contact,
            user=user,
        )

        credit_memo.additional_properties = d
        return credit_memo

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
