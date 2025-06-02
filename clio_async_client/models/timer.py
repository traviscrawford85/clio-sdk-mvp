from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timer_activity import TimerActivity


T = TypeVar("T", bound="Timer")


@_attrs_define
class Timer:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *Timer* was created (as a ISO-8601 timestamp)
        elapsed_time (Union[Unset, float]): How much time has elapsed, in hours, since the timer was started
        etag (Union[Unset, str]): ETag for the *Timer*
        id (Union[Unset, int]): Unique identifier for the *Timer*
        start_time (Union[Unset, str]): The time the *Timer* was started (as ISO-8601 timestamp)
        updated_at (Union[Unset, str]): The time the *Timer* was last updated (as a ISO-8601 timestamp)
        activity (Union[Unset, TimerActivity]):
    """

    created_at: Union[Unset, str] = UNSET
    elapsed_time: Union[Unset, float] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    start_time: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    activity: Union[Unset, "TimerActivity"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        elapsed_time = self.elapsed_time

        etag = self.etag

        id = self.id

        start_time = self.start_time

        updated_at = self.updated_at

        activity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.activity, Unset):
            activity = self.activity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if elapsed_time is not UNSET:
            field_dict["elapsed_time"] = elapsed_time
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if activity is not UNSET:
            field_dict["activity"] = activity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timer_activity import TimerActivity

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        elapsed_time = d.pop("elapsed_time", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        start_time = d.pop("start_time", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _activity = d.pop("activity", UNSET)
        activity: Union[Unset, TimerActivity]
        if isinstance(_activity, Unset):
            activity = UNSET
        else:
            activity = TimerActivity.from_dict(_activity)

        timer = cls(
            created_at=created_at,
            elapsed_time=elapsed_time,
            etag=etag,
            id=id,
            start_time=start_time,
            updated_at=updated_at,
            activity=activity,
        )

        timer.additional_properties = d
        return timer

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
