# adapter_factory/matter.py

from clio_client.models import (
    MatterUpdateRequest,
    MatterUpdateRequestData,
    MatterUpdateRequestDataCustomFieldValuesInner,
)
from clio_client.models import (
    MatterUpdateRequestDataRelationshipsInnerContact as MatterUpdateRequestDataResponsibleStaff,
)
from clio_client.models import MatterUpdateRequestDataStatuteOfLimitations
from clio_sdk.adapter_factory import register_adapter
from clio_sdk.unified_models.matter import MatterUpdateInputModel


@register_adapter("matter")
def to_clio(input: MatterUpdateInputModel) -> MatterUpdateRequest:
    data_kwargs = {
        "description": input.description,
        "status": input.status,
        "close_date": input.close_date,
        "open_date": input.open_date,
    }

    if input.responsible_staff:
        data_kwargs["responsible_staff"] = MatterUpdateRequestDataResponsibleStaff(
            id=input.responsible_staff.id
        )

    if input.practice_area:
        data_kwargs["practice_area"] = {"id": input.practice_area.id}

    if input.group:
        data_kwargs["group"] = {"id": input.group.id}

    if input.statute_of_limitations:
        data_kwargs["statute_of_limitations"] = (
            MatterUpdateRequestDataStatuteOfLimitations(
                due_at=input.statute_of_limitations.due_at
            )
        )

    if input.custom_field_values:
        cf_values = []
        for cf in input.custom_field_values:
            kwargs = {"id": cf.id, "value": cf.value}
            if cf.custom_field:
                kwargs["custom_field"] = cf.custom_field
            cf_values.append(MatterUpdateRequestDataCustomFieldValuesInner(**kwargs))
        data_kwargs["custom_field_values"] = cf_values

    return MatterUpdateRequest(data=MatterUpdateRequestData(**data_kwargs))
