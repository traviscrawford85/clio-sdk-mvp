from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MedicalRecordBase")


@_attrs_define
class MedicalRecordBase:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *MedicalRecord* was created (as a ISO-8601 timestamp)
        document_id (Union[Unset, int]): The id of the document associated with the Medical Record
        end_date (Union[Unset, str]): End date for *MedicalRecord* (as a ISO-8601 date)
        etag (Union[Unset, str]): ETag for the *MedicalRecord*
        id (Union[Unset, int]): Unique identifier for the *MedicalRecord*
        start_date (Union[Unset, str]): Start date for *MedicalRecord* (as a ISO-8601 date)
        updated_at (Union[Unset, str]): The time the *MedicalRecord* was last updated (as a ISO-8601 timestamp)
    """

    created_at: Unset | str = UNSET
    document_id: Unset | int = UNSET
    end_date: Unset | str = UNSET
    etag: Unset | str = UNSET
    id: Unset | int = UNSET
    start_date: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        document_id = self.document_id

        end_date = self.end_date

        etag = self.etag

        id = self.id

        start_date = self.start_date

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        document_id = d.pop("document_id", UNSET)

        end_date = d.pop("end_date", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        start_date = d.pop("start_date", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        medical_record_base = cls(
            created_at=created_at,
            document_id=document_id,
            end_date=end_date,
            etag=etag,
            id=id,
            start_date=start_date,
            updated_at=updated_at,
        )

        medical_record_base.additional_properties = d
        return medical_record_base

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
