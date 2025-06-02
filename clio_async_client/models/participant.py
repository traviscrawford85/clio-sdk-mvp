from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.participant_base_type import ParticipantBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.participant_avatar import ParticipantAvatar


T = TypeVar("T", bound="Participant")


@_attrs_define
class Participant:
    """
    Attributes:
        created_at (Union[Unset, str]): The time the *Participant* was created (as a ISO-8601 timestamp)
        enabled (Union[Unset, bool]): The enabled state of the *Participant* record. Always 'null' if *Participant* type
            is Contact
        etag (Union[Unset, str]): ETag for the *Participant*
        id (Union[Unset, int]): Unique identifier for the *Participant*
        identifier (Union[Unset, str]): A string to identify the *Participant*
        initials (Union[Unset, str]): A  string with the participant initials
        job_title_name (Union[Unset, str]): the job title name of the participant if they are a firm user and have one
        name (Union[Unset, str]): The name of the *Participant* record
        secondary_identifier (Union[Unset, str]): A secondary string to identify the *Participant*
        type_ (Union[Unset, ParticipantBaseType]): The type of the Participant. Person and Company are subtypes of
            Contact
        updated_at (Union[Unset, str]): The time the *Participant* was last updated (as a ISO-8601 timestamp)
        avatar (Union[Unset, ParticipantAvatar]):
    """

    created_at: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    identifier: Union[Unset, str] = UNSET
    initials: Union[Unset, str] = UNSET
    job_title_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    secondary_identifier: Union[Unset, str] = UNSET
    type_: Union[Unset, ParticipantBaseType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    avatar: Union[Unset, "ParticipantAvatar"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        enabled = self.enabled

        etag = self.etag

        id = self.id

        identifier = self.identifier

        initials = self.initials

        job_title_name = self.job_title_name

        name = self.name

        secondary_identifier = self.secondary_identifier

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at = self.updated_at

        avatar: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if initials is not UNSET:
            field_dict["initials"] = initials
        if job_title_name is not UNSET:
            field_dict["job_title_name"] = job_title_name
        if name is not UNSET:
            field_dict["name"] = name
        if secondary_identifier is not UNSET:
            field_dict["secondary_identifier"] = secondary_identifier
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if avatar is not UNSET:
            field_dict["avatar"] = avatar

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.participant_avatar import ParticipantAvatar

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        enabled = d.pop("enabled", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        initials = d.pop("initials", UNSET)

        job_title_name = d.pop("job_title_name", UNSET)

        name = d.pop("name", UNSET)

        secondary_identifier = d.pop("secondary_identifier", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ParticipantBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ParticipantBaseType(_type_)

        updated_at = d.pop("updated_at", UNSET)

        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, ParticipantAvatar]
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = ParticipantAvatar.from_dict(_avatar)

        participant = cls(
            created_at=created_at,
            enabled=enabled,
            etag=etag,
            id=id,
            identifier=identifier,
            initials=initials,
            job_title_name=job_title_name,
            name=name,
            secondary_identifier=secondary_identifier,
            type_=type_,
            updated_at=updated_at,
            avatar=avatar,
        )

        participant.additional_properties = d
        return participant

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
