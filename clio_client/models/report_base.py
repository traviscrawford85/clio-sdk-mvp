from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.report_base_category import ReportBaseCategory
from ..models.report_base_format import ReportBaseFormat
from ..models.report_base_kind import ReportBaseKind
from ..models.report_base_source import ReportBaseSource
from ..models.report_base_state import ReportBaseState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportBase")


@_attrs_define
class ReportBase:
    """
    Attributes:
        category (Union[Unset, ReportBaseCategory]): The category of the report
        created_at (Union[Unset, str]): The time the *Report* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *Report*
        format_ (Union[Unset, ReportBaseFormat]): The requested format of the report
        id (Union[Unset, int]): Unique identifier for the *Report*
        kind (Union[Unset, ReportBaseKind]): The kind of report to generate
        name (Union[Unset, str]): A specified name for the report
        progress (Union[Unset, int]): The integer percentage of how complete the report is.
        source (Union[Unset, ReportBaseSource]): The source of the report
        state (Union[Unset, ReportBaseState]): The current state of the report
        updated_at (Union[Unset, str]): The time the *Report* was last updated (as a ISO-8601 timestamp)
    """

    category: Unset | ReportBaseCategory = UNSET
    created_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    format_: Unset | ReportBaseFormat = UNSET
    id: Unset | int = UNSET
    kind: Unset | ReportBaseKind = UNSET
    name: Unset | str = UNSET
    progress: Unset | int = UNSET
    source: Unset | ReportBaseSource = UNSET
    state: Unset | ReportBaseState = UNSET
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

        name = self.name

        progress = self.progress

        source: Unset | str = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        state: Unset | str = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

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
        if name is not UNSET:
            field_dict["name"] = name
        if progress is not UNSET:
            field_dict["progress"] = progress
        if source is not UNSET:
            field_dict["source"] = source
        if state is not UNSET:
            field_dict["state"] = state
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: Unset | ReportBaseCategory
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ReportBaseCategory(_category)

        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: Unset | ReportBaseFormat
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = ReportBaseFormat(_format_)

        id = d.pop("id", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Unset | ReportBaseKind
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = ReportBaseKind(_kind)

        name = d.pop("name", UNSET)

        progress = d.pop("progress", UNSET)

        _source = d.pop("source", UNSET)
        source: Unset | ReportBaseSource
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ReportBaseSource(_source)

        _state = d.pop("state", UNSET)
        state: Unset | ReportBaseState
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ReportBaseState(_state)

        updated_at = d.pop("updated_at", UNSET)

        report_base = cls(
            category=category,
            created_at=created_at,
            etag=etag,
            format_=format_,
            id=id,
            kind=kind,
            name=name,
            progress=progress,
            source=source,
            state=state,
            updated_at=updated_at,
        )

        report_base.additional_properties = d
        return report_base

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
