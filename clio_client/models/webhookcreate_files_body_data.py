from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhookcreate_files_body_data_events_item import (
    WebhookcreateFilesBodyDataEventsItem,
)
from ..models.webhookcreate_files_body_data_model import WebhookcreateFilesBodyDataModel
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookcreateFilesBodyData")


@_attrs_define
class WebhookcreateFilesBodyData:
    """
    Attributes:
        fields (str): Fields to be included in the Webhook request.
        model (WebhookcreateFilesBodyDataModel): What model the Webhook is for. This field accepts either [the string
            identifier of the model or its ID](#section/Supported-Models)
        url (str): The URL of where to POST the Webhook. Note that only URLs using the `https` protocol will be
            accepted.
        events (Union[Unset, list[WebhookcreateFilesBodyDataEventsItem]]): The events your webhook is subscribed to.
        expires_at (Union[Unset, str]): The date and time when the Webhook will expire. (Expects an ISO-8601 timestamp).
    """

    fields: str
    model: WebhookcreateFilesBodyDataModel
    url: str
    events: Unset | list[WebhookcreateFilesBodyDataEventsItem] = UNSET
    expires_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields = self.fields

        model = self.model.value

        url = self.url

        events: Unset | list[str] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields": fields,
                "model": model,
                "url": url,
            }
        )
        if events is not UNSET:
            field_dict["events"] = events
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fields = d.pop("fields")

        model = WebhookcreateFilesBodyDataModel(d.pop("model"))

        url = d.pop("url")

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = WebhookcreateFilesBodyDataEventsItem(events_item_data)

            events.append(events_item)

        expires_at = d.pop("expires_at", UNSET)

        webhookcreate_files_body_data = cls(
            fields=fields,
            model=model,
            url=url,
            events=events,
            expires_at=expires_at,
        )

        webhookcreate_files_body_data.additional_properties = d
        return webhookcreate_files_body_data

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
