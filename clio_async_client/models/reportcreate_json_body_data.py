from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reportcreate_json_body_data_format import ReportcreateJsonBodyDataFormat
from ..models.reportcreate_json_body_data_kind import ReportcreateJsonBodyDataKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reportcreate_json_body_data_client import (
        ReportcreateJsonBodyDataClient,
    )
    from ..models.reportcreate_json_body_data_matter import (
        ReportcreateJsonBodyDataMatter,
    )
    from ..models.reportcreate_json_body_data_originating_attorney import (
        ReportcreateJsonBodyDataOriginatingAttorney,
    )
    from ..models.reportcreate_json_body_data_practice_area import (
        ReportcreateJsonBodyDataPracticeArea,
    )
    from ..models.reportcreate_json_body_data_responsible_attorney import (
        ReportcreateJsonBodyDataResponsibleAttorney,
    )
    from ..models.reportcreate_json_body_data_user import ReportcreateJsonBodyDataUser


T = TypeVar("T", bound="ReportcreateJsonBodyData")


@_attrs_define
class ReportcreateJsonBodyData:
    """
    Attributes:
        format_ (ReportcreateJsonBodyDataFormat): What format the Report will be generated in.
        kind (ReportcreateJsonBodyDataKind): What kind of Report will be generated.
        client (Union[Unset, ReportcreateJsonBodyDataClient]):
        end_date (Union[Unset, str]): Filters Report data by date. (Expects an ISO-8601 date).
        matter (Union[Unset, ReportcreateJsonBodyDataMatter]):
        originating_attorney (Union[Unset, ReportcreateJsonBodyDataOriginatingAttorney]):
        practice_area (Union[Unset, ReportcreateJsonBodyDataPracticeArea]):
        responsible_attorney (Union[Unset, ReportcreateJsonBodyDataResponsibleAttorney]):
        start_date (Union[Unset, str]): Filters Report data by date. (Expects an ISO-8601 date).
        user (Union[Unset, ReportcreateJsonBodyDataUser]):
        year (Union[Unset, str]): Filters Report data by year. Sets start_date and end_date. (Expects a year).
    """

    format_: ReportcreateJsonBodyDataFormat
    kind: ReportcreateJsonBodyDataKind
    client: Union[Unset, "ReportcreateJsonBodyDataClient"] = UNSET
    end_date: Union[Unset, str] = UNSET
    matter: Union[Unset, "ReportcreateJsonBodyDataMatter"] = UNSET
    originating_attorney: Union[Unset, "ReportcreateJsonBodyDataOriginatingAttorney"] = UNSET
    practice_area: Union[Unset, "ReportcreateJsonBodyDataPracticeArea"] = UNSET
    responsible_attorney: Union[Unset, "ReportcreateJsonBodyDataResponsibleAttorney"] = UNSET
    start_date: Union[Unset, str] = UNSET
    user: Union[Unset, "ReportcreateJsonBodyDataUser"] = UNSET
    year: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_.value

        kind = self.kind.value

        client: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        end_date = self.end_date

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        originating_attorney: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.originating_attorney, Unset):
            originating_attorney = self.originating_attorney.to_dict()

        practice_area: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.practice_area, Unset):
            practice_area = self.practice_area.to_dict()

        responsible_attorney: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.responsible_attorney, Unset):
            responsible_attorney = self.responsible_attorney.to_dict()

        start_date = self.start_date

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
                "kind": kind,
            }
        )
        if client is not UNSET:
            field_dict["client"] = client
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if matter is not UNSET:
            field_dict["matter"] = matter
        if originating_attorney is not UNSET:
            field_dict["originating_attorney"] = originating_attorney
        if practice_area is not UNSET:
            field_dict["practice_area"] = practice_area
        if responsible_attorney is not UNSET:
            field_dict["responsible_attorney"] = responsible_attorney
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if user is not UNSET:
            field_dict["user"] = user
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reportcreate_json_body_data_client import (
            ReportcreateJsonBodyDataClient,
        )
        from ..models.reportcreate_json_body_data_matter import (
            ReportcreateJsonBodyDataMatter,
        )
        from ..models.reportcreate_json_body_data_originating_attorney import (
            ReportcreateJsonBodyDataOriginatingAttorney,
        )
        from ..models.reportcreate_json_body_data_practice_area import (
            ReportcreateJsonBodyDataPracticeArea,
        )
        from ..models.reportcreate_json_body_data_responsible_attorney import (
            ReportcreateJsonBodyDataResponsibleAttorney,
        )
        from ..models.reportcreate_json_body_data_user import (
            ReportcreateJsonBodyDataUser,
        )

        d = dict(src_dict)
        format_ = ReportcreateJsonBodyDataFormat(d.pop("format"))

        kind = ReportcreateJsonBodyDataKind(d.pop("kind"))

        _client = d.pop("client", UNSET)
        client: Union[Unset, ReportcreateJsonBodyDataClient]
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = ReportcreateJsonBodyDataClient.from_dict(_client)

        end_date = d.pop("end_date", UNSET)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, ReportcreateJsonBodyDataMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = ReportcreateJsonBodyDataMatter.from_dict(_matter)

        _originating_attorney = d.pop("originating_attorney", UNSET)
        originating_attorney: Union[Unset, ReportcreateJsonBodyDataOriginatingAttorney]
        if isinstance(_originating_attorney, Unset):
            originating_attorney = UNSET
        else:
            originating_attorney = ReportcreateJsonBodyDataOriginatingAttorney.from_dict(_originating_attorney)

        _practice_area = d.pop("practice_area", UNSET)
        practice_area: Union[Unset, ReportcreateJsonBodyDataPracticeArea]
        if isinstance(_practice_area, Unset):
            practice_area = UNSET
        else:
            practice_area = ReportcreateJsonBodyDataPracticeArea.from_dict(_practice_area)

        _responsible_attorney = d.pop("responsible_attorney", UNSET)
        responsible_attorney: Union[Unset, ReportcreateJsonBodyDataResponsibleAttorney]
        if isinstance(_responsible_attorney, Unset):
            responsible_attorney = UNSET
        else:
            responsible_attorney = ReportcreateJsonBodyDataResponsibleAttorney.from_dict(_responsible_attorney)

        start_date = d.pop("start_date", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ReportcreateJsonBodyDataUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ReportcreateJsonBodyDataUser.from_dict(_user)

        year = d.pop("year", UNSET)

        reportcreate_json_body_data = cls(
            format_=format_,
            kind=kind,
            client=client,
            end_date=end_date,
            matter=matter,
            originating_attorney=originating_attorney,
            practice_area=practice_area,
            responsible_attorney=responsible_attorney,
            start_date=start_date,
            user=user,
            year=year,
        )

        reportcreate_json_body_data.additional_properties = d
        return reportcreate_json_body_data

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
