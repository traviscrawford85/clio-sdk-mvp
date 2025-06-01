from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.matter_base_billing_method import MatterBaseBillingMethod
from ..models.matter_base_status import MatterBaseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="MedicalRecordMatter")


@_attrs_define
class MedicalRecordMatter:
    """
    Attributes:
        billable (Union[Unset, bool]): Whether this matter is billable
        billing_method (Union[Unset, MatterBaseBillingMethod]): Billing method of this matter
        client_id (Union[Unset, int]): Client ID
        client_reference (Union[Unset, str]): Client Reference string for external uses
        close_date (Union[Unset, str]): The date the matter was set to closed (as a ISO-8601 date)
        created_at (Union[Unset, str]): The time the *Matter* was created (as a ISO-8601 timestamp)
        custom_number (Union[Unset, str]): User defined custom number of the *Matter*
        description (Union[Unset, str]): The detailed description of the *Matter*
        display_number (Union[Unset, str]): The reference and label of the *Matter*. Depending on the account's
            manual_matter_numbering setting, this is either read only (generated) or customizable.
        etag (Union[Unset, str]): ETag for the *Matter*
        has_tasks (Union[Unset, bool]): Whether or not the matter has any tasks.
        id (Union[Unset, int]): Unique identifier for the *Matter*
        last_activity_date (Union[Unset, str]): The greatest date out of all of the activities on the matter (as a
            ISO-8601 date)
        location (Union[Unset, str]): The location of the *Matter*
        maildrop_address (Union[Unset, str]): A unique Maildrop email address for the matter
        matter_stage_updated_at (Union[Unset, str]): The date the matter stage was last updated (as a ISO-8601 date)
        number (Union[Unset, int]): The number given to the *Matter* within an account
        open_date (Union[Unset, str]): The date the matter was set to open (as a ISO-8601 date)
        pending_date (Union[Unset, str]): The date the matter was set to pending (as a ISO-8601 date)
        shared (Union[Unset, bool]): Whether the matter is currently shared with Clio Connect
        status (Union[Unset, MatterBaseStatus]): The current status of the *Matter*
        updated_at (Union[Unset, str]): The time the *Matter* was last updated (as a ISO-8601 timestamp)
    """

    billable: Unset | bool = UNSET
    billing_method: Unset | MatterBaseBillingMethod = UNSET
    client_id: Unset | int = UNSET
    client_reference: Unset | str = UNSET
    close_date: Unset | str = UNSET
    created_at: Unset | str = UNSET
    custom_number: Unset | str = UNSET
    description: Unset | str = UNSET
    display_number: Unset | str = UNSET
    etag: Unset | str = UNSET
    has_tasks: Unset | bool = UNSET
    id: Unset | int = UNSET
    last_activity_date: Unset | str = UNSET
    location: Unset | str = UNSET
    maildrop_address: Unset | str = UNSET
    matter_stage_updated_at: Unset | str = UNSET
    number: Unset | int = UNSET
    open_date: Unset | str = UNSET
    pending_date: Unset | str = UNSET
    shared: Unset | bool = UNSET
    status: Unset | MatterBaseStatus = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billable = self.billable

        billing_method: Unset | str = UNSET
        if not isinstance(self.billing_method, Unset):
            billing_method = self.billing_method.value

        client_id = self.client_id

        client_reference = self.client_reference

        close_date = self.close_date

        created_at = self.created_at

        custom_number = self.custom_number

        description = self.description

        display_number = self.display_number

        etag = self.etag

        has_tasks = self.has_tasks

        id = self.id

        last_activity_date = self.last_activity_date

        location = self.location

        maildrop_address = self.maildrop_address

        matter_stage_updated_at = self.matter_stage_updated_at

        number = self.number

        open_date = self.open_date

        pending_date = self.pending_date

        shared = self.shared

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billable is not UNSET:
            field_dict["billable"] = billable
        if billing_method is not UNSET:
            field_dict["billing_method"] = billing_method
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_reference is not UNSET:
            field_dict["client_reference"] = client_reference
        if close_date is not UNSET:
            field_dict["close_date"] = close_date
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if custom_number is not UNSET:
            field_dict["custom_number"] = custom_number
        if description is not UNSET:
            field_dict["description"] = description
        if display_number is not UNSET:
            field_dict["display_number"] = display_number
        if etag is not UNSET:
            field_dict["etag"] = etag
        if has_tasks is not UNSET:
            field_dict["has_tasks"] = has_tasks
        if id is not UNSET:
            field_dict["id"] = id
        if last_activity_date is not UNSET:
            field_dict["last_activity_date"] = last_activity_date
        if location is not UNSET:
            field_dict["location"] = location
        if maildrop_address is not UNSET:
            field_dict["maildrop_address"] = maildrop_address
        if matter_stage_updated_at is not UNSET:
            field_dict["matter_stage_updated_at"] = matter_stage_updated_at
        if number is not UNSET:
            field_dict["number"] = number
        if open_date is not UNSET:
            field_dict["open_date"] = open_date
        if pending_date is not UNSET:
            field_dict["pending_date"] = pending_date
        if shared is not UNSET:
            field_dict["shared"] = shared
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        billable = d.pop("billable", UNSET)

        _billing_method = d.pop("billing_method", UNSET)
        billing_method: Unset | MatterBaseBillingMethod
        if isinstance(_billing_method, Unset):
            billing_method = UNSET
        else:
            billing_method = MatterBaseBillingMethod(_billing_method)

        client_id = d.pop("client_id", UNSET)

        client_reference = d.pop("client_reference", UNSET)

        close_date = d.pop("close_date", UNSET)

        created_at = d.pop("created_at", UNSET)

        custom_number = d.pop("custom_number", UNSET)

        description = d.pop("description", UNSET)

        display_number = d.pop("display_number", UNSET)

        etag = d.pop("etag", UNSET)

        has_tasks = d.pop("has_tasks", UNSET)

        id = d.pop("id", UNSET)

        last_activity_date = d.pop("last_activity_date", UNSET)

        location = d.pop("location", UNSET)

        maildrop_address = d.pop("maildrop_address", UNSET)

        matter_stage_updated_at = d.pop("matter_stage_updated_at", UNSET)

        number = d.pop("number", UNSET)

        open_date = d.pop("open_date", UNSET)

        pending_date = d.pop("pending_date", UNSET)

        shared = d.pop("shared", UNSET)

        _status = d.pop("status", UNSET)
        status: Unset | MatterBaseStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MatterBaseStatus(_status)

        updated_at = d.pop("updated_at", UNSET)

        medical_record_matter = cls(
            billable=billable,
            billing_method=billing_method,
            client_id=client_id,
            client_reference=client_reference,
            close_date=close_date,
            created_at=created_at,
            custom_number=custom_number,
            description=description,
            display_number=display_number,
            etag=etag,
            has_tasks=has_tasks,
            id=id,
            last_activity_date=last_activity_date,
            location=location,
            maildrop_address=maildrop_address,
            matter_stage_updated_at=matter_stage_updated_at,
            number=number,
            open_date=open_date,
            pending_date=pending_date,
            shared=shared,
            status=status,
            updated_at=updated_at,
        )

        medical_record_matter.additional_properties = d
        return medical_record_matter

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
