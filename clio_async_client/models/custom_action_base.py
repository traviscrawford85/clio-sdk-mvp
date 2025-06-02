from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_action_base_ui_reference import CustomActionBaseUiReference
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomActionBase")


@_attrs_define
class CustomActionBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *CustomAction* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *CustomAction*
        id (Union[Unset, int]): Unique identifier for the *CustomAction*
        label (Union[Unset, str]): Text label to be displayed on the custom link.
        target_url (Union[Unset, str]): Target URL which will be opened in a new tab when the user clicks the custom
            link.
        ui_reference (Union[Unset, CustomActionBaseUiReference]): UI reference location within Clio where the link will
            be displayed.
        updated_at (Union[Unset, str]): The time the *CustomAction* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    target_url: Union[Unset, str] = UNSET
    ui_reference: Union[Unset, CustomActionBaseUiReference] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        etag = self.etag

        id = self.id

        label = self.label

        target_url = self.target_url

        ui_reference: Union[Unset, str] = UNSET
        if not isinstance(self.ui_reference, Unset):
            ui_reference = self.ui_reference.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if target_url is not UNSET:
            field_dict["target_url"] = target_url
        if ui_reference is not UNSET:
            field_dict["ui_reference"] = ui_reference
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        target_url = d.pop("target_url", UNSET)

        _ui_reference = d.pop("ui_reference", UNSET)
        ui_reference: Union[Unset, CustomActionBaseUiReference]
        if isinstance(_ui_reference, Unset):
            ui_reference = UNSET
        else:
            ui_reference = CustomActionBaseUiReference(_ui_reference)

        updated_at = d.pop("updated_at", UNSET)

        custom_action_base = cls(
            created_at=created_at,
            etag=etag,
            id=id,
            label=label,
            target_url=target_url,
            ui_reference=ui_reference,
            updated_at=updated_at,
        )

        custom_action_base.additional_properties = d
        return custom_action_base

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
