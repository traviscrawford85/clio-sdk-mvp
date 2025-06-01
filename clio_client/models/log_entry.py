from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.log_entry_base_type import LogEntryBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_entry_item import LogEntryItem
    from ..models.log_entry_user import LogEntryUser


T = TypeVar("T", bound="LogEntry")


@_attrs_define
class LogEntry:
    """
    Attributes:
        accessed_at (Union[Unset, str]): The time the item was last accessed (as a ISO-8601 timestamp)
        created_at (Union[Unset, str]): The time the *LogEntry* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *LogEntry*
        id (Union[Unset, int]): Unique identifier for the *LogEntry*
        type_ (Union[Unset, LogEntryBaseType]): The type of the *LogEntry*
        updated_at (Union[Unset, str]): The time the *LogEntry* was last updated (as a ISO-8601 timestamp)
        item (Union[Unset, LogEntryItem]):
        user (Union[Unset, LogEntryUser]):
    """

    accessed_at: Unset | str = UNSET
    created_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    type_: Unset | LogEntryBaseType = UNSET
    updated_at: Unset | str = UNSET
    item: Union[Unset, "LogEntryItem"] = UNSET
    user: Union[Unset, "LogEntryUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accessed_at = self.accessed_at

        created_at = self.created_at

        etag = self.etag

        id = self.id

        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        item: Unset | dict[str, Any] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()

        user: Unset | dict[str, Any] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accessed_at is not UNSET:
            field_dict["accessed_at"] = accessed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if item is not UNSET:
            field_dict["item"] = item
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log_entry_item import LogEntryItem
        from ..models.log_entry_user import LogEntryUser

        d = dict(src_dict)
        accessed_at = d.pop("accessed_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Unset | LogEntryBaseType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = LogEntryBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        _item = d.pop("item", UNSET)
        item: Unset | LogEntryItem
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = LogEntryItem.from_dict(_item)

        _user = d.pop("user", UNSET)
        user: Unset | LogEntryUser
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = LogEntryUser.from_dict(_user)

        log_entry = cls(
            accessed_at=accessed_at,
            created_at=created_at,
            etag=etag,
            id=id,
            type_=type_,
            updated_at=updated_at,
            item=item,
            user=user,
        )

        log_entry.additional_properties = d
        return log_entry

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
