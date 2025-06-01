from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.group_list import GroupList
from ...models.groupindex_order import GroupindexOrder
from ...models.groupindex_type import GroupindexType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: Unset | bool = UNSET,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    name: Unset | str = UNSET,
    order: Unset | GroupindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    type_: Unset | GroupindexType = UNSET,
    updated_since: Unset | str = UNSET,
    user_id: Unset | int = UNSET,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["archived"] = archived

    params["created_since"] = created_since

    params["fields"] = fields

    params["ids[]"] = ids

    params["limit"] = limit

    params["name"] = name

    json_order: Unset | str = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params["query"] = query

    json_type_: Unset | str = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["updated_since"] = updated_since

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | GroupList | None:
    if response.status_code == 200:
        response_200 = GroupList.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | GroupList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    archived: Unset | bool = UNSET,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    name: Unset | str = UNSET,
    order: Unset | GroupindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    type_: Unset | GroupindexType = UNSET,
    updated_since: Unset | str = UNSET,
    user_id: Unset | int = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | GroupList]:
    """Return the data for all Groups

     Outlines the parameters, optional and required, used when requesting the data for all Groups

    Args:
        archived (Union[Unset, bool]):
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        order (Union[Unset, GroupindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        type_ (Union[Unset, GroupindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GroupList]]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        name=name,
        order=order,
        page_token=page_token,
        query=query,
        type_=type_,
        updated_since=updated_since,
        user_id=user_id,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    archived: Unset | bool = UNSET,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    name: Unset | str = UNSET,
    order: Unset | GroupindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    type_: Unset | GroupindexType = UNSET,
    updated_since: Unset | str = UNSET,
    user_id: Unset | int = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | GroupList | None:
    """Return the data for all Groups

     Outlines the parameters, optional and required, used when requesting the data for all Groups

    Args:
        archived (Union[Unset, bool]):
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        order (Union[Unset, GroupindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        type_ (Union[Unset, GroupindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GroupList]
    """

    return sync_detailed(
        client=client,
        archived=archived,
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        name=name,
        order=order,
        page_token=page_token,
        query=query,
        type_=type_,
        updated_since=updated_since,
        user_id=user_id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    archived: Unset | bool = UNSET,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    name: Unset | str = UNSET,
    order: Unset | GroupindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    type_: Unset | GroupindexType = UNSET,
    updated_since: Unset | str = UNSET,
    user_id: Unset | int = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | GroupList]:
    """Return the data for all Groups

     Outlines the parameters, optional and required, used when requesting the data for all Groups

    Args:
        archived (Union[Unset, bool]):
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        order (Union[Unset, GroupindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        type_ (Union[Unset, GroupindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GroupList]]
    """

    kwargs = _get_kwargs(
        archived=archived,
        created_since=created_since,
        fields=fields,
        ids=ids,
        limit=limit,
        name=name,
        order=order,
        page_token=page_token,
        query=query,
        type_=type_,
        updated_since=updated_since,
        user_id=user_id,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    archived: Unset | bool = UNSET,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    name: Unset | str = UNSET,
    order: Unset | GroupindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    type_: Unset | GroupindexType = UNSET,
    updated_since: Unset | str = UNSET,
    user_id: Unset | int = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | GroupList | None:
    """Return the data for all Groups

     Outlines the parameters, optional and required, used when requesting the data for all Groups

    Args:
        archived (Union[Unset, bool]):
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        order (Union[Unset, GroupindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        type_ (Union[Unset, GroupindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GroupList]
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            created_since=created_since,
            fields=fields,
            ids=ids,
            limit=limit,
            name=name,
            order=order,
            page_token=page_token,
            query=query,
            type_=type_,
            updated_since=updated_since,
            user_id=user_id,
            x_api_version=x_api_version,
        )
    ).parsed
