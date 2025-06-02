from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhookupdate_data_body_data_events_item import (
    WebhookupdateDataBodyDataEventsItem,
)
from ..models.webhookupdate_data_body_data_model import WebhookupdateDataBodyDataModel
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookupdateDataBodyData")


@_attrs_define
class WebhookupdateDataBodyData:
    """
    Attributes:
        events (Union[Unset, list[WebhookupdateDataBodyDataEventsItem]]): The events your webhook is subscribed to.
        expires_at (Union[Unset, str]): The date and time when the Webhook will expire. (Expects an ISO-8601 timestamp).
        fields (Union[Unset, str]): Fields to be included in the Webhook request.
        model (Union[Unset, WebhookupdateDataBodyDataModel]): What model the Webhook is for. This field accepts either
            [the string identifier of the model or its ID](#section/Supported-Models)
        url (Union[Unset, str]): The URL of where to POST the Webhook. Note that only URLs using the `https` protocol
            will be accepted.
    """

    events: Union[Unset, list[WebhookupdateDataBodyDataEventsItem]] = UNSET
    expires_at: Union[Unset, str] = UNSET
    fields: Union[Unset, str] = UNSET
    model: Union[Unset, WebhookupdateDataBodyDataModel] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events: Union[Unset, list[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        expires_at = self.expires_at

        fields = self.fields

        model: Union[Unset, str] = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if fields is not UNSET:
            field_dict["fields"] = fields
        if model is not UNSET:
            field_dict["model"] = model
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = WebhookupdateDataBodyDataEventsItem(events_item_data)

            events.append(events_item)

        expires_at = d.pop("expires_at", UNSET)

        fields = d.pop("fields", UNSET)

        _model = d.pop("model", UNSET)
        model: Union[Unset, WebhookupdateDataBodyDataModel]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = WebhookupdateDataBodyDataModel(_model)

        url = d.pop("url", UNSET)

        webhookupdate_data_body_data = cls(
            events=events,
            expires_at=expires_at,
            fields=fields,
            model=model,
            url=url,
        )

        webhookupdate_data_body_data.additional_properties = d
        return webhookupdate_data_body_data

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
