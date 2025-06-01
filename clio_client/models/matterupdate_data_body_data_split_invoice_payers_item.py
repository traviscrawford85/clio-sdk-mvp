from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatterupdateDataBodyDataSplitInvoicePayersItem")


@_attrs_define
class MatterupdateDataBodyDataSplitInvoicePayersItem:
    """
    Attributes:
        field_destroy (Union[Unset, bool]): If this flag is set to `true`, the split invoice payer will be deleted from
            the Matter.
        contact_id (Union[Unset, int]): Contact id for the matter payer.
        id (Union[Unset, int]): The id for the payer.
        send_to_bill_recipients (Union[Unset, bool]): Boolean indication to send a split invoice to all bill recipients.
        split_portion (Union[Unset, float]): The split portion for the payer.
    """

    field_destroy: Unset | bool = UNSET
    contact_id: Unset | int = UNSET
    id: Unset | int = UNSET
    send_to_bill_recipients: Unset | bool = UNSET
    split_portion: Unset | float = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_destroy = self.field_destroy

        contact_id = self.contact_id

        id = self.id

        send_to_bill_recipients = self.send_to_bill_recipients

        split_portion = self.split_portion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if id is not UNSET:
            field_dict["id"] = id
        if send_to_bill_recipients is not UNSET:
            field_dict["send_to_bill_recipients"] = send_to_bill_recipients
        if split_portion is not UNSET:
            field_dict["split_portion"] = split_portion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_destroy = d.pop("_destroy", UNSET)

        contact_id = d.pop("contact_id", UNSET)

        id = d.pop("id", UNSET)

        send_to_bill_recipients = d.pop("send_to_bill_recipients", UNSET)

        split_portion = d.pop("split_portion", UNSET)

        matterupdate_data_body_data_split_invoice_payers_item = cls(
            field_destroy=field_destroy,
            contact_id=contact_id,
            id=id,
            send_to_bill_recipients=send_to_bill_recipients,
            split_portion=split_portion,
        )

        matterupdate_data_body_data_split_invoice_payers_item.additional_properties = d
        return matterupdate_data_body_data_split_invoice_payers_item

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
