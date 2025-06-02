from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_set_list import CustomFieldSetList
from ...models.custom_field_setindex_order import CustomFieldSetindexOrder
from ...models.custom_field_setindex_parent_type import CustomFieldSetindexParentType
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_since: Union[Unset, str] = UNSET,
    displayed: Union[Unset, bool] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, CustomFieldSetindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    parent_type: Union[Unset, CustomFieldSetindexParentType] = UNSET,
    query: Union[Unset, str] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["created_since"] = created_since

    params["displayed"] = displayed

    params["fields"] = fields

    params["ids[]"] = ids

    params["limit"] = limit

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    json_parent_type: Union[Unset, str] = UNSET
    if not isinstance(parent_type, Unset):
        json_parent_type = parent_type.value

    params["parent_type"] = json_parent_type

    params["query"] = query

    params["updated_since"] = updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/custom_field_sets.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CustomFieldSetList, Error]]:
    if response.status_code == 200:
        response_200 = CustomFieldSetList.from_dict(response.json())

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
) -> Response[Union[CustomFieldSetList, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, str] = UNSET,
    displayed: Union[Unset, bool] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, CustomFieldSetindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    parent_type: Union[Unset, CustomFieldSetindexParentType] = UNSET,
    query: Union[Unset, str] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[CustomFieldSetList, Error]]:
    """Return the data for all CustomFieldSets

     Outlines the parameters, optional and required, used when requesting the data for all
    CustomFieldSets

    Args:
        created_since (Union[Unset, str]):
        displayed (Union[Unset, bool]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, CustomFieldSetindexOrder]):
        page_token (Union[Unset, str]):
        parent_type (Union[Unset, CustomFieldSetindexParentType]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomFieldSetList, Error]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        displayed=displayed,
        fields=fields,
        ids=ids,
        limit=limit,
        order=order,
        page_token=page_token,
        parent_type=parent_type,
        query=query,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, str] = UNSET,
    displayed: Union[Unset, bool] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, CustomFieldSetindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    parent_type: Union[Unset, CustomFieldSetindexParentType] = UNSET,
    query: Union[Unset, str] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[CustomFieldSetList, Error]]:
    """Return the data for all CustomFieldSets

     Outlines the parameters, optional and required, used when requesting the data for all
    CustomFieldSets

    Args:
        created_since (Union[Unset, str]):
        displayed (Union[Unset, bool]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, CustomFieldSetindexOrder]):
        page_token (Union[Unset, str]):
        parent_type (Union[Unset, CustomFieldSetindexParentType]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomFieldSetList, Error]
    """

    return sync_detailed(
        client=client,
        created_since=created_since,
        displayed=displayed,
        fields=fields,
        ids=ids,
        limit=limit,
        order=order,
        page_token=page_token,
        parent_type=parent_type,
        query=query,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, str] = UNSET,
    displayed: Union[Unset, bool] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, CustomFieldSetindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    parent_type: Union[Unset, CustomFieldSetindexParentType] = UNSET,
    query: Union[Unset, str] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[CustomFieldSetList, Error]]:
    """Return the data for all CustomFieldSets

     Outlines the parameters, optional and required, used when requesting the data for all
    CustomFieldSets

    Args:
        created_since (Union[Unset, str]):
        displayed (Union[Unset, bool]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, CustomFieldSetindexOrder]):
        page_token (Union[Unset, str]):
        parent_type (Union[Unset, CustomFieldSetindexParentType]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomFieldSetList, Error]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        displayed=displayed,
        fields=fields,
        ids=ids,
        limit=limit,
        order=order,
        page_token=page_token,
        parent_type=parent_type,
        query=query,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    created_since: Union[Unset, str] = UNSET,
    displayed: Union[Unset, bool] = UNSET,
    fields: Union[Unset, str] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, CustomFieldSetindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    parent_type: Union[Unset, CustomFieldSetindexParentType] = UNSET,
    query: Union[Unset, str] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[CustomFieldSetList, Error]]:
    """Return the data for all CustomFieldSets

     Outlines the parameters, optional and required, used when requesting the data for all
    CustomFieldSets

    Args:
        created_since (Union[Unset, str]):
        displayed (Union[Unset, bool]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, CustomFieldSetindexOrder]):
        page_token (Union[Unset, str]):
        parent_type (Union[Unset, CustomFieldSetindexParentType]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomFieldSetList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            created_since=created_since,
            displayed=displayed,
            fields=fields,
            ids=ids,
            limit=limit,
            order=order,
            page_token=page_token,
            parent_type=parent_type,
            query=query,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
