from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matter_created_webhook_event_payload_custom_fields import (
        MatterCreatedWebhookEventPayloadCustomFields,
    )


T = TypeVar("T", bound="MatterCreatedWebhookEventPayload")


@_attrs_define
class MatterCreatedWebhookEventPayload:
    """
    Attributes:
        custom_fields (Union[Unset, MatterCreatedWebhookEventPayloadCustomFields]): Dynamic map of custom field values,
            e.g., date_of_incident
        display_number (Union[Unset, str]):
        id (Union[Unset, int]): The ID of the created matter
        practice_area (Union[Unset, str]):
    """

    custom_fields: Union[Unset, "MatterCreatedWebhookEventPayloadCustomFields"] = UNSET
    display_number: Unset | str = UNSET
    id: Unset | int = UNSET
    practice_area: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_fields: Unset | dict[str, Any] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        display_number = self.display_number

        id = self.id

        practice_area = self.practice_area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if display_number is not UNSET:
            field_dict["display_number"] = display_number
        if id is not UNSET:
            field_dict["id"] = id
        if practice_area is not UNSET:
            field_dict["practice_area"] = practice_area

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matter_created_webhook_event_payload_custom_fields import (
            MatterCreatedWebhookEventPayloadCustomFields,
        )

        d = dict(src_dict)
        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Unset | MatterCreatedWebhookEventPayloadCustomFields
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = MatterCreatedWebhookEventPayloadCustomFields.from_dict(
                _custom_fields
            )

        display_number = d.pop("display_number", UNSET)

        id = d.pop("id", UNSET)

        practice_area = d.pop("practice_area", UNSET)

        matter_created_webhook_event_payload = cls(
            custom_fields=custom_fields,
            display_number=display_number,
            id=id,
            practice_area=practice_area,
        )

        matter_created_webhook_event_payload.additional_properties = d
        return matter_created_webhook_event_payload

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
