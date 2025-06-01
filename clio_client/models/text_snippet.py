from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextSnippet")


@_attrs_define
class TextSnippet:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *TextSnippet* was created (as a ISO-8601 timestamp)
        etag (Union[Unset, str]): ETag for the *TextSnippet*
        id (Union[Unset, int]): Unique identifier for the *TextSnippet*
        phrase (Union[Unset, str]): The phrase the abbreviation should be expanded to
        snippet (Union[Unset, str]): The abbreviation that should be expanded
        updated_at (Union[Unset, str]): The time the *TextSnippet* was last updated (as a ISO-8601 timestamp)
        whole_word (Union[Unset, bool]): Whether the *TextSnippet* abbreviation requires a space after it has been
            entered to expand to a phrase
    """

    created_at: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    phrase: Unset | str = UNSET
    snippet: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    whole_word: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        etag = self.etag

        id = self.id

        phrase = self.phrase

        snippet = self.snippet

        updated_at = self.updated_at

        whole_word = self.whole_word

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if phrase is not UNSET:
            field_dict["phrase"] = phrase
        if snippet is not UNSET:
            field_dict["snippet"] = snippet
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if whole_word is not UNSET:
            field_dict["whole_word"] = whole_word

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        phrase = d.pop("phrase", UNSET)

        snippet = d.pop("snippet", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        whole_word = d.pop("whole_word", UNSET)

        text_snippet = cls(
            created_at=created_at,
            etag=etag,
            id=id,
            phrase=phrase,
            snippet=snippet,
            updated_at=updated_at,
            whole_word=whole_word,
        )

        text_snippet.additional_properties = d
        return text_snippet

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
