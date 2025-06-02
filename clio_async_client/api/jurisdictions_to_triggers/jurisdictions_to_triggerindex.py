from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.jurisdictions_to_trigger_list import JurisdictionsToTriggerList
from ...models.jurisdictions_to_triggerindex_order import (
    JurisdictionsToTriggerindexOrder,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    jurisdiction_id: int,
    *,
    created_since: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    is_requirements_required: Union[Unset, bool] = UNSET,
    is_served: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, JurisdictionsToTriggerindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["created_since"] = created_since

    params["fields"] = fields

    params["ids[]"] = ids

    params["is_requirements_required"] = is_requirements_required

    params["is_served"] = is_served

    params["limit"] = limit

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params["query"] = query

    params["updated_since"] = updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/court_rules/jurisdictions/{jurisdiction_id}/triggers.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, JurisdictionsToTriggerList]]:
    if response.status_code == 200:
        response_200 = JurisdictionsToTriggerList.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, JurisdictionsToTriggerList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    jurisdiction_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    is_requirements_required: Union[Unset, bool] = UNSET,
    is_served: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, JurisdictionsToTriggerindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, JurisdictionsToTriggerList]]:
    """Return the data for all triggers

     Outlines the parameters, optional and required, used when requesting the data for all
    JurisdictionsToTriggers

    Args:
        jurisdiction_id (int):
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        is_requirements_required (Union[Unset, bool]):
        is_served (Union[Unset, bool]):
        limit (Union[Unset, int]):
        order (Union[Unset, JurisdictionsToTriggerindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, JurisdictionsToTriggerList]]
    """

    kwargs = _get_kwargs(
        jurisdiction_id=jurisdiction_id,
        created_since=created_since,
        fields=fields,
        ids=ids,
        is_requirements_required=is_requirements_required,
        is_served=is_served,
        limit=limit,
        order=order,
        page_token=page_token,
        query=query,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    jurisdiction_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    is_requirements_required: Union[Unset, bool] = UNSET,
    is_served: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, JurisdictionsToTriggerindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, JurisdictionsToTriggerList]]:
    """Return the data for all triggers

     Outlines the parameters, optional and required, used when requesting the data for all
    JurisdictionsToTriggers

    Args:
        jurisdiction_id (int):
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        is_requirements_required (Union[Unset, bool]):
        is_served (Union[Unset, bool]):
        limit (Union[Unset, int]):
        order (Union[Unset, JurisdictionsToTriggerindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, JurisdictionsToTriggerList]
    """

    return sync_detailed(
        jurisdiction_id=jurisdiction_id,
        client=client,
        created_since=created_since,
        fields=fields,
        ids=ids,
        is_requirements_required=is_requirements_required,
        is_served=is_served,
        limit=limit,
        order=order,
        page_token=page_token,
        query=query,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    jurisdiction_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    is_requirements_required: Union[Unset, bool] = UNSET,
    is_served: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, JurisdictionsToTriggerindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, JurisdictionsToTriggerList]]:
    """Return the data for all triggers

     Outlines the parameters, optional and required, used when requesting the data for all
    JurisdictionsToTriggers

    Args:
        jurisdiction_id (int):
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        is_requirements_required (Union[Unset, bool]):
        is_served (Union[Unset, bool]):
        limit (Union[Unset, int]):
        order (Union[Unset, JurisdictionsToTriggerindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, JurisdictionsToTriggerList]]
    """

    kwargs = _get_kwargs(
        jurisdiction_id=jurisdiction_id,
        created_since=created_since,
        fields=fields,
        ids=ids,
        is_requirements_required=is_requirements_required,
        is_served=is_served,
        limit=limit,
        order=order,
        page_token=page_token,
        query=query,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    jurisdiction_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    is_requirements_required: Union[Unset, bool] = UNSET,
    is_served: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, JurisdictionsToTriggerindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, JurisdictionsToTriggerList]]:
    """Return the data for all triggers

     Outlines the parameters, optional and required, used when requesting the data for all
    JurisdictionsToTriggers

    Args:
        jurisdiction_id (int):
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        is_requirements_required (Union[Unset, bool]):
        is_served (Union[Unset, bool]):
        limit (Union[Unset, int]):
        order (Union[Unset, JurisdictionsToTriggerindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, JurisdictionsToTriggerList]
    """

    return (
        await asyncio_detailed(
            jurisdiction_id=jurisdiction_id,
            client=client,
            created_since=created_since,
            fields=fields,
            ids=ids,
            is_requirements_required=is_requirements_required,
            is_served=is_served,
            limit=limit,
            order=order,
            page_token=page_token,
            query=query,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
