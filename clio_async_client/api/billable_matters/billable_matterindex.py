from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billable_matter_list import BillableMatterList
from ...models.billable_matterindex_custom_field_values import (
    BillableMatterindexCustomFieldValues,
)
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client_id: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, BillableMatterindexCustomFieldValues] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["client_id"] = client_id

    json_custom_field_values: Union[Unset, str] = UNSET
    if not isinstance(custom_field_values, Unset):
        json_custom_field_values = custom_field_values.value

    params["custom_field_values"] = json_custom_field_values

    params["end_date"] = end_date

    params["fields"] = fields

    params["limit"] = limit

    params["matter_id"] = matter_id

    params["originating_attorney_id"] = originating_attorney_id

    params["page_token"] = page_token

    params["query"] = query

    params["responsible_attorney_id"] = responsible_attorney_id

    params["start_date"] = start_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/billable_matters.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BillableMatterList, Error]]:
    if response.status_code == 200:
        response_200 = BillableMatterList.from_dict(response.json())

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
) -> Response[Union[BillableMatterList, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    client_id: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, BillableMatterindexCustomFieldValues] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[BillableMatterList, Error]]:
    """Return the data for all BillableMatters

     Outlines the parameters, optional and required, used when requesting the data for all
    BillableMatters

    Args:
        client_id (Union[Unset, int]):
        custom_field_values (Union[Unset, BillableMatterindexCustomFieldValues]):
        end_date (Union[Unset, str]):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        originating_attorney_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        start_date (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillableMatterList, Error]]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        custom_field_values=custom_field_values,
        end_date=end_date,
        fields=fields,
        limit=limit,
        matter_id=matter_id,
        originating_attorney_id=originating_attorney_id,
        page_token=page_token,
        query=query,
        responsible_attorney_id=responsible_attorney_id,
        start_date=start_date,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    client_id: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, BillableMatterindexCustomFieldValues] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[BillableMatterList, Error]]:
    """Return the data for all BillableMatters

     Outlines the parameters, optional and required, used when requesting the data for all
    BillableMatters

    Args:
        client_id (Union[Unset, int]):
        custom_field_values (Union[Unset, BillableMatterindexCustomFieldValues]):
        end_date (Union[Unset, str]):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        originating_attorney_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        start_date (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BillableMatterList, Error]
    """

    return sync_detailed(
        client=client,
        client_id=client_id,
        custom_field_values=custom_field_values,
        end_date=end_date,
        fields=fields,
        limit=limit,
        matter_id=matter_id,
        originating_attorney_id=originating_attorney_id,
        page_token=page_token,
        query=query,
        responsible_attorney_id=responsible_attorney_id,
        start_date=start_date,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    client_id: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, BillableMatterindexCustomFieldValues] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[BillableMatterList, Error]]:
    """Return the data for all BillableMatters

     Outlines the parameters, optional and required, used when requesting the data for all
    BillableMatters

    Args:
        client_id (Union[Unset, int]):
        custom_field_values (Union[Unset, BillableMatterindexCustomFieldValues]):
        end_date (Union[Unset, str]):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        originating_attorney_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        start_date (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillableMatterList, Error]]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        custom_field_values=custom_field_values,
        end_date=end_date,
        fields=fields,
        limit=limit,
        matter_id=matter_id,
        originating_attorney_id=originating_attorney_id,
        page_token=page_token,
        query=query,
        responsible_attorney_id=responsible_attorney_id,
        start_date=start_date,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    client_id: Union[Unset, int] = UNSET,
    custom_field_values: Union[Unset, BillableMatterindexCustomFieldValues] = UNSET,
    end_date: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    start_date: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[BillableMatterList, Error]]:
    """Return the data for all BillableMatters

     Outlines the parameters, optional and required, used when requesting the data for all
    BillableMatters

    Args:
        client_id (Union[Unset, int]):
        custom_field_values (Union[Unset, BillableMatterindexCustomFieldValues]):
        end_date (Union[Unset, str]):
        fields (Union[Unset, str]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        originating_attorney_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        start_date (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BillableMatterList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            client_id=client_id,
            custom_field_values=custom_field_values,
            end_date=end_date,
            fields=fields,
            limit=limit,
            matter_id=matter_id,
            originating_attorney_id=originating_attorney_id,
            page_token=page_token,
            query=query,
            responsible_attorney_id=responsible_attorney_id,
            start_date=start_date,
            x_api_version=x_api_version,
        )
    ).parsed
