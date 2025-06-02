from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.matter_created_webhook_event_event import MatterCreatedWebhookEventEvent
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matter_created_webhook_event_payload import (
        MatterCreatedWebhookEventPayload,
    )


T = TypeVar("T", bound="MatterCreatedWebhookEvent")


@_attrs_define
class MatterCreatedWebhookEvent:
    """
    Attributes:
        event (Union[Unset, MatterCreatedWebhookEventEvent]):
        payload (Union[Unset, MatterCreatedWebhookEventPayload]):
        timestamp (Union[Unset, str]):
    """

    event: Union[Unset, MatterCreatedWebhookEventEvent] = UNSET
    payload: Union[Unset, "MatterCreatedWebhookEventPayload"] = UNSET
    timestamp: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event: Union[Unset, str] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.value

        payload: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event
        if payload is not UNSET:
            field_dict["payload"] = payload
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matter_created_webhook_event_payload import (
            MatterCreatedWebhookEventPayload,
        )

        d = dict(src_dict)
        _event = d.pop("event", UNSET)
        event: Union[Unset, MatterCreatedWebhookEventEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = MatterCreatedWebhookEventEvent(_event)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, MatterCreatedWebhookEventPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = MatterCreatedWebhookEventPayload.from_dict(_payload)

        timestamp = d.pop("timestamp", UNSET)

        matter_created_webhook_event = cls(
            event=event,
            payload=payload,
            timestamp=timestamp,
        )

        matter_created_webhook_event.additional_properties = d
        return matter_created_webhook_event

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
