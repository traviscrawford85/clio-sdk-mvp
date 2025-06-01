from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.communication_list import CommunicationList
from ...models.communicationindex_order import CommunicationindexOrder
from ...models.communicationindex_type import CommunicationindexType
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    contact_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    date: Unset | str = UNSET,
    external_property_name: Unset | str = UNSET,
    external_property_value: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    having_time_entries: Unset | bool = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | CommunicationindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    received_at: Unset | str = UNSET,
    received_before: Unset | str = UNSET,
    received_since: Unset | str = UNSET,
    type_: Unset | CommunicationindexType = UNSET,
    updated_since: Unset | str = UNSET,
    user_id: Unset | int = UNSET,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["contact_id"] = contact_id

    params["created_since"] = created_since

    params["date"] = date

    params["external_property_name"] = external_property_name

    params["external_property_value"] = external_property_value

    params["fields"] = fields

    params["having_time_entries"] = having_time_entries

    params["ids[]"] = ids

    params["limit"] = limit

    params["matter_id"] = matter_id

    json_order: Unset | str = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params["query"] = query

    params["received_at"] = received_at

    params["received_before"] = received_before

    params["received_since"] = received_since

    json_type_: Unset | str = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["updated_since"] = updated_since

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/communications.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommunicationList | Error | None:
    if response.status_code == 200:
        response_200 = CommunicationList.from_dict(response.json())

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
) -> Response[CommunicationList | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    contact_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    date: Unset | str = UNSET,
    external_property_name: Unset | str = UNSET,
    external_property_value: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    having_time_entries: Unset | bool = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | CommunicationindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    received_at: Unset | str = UNSET,
    received_before: Unset | str = UNSET,
    received_since: Unset | str = UNSET,
    type_: Unset | CommunicationindexType = UNSET,
    updated_since: Unset | str = UNSET,
    user_id: Unset | int = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[CommunicationList | Error]:
    """Return the data for all Communications

     Outlines the parameters, optional and required, used when requesting the data for all Communications

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        date (Union[Unset, str]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        having_time_entries (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, CommunicationindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        received_at (Union[Unset, str]):
        received_before (Union[Unset, str]):
        received_since (Union[Unset, str]):
        type_ (Union[Unset, CommunicationindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommunicationList, Error]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        created_since=created_since,
        date=date,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        having_time_entries=having_time_entries,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        query=query,
        received_at=received_at,
        received_before=received_before,
        received_since=received_since,
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
    contact_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    date: Unset | str = UNSET,
    external_property_name: Unset | str = UNSET,
    external_property_value: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    having_time_entries: Unset | bool = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | CommunicationindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    received_at: Unset | str = UNSET,
    received_before: Unset | str = UNSET,
    received_since: Unset | str = UNSET,
    type_: Unset | CommunicationindexType = UNSET,
    updated_since: Unset | str = UNSET,
    user_id: Unset | int = UNSET,
    x_api_version: Unset | str = UNSET,
) -> CommunicationList | Error | None:
    """Return the data for all Communications

     Outlines the parameters, optional and required, used when requesting the data for all Communications

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        date (Union[Unset, str]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        having_time_entries (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, CommunicationindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        received_at (Union[Unset, str]):
        received_before (Union[Unset, str]):
        received_since (Union[Unset, str]):
        type_ (Union[Unset, CommunicationindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommunicationList, Error]
    """

    return sync_detailed(
        client=client,
        contact_id=contact_id,
        created_since=created_since,
        date=date,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        having_time_entries=having_time_entries,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        query=query,
        received_at=received_at,
        received_before=received_before,
        received_since=received_since,
        type_=type_,
        updated_since=updated_since,
        user_id=user_id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    contact_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    date: Unset | str = UNSET,
    external_property_name: Unset | str = UNSET,
    external_property_value: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    having_time_entries: Unset | bool = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | CommunicationindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    received_at: Unset | str = UNSET,
    received_before: Unset | str = UNSET,
    received_since: Unset | str = UNSET,
    type_: Unset | CommunicationindexType = UNSET,
    updated_since: Unset | str = UNSET,
    user_id: Unset | int = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[CommunicationList | Error]:
    """Return the data for all Communications

     Outlines the parameters, optional and required, used when requesting the data for all Communications

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        date (Union[Unset, str]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        having_time_entries (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, CommunicationindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        received_at (Union[Unset, str]):
        received_before (Union[Unset, str]):
        received_since (Union[Unset, str]):
        type_ (Union[Unset, CommunicationindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommunicationList, Error]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        created_since=created_since,
        date=date,
        external_property_name=external_property_name,
        external_property_value=external_property_value,
        fields=fields,
        having_time_entries=having_time_entries,
        ids=ids,
        limit=limit,
        matter_id=matter_id,
        order=order,
        page_token=page_token,
        query=query,
        received_at=received_at,
        received_before=received_before,
        received_since=received_since,
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
    contact_id: Unset | int = UNSET,
    created_since: Unset | str = UNSET,
    date: Unset | str = UNSET,
    external_property_name: Unset | str = UNSET,
    external_property_value: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    having_time_entries: Unset | bool = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    matter_id: Unset | int = UNSET,
    order: Unset | CommunicationindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    received_at: Unset | str = UNSET,
    received_before: Unset | str = UNSET,
    received_since: Unset | str = UNSET,
    type_: Unset | CommunicationindexType = UNSET,
    updated_since: Unset | str = UNSET,
    user_id: Unset | int = UNSET,
    x_api_version: Unset | str = UNSET,
) -> CommunicationList | Error | None:
    """Return the data for all Communications

     Outlines the parameters, optional and required, used when requesting the data for all Communications

    Args:
        contact_id (Union[Unset, int]):
        created_since (Union[Unset, str]):
        date (Union[Unset, str]):
        external_property_name (Union[Unset, str]):
        external_property_value (Union[Unset, str]):
        fields (Union[Unset, str]):
        having_time_entries (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        matter_id (Union[Unset, int]):
        order (Union[Unset, CommunicationindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        received_at (Union[Unset, str]):
        received_before (Union[Unset, str]):
        received_since (Union[Unset, str]):
        type_ (Union[Unset, CommunicationindexType]):
        updated_since (Union[Unset, str]):
        user_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommunicationList, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            contact_id=contact_id,
            created_since=created_since,
            date=date,
            external_property_name=external_property_name,
            external_property_value=external_property_value,
            fields=fields,
            having_time_entries=having_time_entries,
            ids=ids,
            limit=limit,
            matter_id=matter_id,
            order=order,
            page_token=page_token,
            query=query,
            received_at=received_at,
            received_before=received_before,
            received_since=received_since,
            type_=type_,
            updated_since=updated_since,
            user_id=user_id,
            x_api_version=x_api_version,
        )
    ).parsed
