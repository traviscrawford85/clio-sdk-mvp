from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_preset_base_category import ReportPresetBaseCategory
from ..models.report_preset_base_format import ReportPresetBaseFormat
from ..models.report_preset_base_kind import ReportPresetBaseKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportPresetBase")


@_attrs_define
class ReportPresetBase:
    """
    Attributes:
        category (Union[Unset, ReportPresetBaseCategory]): The category of the report the preset generates
        created_at (Union[Unset, str]): The time the *ReportPreset* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *ReportPreset*
        format_ (Union[Unset, ReportPresetBaseFormat]): The format of the report the preset generates
        id (Union[Unset, int]): Unique identifier for the *ReportPreset*
        kind (Union[Unset, ReportPresetBaseKind]): The kind of report the preset generates
        last_generated_at (Union[Unset, str]): The time of the last generated report from this preset (as a ISO-8601
            timestamp)
        name (Union[Unset, str]): A specified name for the report preset
        options (Union[Unset, str]): The report options parameters
        updated_at (Union[Unset, str]): The time the *ReportPreset* was last updated (as a ISO-8601 timestamp)
    """

    category: Unset | ReportPresetBaseCategory = UNSET
    created_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    format_: Unset | ReportPresetBaseFormat = UNSET
    id: Unset | int = UNSET
    kind: Unset | ReportPresetBaseKind = UNSET
    last_generated_at: Unset | str = UNSET
    name: Unset | str = UNSET
    options: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: Unset | str = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        created_at = self.created_at

        etag = self.etag

        format_: Unset | str = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        id = self.id

        kind: Unset | str = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        last_generated_at = self.last_generated_at

        name = self.name

        options = self.options

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if format_ is not UNSET:
            field_dict["format"] = format_
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if last_generated_at is not UNSET:
            field_dict["last_generated_at"] = last_generated_at
        if name is not UNSET:
            field_dict["name"] = name
        if options is not UNSET:
            field_dict["options"] = options
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: Unset | ReportPresetBaseCategory
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ReportPresetBaseCategory(_category)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: Unset | ReportPresetBaseFormat
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = ReportPresetBaseFormat(_format_)

        id = d.pop("id", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Unset | ReportPresetBaseKind
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ReportPresetBaseKind(_kind)

        last_generated_at = d.pop("last_generated_at", UNSET)

        name = d.pop("name", UNSET)

        options = d.pop("options", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        report_preset_base = cls(
            category=category,
            created_at=created_at,
            etag=etag,
            format_=format_,
            id=id,
            kind=kind,
            last_generated_at=last_generated_at,
            name=name,
            options=options,
            updated_at=updated_at,
        )

        report_preset_base.additional_properties = d
        return report_preset_base

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
