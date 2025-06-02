from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.medical_record_matter import MedicalRecordMatter


T = TypeVar("T", bound="MedicalRecord")


@_attrs_define
class MedicalRecord:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *MedicalRecord* was created (as a ISO-8601 timestamp)
        document_id (Union[Unset, int]): The id of the document associated with the Medical Record
        end_date (Union[Unset, str]): End date for *MedicalRecord* (as a ISO-8601 date)
        etag (Union[Unset, str]): ETag for the *MedicalRecord*
        id (Union[Unset, int]): Unique identifier for the *MedicalRecord*
        start_date (Union[Unset, str]): Start date for *MedicalRecord* (as a ISO-8601 date)
        updated_at (Union[Unset, str]): The time the *MedicalRecord* was last updated (as a ISO-8601 timestamp)
        matter (Union[Unset, MedicalRecordMatter]):
    """

    created_at: Union[Unset, str] = UNSET
    document_id: Union[Unset, int] = UNSET
    end_date: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    start_date: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    matter: Union[Unset, "MedicalRecordMatter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        document_id = self.document_id

        end_date = self.end_date

        etag = self.etag

        id = self.id

        start_date = self.start_date

        updated_at = self.updated_at

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

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
        if matter is not UNSET:
            field_dict["matter"] = matter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.medical_record_matter import MedicalRecordMatter

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        document_id = d.pop("document_id", UNSET)

        end_date = d.pop("end_date", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        start_date = d.pop("start_date", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, MedicalRecordMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MedicalRecordMatter.from_dict(_matter)

        medical_record = cls(
            created_at=created_at,
            document_id=document_id,
            end_date=end_date,
            etag=etag,
            id=id,
            start_date=start_date,
            updated_at=updated_at,
            matter=matter,
        )

        medical_record.additional_properties = d
        return medical_record

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
