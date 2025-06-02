from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.medical_records_requestcreate_files_body_data_bills_status import (
    MedicalRecordsRequestcreateFilesBodyDataBillsStatus,
)
from ..models.medical_records_requestcreate_files_body_data_records_status import (
    MedicalRecordsRequestcreateFilesBodyDataRecordsStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.medical_records_requestcreate_files_body_data_medical_bills_item import (
        MedicalRecordsRequestcreateFilesBodyDataMedicalBillsItem,
    )
    from ..models.medical_records_requestcreate_files_body_data_medical_records_item import (
        MedicalRecordsRequestcreateFilesBodyDataMedicalRecordsItem,
    )


T = TypeVar("T", bound="MedicalRecordsRequestcreateFilesBodyData")


@_attrs_define
class MedicalRecordsRequestcreateFilesBodyData:
    """
    Attributes:
        bills_status (MedicalRecordsRequestcreateFilesBodyDataBillsStatus): Current status for the Medical Bills.
        in_treatment (bool): True or false value to record if the treatment has been completed.
        matter_id (int): The ID of the matter that the Medical Records Detail belongs to.
        medical_provider_id (int): The unique identifier for a single Medical Provider associated with this Medical
            Records Detail.
        records_status (MedicalRecordsRequestcreateFilesBodyDataRecordsStatus): Current status for the Medical Records.
        bills_follow_up_date (Union[Unset, str]): Follow up date for Medical Bills. (Expects an ISO-8601 date).
        bills_request_date (Union[Unset, str]): Requested date for Medical Bills. (Expects an ISO-8601 date).
        description (Union[Unset, str]): Detailed description of the Medical Records Detail.
        medical_bills (Union[Unset, list['MedicalRecordsRequestcreateFilesBodyDataMedicalBillsItem']]):
        medical_records (Union[Unset, list['MedicalRecordsRequestcreateFilesBodyDataMedicalRecordsItem']]):
        records_follow_up_date (Union[Unset, str]): Follow up date for Medical Records. (Expects an ISO-8601 date).
        records_request_date (Union[Unset, str]): Requested date for Medical Records. (Expects an ISO-8601 date).
        treatment_end_date (Union[Unset, str]): End date for the treatment. (Expects an ISO-8601 date).
        treatment_start_date (Union[Unset, str]): Start date for the treatment. (Expects an ISO-8601 date).
    """

    bills_status: MedicalRecordsRequestcreateFilesBodyDataBillsStatus
    in_treatment: bool
    matter_id: int
    medical_provider_id: int
    records_status: MedicalRecordsRequestcreateFilesBodyDataRecordsStatus
    bills_follow_up_date: Union[Unset, str] = UNSET
    bills_request_date: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    medical_bills: Union[Unset, list["MedicalRecordsRequestcreateFilesBodyDataMedicalBillsItem"]] = UNSET
    medical_records: Union[Unset, list["MedicalRecordsRequestcreateFilesBodyDataMedicalRecordsItem"]] = UNSET
    records_follow_up_date: Union[Unset, str] = UNSET
    records_request_date: Union[Unset, str] = UNSET
    treatment_end_date: Union[Unset, str] = UNSET
    treatment_start_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bills_status = self.bills_status.value

        in_treatment = self.in_treatment

        matter_id = self.matter_id

        medical_provider_id = self.medical_provider_id

        records_status = self.records_status.value

        bills_follow_up_date = self.bills_follow_up_date

        bills_request_date = self.bills_request_date

        description = self.description

        medical_bills: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.medical_bills, Unset):
            medical_bills = []
            for medical_bills_item_data in self.medical_bills:
                medical_bills_item = medical_bills_item_data.to_dict()
                medical_bills.append(medical_bills_item)

        medical_records: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.medical_records, Unset):
            medical_records = []
            for medical_records_item_data in self.medical_records:
                medical_records_item = medical_records_item_data.to_dict()
                medical_records.append(medical_records_item)

        records_follow_up_date = self.records_follow_up_date

        records_request_date = self.records_request_date

        treatment_end_date = self.treatment_end_date

        treatment_start_date = self.treatment_start_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bills_status": bills_status,
                "in_treatment": in_treatment,
                "matter_id": matter_id,
                "medical_provider_id": medical_provider_id,
                "records_status": records_status,
            }
        )
        if bills_follow_up_date is not UNSET:
            field_dict["bills_follow_up_date"] = bills_follow_up_date
        if bills_request_date is not UNSET:
            field_dict["bills_request_date"] = bills_request_date
        if description is not UNSET:
            field_dict["description"] = description
        if medical_bills is not UNSET:
            field_dict["medical_bills"] = medical_bills
        if medical_records is not UNSET:
            field_dict["medical_records"] = medical_records
        if records_follow_up_date is not UNSET:
            field_dict["records_follow_up_date"] = records_follow_up_date
        if records_request_date is not UNSET:
            field_dict["records_request_date"] = records_request_date
        if treatment_end_date is not UNSET:
            field_dict["treatment_end_date"] = treatment_end_date
        if treatment_start_date is not UNSET:
            field_dict["treatment_start_date"] = treatment_start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.medical_records_requestcreate_files_body_data_medical_bills_item import (
            MedicalRecordsRequestcreateFilesBodyDataMedicalBillsItem,
        )
        from ..models.medical_records_requestcreate_files_body_data_medical_records_item import (
            MedicalRecordsRequestcreateFilesBodyDataMedicalRecordsItem,
        )

        d = dict(src_dict)
        bills_status = MedicalRecordsRequestcreateFilesBodyDataBillsStatus(d.pop("bills_status"))

        in_treatment = d.pop("in_treatment")

        matter_id = d.pop("matter_id")

        medical_provider_id = d.pop("medical_provider_id")

        records_status = MedicalRecordsRequestcreateFilesBodyDataRecordsStatus(d.pop("records_status"))

        bills_follow_up_date = d.pop("bills_follow_up_date", UNSET)

        bills_request_date = d.pop("bills_request_date", UNSET)

        description = d.pop("description", UNSET)

        medical_bills = []
        _medical_bills = d.pop("medical_bills", UNSET)
        for medical_bills_item_data in _medical_bills or []:
            medical_bills_item = MedicalRecordsRequestcreateFilesBodyDataMedicalBillsItem.from_dict(
                medical_bills_item_data
            )

            medical_bills.append(medical_bills_item)

        medical_records = []
        _medical_records = d.pop("medical_records", UNSET)
        for medical_records_item_data in _medical_records or []:
            medical_records_item = MedicalRecordsRequestcreateFilesBodyDataMedicalRecordsItem.from_dict(
                medical_records_item_data
            )

            medical_records.append(medical_records_item)

        records_follow_up_date = d.pop("records_follow_up_date", UNSET)

        records_request_date = d.pop("records_request_date", UNSET)

        treatment_end_date = d.pop("treatment_end_date", UNSET)

        treatment_start_date = d.pop("treatment_start_date", UNSET)

        medical_records_requestcreate_files_body_data = cls(
            bills_status=bills_status,
            in_treatment=in_treatment,
            matter_id=matter_id,
            medical_provider_id=medical_provider_id,
            records_status=records_status,
            bills_follow_up_date=bills_follow_up_date,
            bills_request_date=bills_request_date,
            description=description,
            medical_bills=medical_bills,
            medical_records=medical_records,
            records_follow_up_date=records_follow_up_date,
            records_request_date=records_request_date,
            treatment_end_date=treatment_end_date,
            treatment_start_date=treatment_start_date,
        )

        medical_records_requestcreate_files_body_data.additional_properties = d
        return medical_records_requestcreate_files_body_data

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
