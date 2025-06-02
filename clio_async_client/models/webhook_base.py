from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_base_events_item import WebhookBaseEventsItem
from ..models.webhook_base_model import WebhookBaseModel
from ..models.webhook_base_status import WebhookBaseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookBase")


@_attrs_define
class WebhookBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *Webhook* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *Webhook*
        events (Union[Unset, list[WebhookBaseEventsItem]]): The events your webhook is subscribed to.
        expires_at (Union[Unset, str]): The time webhook will expire (as a ISO-8601 timestamp)
        fields (Union[Unset, str]): Fields to be included in the webhook request
        id (Union[Unset, int]): Unique identifier for the *Webhook*
        model (Union[Unset, WebhookBaseModel]): What kind of records the webhook is for
        shared_secret (Union[Unset, str]): A shared secret used to create a signature for the payload
        status (Union[Unset, WebhookBaseStatus]): The current status of the webhook.
        updated_at (Union[Unset, str]): The time the *Webhook* was last updated (as a ISO-8601 timestamp)
        url (Union[Unset, str]): The `https` URL to send the data to when the events are triggered
    """

    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    events: Union[Unset, list[WebhookBaseEventsItem]] = UNSET
    expires_at: Union[Unset, str] = UNSET
    fields: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    model: Union[Unset, WebhookBaseModel] = UNSET
    shared_secret: Union[Unset, str] = UNSET
    status: Union[Unset, WebhookBaseStatus] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        etag = self.etag

        events: Union[Unset, list[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        expires_at = self.expires_at

        fields = self.fields

        id = self.id

        model: Union[Unset, str] = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.value

        shared_secret = self.shared_secret

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if events is not UNSET:
            field_dict["events"] = events
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if fields is not UNSET:
            field_dict["fields"] = fields
        if id is not UNSET:
            field_dict["id"] = id
        if model is not UNSET:
            field_dict["model"] = model
        if shared_secret is not UNSET:
            field_dict["shared_secret"] = shared_secret
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = WebhookBaseEventsItem(events_item_data)

            events.append(events_item)

        expires_at = d.pop("expires_at", UNSET)

        fields = d.pop("fields", UNSET)

        id = d.pop("id", UNSET)

        _model = d.pop("model", UNSET)
        model: Union[Unset, WebhookBaseModel]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = WebhookBaseModel(_model)

        shared_secret = d.pop("shared_secret", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, WebhookBaseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WebhookBaseStatus(_status)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        webhook_base = cls(
            created_at=created_at,
            etag=etag,
            events=events,
            expires_at=expires_at,
            fields=fields,
            id=id,
            model=model,
            shared_secret=shared_secret,
            status=status,
            updated_at=updated_at,
            url=url,
        )

        webhook_base.additional_properties = d
        return webhook_base

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
