from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.conversation_list import ConversationList
from ...models.conversationindex_order import ConversationindexOrder
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: Union[Unset, bool] = UNSET,
    contact_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    for_user: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, ConversationindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    read_status: Union[Unset, bool] = UNSET,
    time_entries: Union[Unset, bool] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["archived"] = archived

    params["contact_id"] = contact_id

    params["created_since"] = created_since

    params["date"] = date

    params["fields"] = fields

    params["for_user"] = for_user

    params["ids[]"] = ids

    params["limit"] = limit

    params["matter_id"] = matter_id

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params["read_status"] = read_status

    params["time_entries"] = time_entries

    params["updated_since"] = updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/conversations.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ConversationList, Error]]:
    if response.status_code == 200:
        response_200 = ConversationList.from_dict(response.json())

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
) -> Response[Union[ConversationList, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    archived: Union[Unset, bool] = UNSET,
    contact_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    for_user: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, ConversationindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    read_status: Union[Unset, bool] = UNSET,
    time_entries: Union[Unset, bool] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[ConversationList, Error]]:
    """Return the data for all Conversations

     Outlines the parameters, optional and required, used when requesting the data for all Conversations

    Args:
        archived (Union[Unset, bool]):
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        date (Union[Unset, str]):
        fields (Union[Unset, str]):
        for_user (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, ConversationindexOrder]):
        page_token (Union[Unset, str]):
        read_status (Union[Unset, bool]):
        time_entries (Union[Unset, bool]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConversationList, Error]]
    """

    kwargs = _get_kwargs(
        archived=archived,
        contact_id=contact_id,
        created_since=created_since,
        date=date,
        fields=fields,
        for_user=for_user,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        read_status=read_status,
        time_entries=time_entries,
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
    archived: Union[Unset, bool] = UNSET,
    contact_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    for_user: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, ConversationindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    read_status: Union[Unset, bool] = UNSET,
    time_entries: Union[Unset, bool] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[ConversationList, Error]]:
    """Return the data for all Conversations

     Outlines the parameters, optional and required, used when requesting the data for all Conversations

    Args:
        archived (Union[Unset, bool]):
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        date (Union[Unset, str]):
        fields (Union[Unset, str]):
        for_user (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, ConversationindexOrder]):
        page_token (Union[Unset, str]):
        read_status (Union[Unset, bool]):
        time_entries (Union[Unset, bool]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConversationList, Error]
    """

    return sync_detailed(
        client=client,
        archived=archived,
        contact_id=contact_id,
        created_since=created_since,
        date=date,
        fields=fields,
        for_user=for_user,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        read_status=read_status,
        time_entries=time_entries,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    archived: Union[Unset, bool] = UNSET,
    contact_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    for_user: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, ConversationindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    read_status: Union[Unset, bool] = UNSET,
    time_entries: Union[Unset, bool] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[ConversationList, Error]]:
    """Return the data for all Conversations

     Outlines the parameters, optional and required, used when requesting the data for all Conversations

    Args:
        archived (Union[Unset, bool]):
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        date (Union[Unset, str]):
        fields (Union[Unset, str]):
        for_user (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, ConversationindexOrder]):
        page_token (Union[Unset, str]):
        read_status (Union[Unset, bool]):
        time_entries (Union[Unset, bool]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConversationList, Error]]
    """

    kwargs = _get_kwargs(
        archived=archived,
        contact_id=contact_id,
        created_since=created_since,
        date=date,
        fields=fields,
        for_user=for_user,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        read_status=read_status,
        time_entries=time_entries,
        updated_since=updated_since,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    archived: Union[Unset, bool] = UNSET,
    contact_id: Union[Unset, int] = UNSET,
    created_since: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    for_user: Union[Unset, bool] = UNSET,
    ids: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    matter_id: Union[Unset, int] = UNSET,
    order: Union[Unset, ConversationindexOrder] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    read_status: Union[Unset, bool] = UNSET,
    time_entries: Union[Unset, bool] = UNSET,
    updated_since: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[ConversationList, Error]]:
    """Return the data for all Conversations

     Outlines the parameters, optional and required, used when requesting the data for all Conversations

    Args:
        archived (Union[Unset, bool]):
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        date (Union[Unset, str]):
        fields (Union[Unset, str]):
        for_user (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, ConversationindexOrder]):
        page_token (Union[Unset, str]):
        read_status (Union[Unset, bool]):
        time_entries (Union[Unset, bool]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConversationList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            contact_id=contact_id,
            created_since=created_since,
            date=date,
            fields=fields,
            for_user=for_user,
            ids=ids,
            limit=limit,
            matter_id=matter_id,
            order=order,
            page_token=page_token,
            read_status=read_status,
            time_entries=time_entries,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
