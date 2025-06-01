from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.polymorphic_custom_rate_activity_description import (
        PolymorphicCustomRateActivityDescription,
    )
    from ..models.polymorphic_custom_rate_group import PolymorphicCustomRateGroup
    from ..models.polymorphic_custom_rate_user import PolymorphicCustomRateUser


T = TypeVar("T", bound="PolymorphicCustomRate")


@_attrs_define
class PolymorphicCustomRate:
    """
    Attributes:
        award (Union[Unset, float]): The value of the ContingencyFee award.
        created_at (Union[Unset, str]): The time the *PolymorphicCustomRate* was created (as a ISO-8601 timestamp)
        date (Union[Unset, str]): The date of the ContingencyFee award.
        etag (Union[Unset, str]): ETag for the *PolymorphicCustomRate*
        id (Union[Unset, int]): The unique identifier for the custom rate
        note (Union[Unset, str]): Details about the ContingencyFee award.
        rate (Union[Unset, float]): If `custom_rate.type` is `HourlyRate`, it is the dollar amount of the custom rate of
            the User or Group for the Matter.

            If `custom_rate.type` is `FlatRate`, it is the dollar amount of the custom flat rate for the Matter.

            If `custom_rate.type` is `ContingencyFee`, it is the percentage of the contingency fee awarded to the user for
            the Matter. The value may also be expressed as string that represents a rational number such as `1/3`.

            If the user does not have sufficient rate visibility, the rates are hidden.
        updated_at (Union[Unset, str]): The time the *PolymorphicCustomRate* was last updated (as a ISO-8601 timestamp)
        activity_description (Union[Unset, PolymorphicCustomRateActivityDescription]):
        group (Union[Unset, PolymorphicCustomRateGroup]):
        user (Union[Unset, PolymorphicCustomRateUser]):
    """

    award: Unset | float = UNSET
    created_at: Unset | str = UNSET
    date: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    note: Unset | str = UNSET
    rate: Unset | float = UNSET
    updated_at: Unset | str = UNSET
    activity_description: Union[Unset, "PolymorphicCustomRateActivityDescription"] = (
        UNSET
    )
    group: Union[Unset, "PolymorphicCustomRateGroup"] = UNSET
    user: Union[Unset, "PolymorphicCustomRateUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        award = self.award

        created_at = self.created_at

        date = self.date

        etag = self.etag

        id = self.id

        note = self.note

        rate = self.rate

        updated_at = self.updated_at

        activity_description: Unset | dict[str, Any] = UNSET
        if not isinstance(self.activity_description, Unset):
            activity_description = self.activity_description.to_dict()

        group: Unset | dict[str, Any] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        user: Unset | dict[str, Any] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if award is not UNSET:
            field_dict["award"] = award
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
        if rate is not UNSET:
            field_dict["rate"] = rate
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if activity_description is not UNSET:
            field_dict["activity_description"] = activity_description
        if group is not UNSET:
            field_dict["group"] = group
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.polymorphic_custom_rate_activity_description import (
            PolymorphicCustomRateActivityDescription,
        )
        from ..models.polymorphic_custom_rate_group import PolymorphicCustomRateGroup
        from ..models.polymorphic_custom_rate_user import PolymorphicCustomRateUser

        d = dict(src_dict)
        award = d.pop("award", UNSET)

        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        note = d.pop("note", UNSET)

        rate = d.pop("rate", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _activity_description = d.pop("activity_description", UNSET)
        activity_description: Unset | PolymorphicCustomRateActivityDescription
        if isinstance(_activity_description, Unset):
            activity_description = UNSET
        else:
            activity_description = PolymorphicCustomRateActivityDescription.from_dict(
                _activity_description
            )

        _group = d.pop("group", UNSET)
        group: Unset | PolymorphicCustomRateGroup
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = PolymorphicCustomRateGroup.from_dict(_group)

        _user = d.pop("user", UNSET)
        user: Unset | PolymorphicCustomRateUser
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PolymorphicCustomRateUser.from_dict(_user)

        polymorphic_custom_rate = cls(
            award=award,
            created_at=created_at,
            date=date,
            etag=etag,
            id=id,
            note=note,
            rate=rate,
            updated_at=updated_at,
            activity_description=activity_description,
            group=group,
            user=user,
        )

        polymorphic_custom_rate.additional_properties = d
        return polymorphic_custom_rate

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
