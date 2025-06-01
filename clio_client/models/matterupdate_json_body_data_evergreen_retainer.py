from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matterupdate_json_body_data_evergreen_retainer_recipients_item import (
        MatterupdateJsonBodyDataEvergreenRetainerRecipientsItem,
    )


T = TypeVar("T", bound="MatterupdateJsonBodyDataEvergreenRetainer")


@_attrs_define
class MatterupdateJsonBodyDataEvergreenRetainer:
    """
    Attributes:
        field_destroy (Union[Unset, bool]): If this flag is set to `true`, the trust balance notification will be
            deleted from the Matter.
        minimum_threshold (Union[Unset, float]): The trust balance threshold for the Matter. When the balance falls
            below the threshold, the retainer's associated recipients (firm users) will receive a notification.
        recipients (Union[Unset, list['MatterupdateJsonBodyDataEvergreenRetainerRecipientsItem']]):
    """

    field_destroy: Unset | bool = UNSET
    minimum_threshold: Unset | float = UNSET
    recipients: (
        Unset | list["MatterupdateJsonBodyDataEvergreenRetainerRecipientsItem"]
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_destroy = self.field_destroy

        minimum_threshold = self.minimum_threshold

        recipients: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = []
            for recipients_item_data in self.recipients:
                recipients_item = recipients_item_data.to_dict()
                recipients.append(recipients_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if minimum_threshold is not UNSET:
            field_dict["minimum_threshold"] = minimum_threshold
        if recipients is not UNSET:
            field_dict["recipients"] = recipients

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matterupdate_json_body_data_evergreen_retainer_recipients_item import (
            MatterupdateJsonBodyDataEvergreenRetainerRecipientsItem,
        )

        d = dict(src_dict)
        field_destroy = d.pop("_destroy", UNSET)

        minimum_threshold = d.pop("minimum_threshold", UNSET)

        recipients = []
        _recipients = d.pop("recipients", UNSET)
        for recipients_item_data in _recipients or []:
            recipients_item = (
                MatterupdateJsonBodyDataEvergreenRetainerRecipientsItem.from_dict(
                    recipients_item_data
                )
            )

            recipients.append(recipients_item)

        matterupdate_json_body_data_evergreen_retainer = cls(
            field_destroy=field_destroy,
            minimum_threshold=minimum_threshold,
            recipients=recipients,
        )

        matterupdate_json_body_data_evergreen_retainer.additional_properties = d
        return matterupdate_json_body_data_evergreen_retainer

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
