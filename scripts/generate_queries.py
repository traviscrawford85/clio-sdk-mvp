"""
Matter Queries

This module provides read-only access to Matter data from Clio.
It wraps the clio_async_client API and converts results into high-level SDK models.
"""

from clio_async_client.api.matters import raw_list_matters, raw_get_matter
from clio_async_client.client import AuthenticatedClient

# from clio_client.models.matter_update_request import MatterUpdateRequest
# from clio_client.models.matter_update_request_data import MatterUpdateRequestData
# from clio_client.models.matter_update_request_data_custom_field_values_inner import (
#     MatterUpdateRequestDataCustomFieldValuesInner,
# )
# from clio_client.models.matter_update_request_data_relationships_inner_contact import (
#     MatterUpdateRequestDataRelationshipsInnerContact as MatterUpdateRequestDataResponsibleStaff,
# )
# from clio_client.models.matter_update_request_data_statute_of_limitations import (
#     MatterUpdateRequestDataStatuteOfLimitations,
# )
from clio_sdk.adapter_factory import get_adapter

# from clio_sdk.queries.matter_builders import build_full_update_request

# --- Async Query Functions ---


async def list_matters(client: AuthenticatedClient) -> list:
    """Returns all matters as SDK models"""
    resp = await raw_list_matters(client=client)
    if resp.status_code == 200 and resp.parsed:
        adapter = get_adapter("matter")
        return [adapter["from_clio"](m) for m in resp.parsed.matters]
    return []


async def get_matter_by_id(client: AuthenticatedClient, matter_id: int):
    """Returns a single matter by ID"""
    resp = await raw_get_matter(client=client, id=matter_id)
    if resp.status_code == 200 and resp.parsed:
        adapter = get_adapter("matter")
        return adapter["from_clio"](resp.parsed.matter)
    return None


# --- Rich Async Query Scaffolds (placeholders, to be implemented) ---


async def list_tasks_by_matter(_client: AuthenticatedClient, _matter_id: int) -> list:
    """Returns tasks linked to a specific matter ID."""
    # TODO: Call task API with filter by matter_id, map to Task model
    return []


async def delete_empty_customfields_on_matter(
    _client: AuthenticatedClient, _matter_id: int
) -> bool:
    """Deletes any custom fields on a matter that have no value."""
    # TODO: Fetch custom fields, check for empty values, issue DELETEs
    return True


async def update_matter_info(
    _client: AuthenticatedClient, _matter_id: int, _updates: dict
):
    """Updates a matter's info based on provided fields."""
    # TODO: Transform dict to ClioMatterBase and PATCH
    return None


async def batch_update_matter_status(
    _client: AuthenticatedClient, _matter_ids: list[int], _status: str
) -> list:
    """Batch update status field for multiple matters."""
    # TODO: Loop through matter_ids, patch each with new status
    return []


async def batch_update_matter_responsible_staff(
    _client: AuthenticatedClient, _matter_ids: list[int], _user_id: int
) -> list:
    """Batch assign a responsible staff member to multiple matters."""
    # TODO: Patch each matter with responsible attorney/user_id
    return []


async def list_matters_missing_date_of_incident(_client: AuthenticatedClient) -> list:
    """Returns all matters with no date_of_incident field set."""
    # TODO: Filter matters where date_of_incident is null or missing
    return []


async def list_matters_with_limitations_date_due_this_month(
    _client: AuthenticatedClient,
) -> list:
    """Returns matters whose limitations date falls within the current month."""
    # TODO: Filter matters by limitations_date within this month
    return []


# --- Model Update Builder (sync is fine here) ---


def build_update_request_from_model(_matter):
    # logic as in builder, converting to MatterUpdateRequestData
    # data = MatterUpdateRequestData()  # populate fields as needed from 'matter'
    # return MatterUpdateRequest(data=data)
    pass

    # def build_full_update_request(input) -> MatterUpdateRequest:
    #     data_kwargs = {
    #         "description": input.description,
    #         "status": input.status,
    #         "close_date": input.close_date,
    #         "open_date": input.open_date,
    #     }
    #
    #     if input.responsible_staff:
    #         data_kwargs["responsible_staff"] = MatterUpdateRequestDataResponsibleStaff(
    #             id=input.responsible_staff.id
    #         )
    #
    #     if input.practice_area:
    #         data_kwargs["practice_area"] = {"id": input.practice_area.id}
    #
    #     if input.group:
    #         data_kwargs["group"] = {"id": input.group.id}
    #
    #     if input.statute_of_limitations:
    #         data_kwargs["statute_of_limitations"] = (
    #             MatterUpdateRequestDataStatuteOfLimitations(
    #                 due_at=input.statute_of_limitations.due_at
    #             )
    #         )
    #
    #     if input.custom_field_values:
    #         cf_values = []
    #         for cf in input.custom_field_values:
    #             kwargs = {"id": cf.id, "value": cf.value}
    #             if hasattr(cf, "custom_field") and cf.custom_field:
    #                 kwargs["custom_field"] = cf.custom_field
    #             cf_values.append(MatterUpdateRequestDataCustomFieldValuesInner(**kwargs))
    #         data_kwargs["custom_field_values"] = cf_values
    #
    #     return MatterUpdateRequest(data=MatterUpdateRequestData(**data_kwargs))
    return MatterUpdateRequest(data=MatterUpdateRequestData(**data_kwargs))
