from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.jurisdiction_list import JurisdictionList
from ...models.jurisdictionindex_order import JurisdictionindexOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    for_current_account: Unset | bool = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    order: Unset | JurisdictionindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["created_since"] = created_since

    params["fields"] = fields

    params["for_current_account"] = for_current_account

    params["ids[]"] = ids

    params["limit"] = limit

    json_order: Unset | str = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["page_token"] = page_token

    params["query"] = query

    params["updated_since"] = updated_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/court_rules/jurisdictions.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | JurisdictionList | None:
    if response.status_code == 200:
        response_200 = JurisdictionList.from_dict(response.json())

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
) -> Response[Error | JurisdictionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    for_current_account: Unset | bool = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    order: Unset | JurisdictionindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | JurisdictionList]:
    """Return the data for all jurisdictions

     Outlines the parameters, optional and required, used when requesting the data for all Jurisdictions

    Args:
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        for_current_account (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, JurisdictionindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, JurisdictionList]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        fields=fields,
        for_current_account=for_current_account,
        ids=ids,
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
    *,
    client: AuthenticatedClient | Client,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    for_current_account: Unset | bool = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    order: Unset | JurisdictionindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | JurisdictionList | None:
    """Return the data for all jurisdictions

     Outlines the parameters, optional and required, used when requesting the data for all Jurisdictions

    Args:
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        for_current_account (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, JurisdictionindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, JurisdictionList]
    """

    return sync_detailed(
        client=client,
        created_since=created_since,
        fields=fields,
        for_current_account=for_current_account,
        ids=ids,
        limit=limit,
        order=order,
        page_token=page_token,
        query=query,
        updated_since=updated_since,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    for_current_account: Unset | bool = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    order: Unset | JurisdictionindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | JurisdictionList]:
    """Return the data for all jurisdictions

     Outlines the parameters, optional and required, used when requesting the data for all Jurisdictions

    Args:
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        for_current_account (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, JurisdictionindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, JurisdictionList]]
    """

    kwargs = _get_kwargs(
        created_since=created_since,
        fields=fields,
        for_current_account=for_current_account,
        ids=ids,
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
    *,
    client: AuthenticatedClient | Client,
    created_since: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    for_current_account: Unset | bool = UNSET,
    ids: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    order: Unset | JurisdictionindexOrder = UNSET,
    page_token: Unset | str = UNSET,
    query: Unset | str = UNSET,
    updated_since: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | JurisdictionList | None:
    """Return the data for all jurisdictions

     Outlines the parameters, optional and required, used when requesting the data for all Jurisdictions

    Args:
        created_since (Union[Unset, str]):
        fields (Union[Unset, str]):
        for_current_account (Union[Unset, bool]):
        ids (Union[Unset, int]):
        limit (Union[Unset, int]):
        order (Union[Unset, JurisdictionindexOrder]):
        page_token (Union[Unset, str]):
        query (Union[Unset, str]):
        updated_since (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, JurisdictionList]
    """

    return (
        await asyncio_detailed(
            client=client,
            created_since=created_since,
            fields=fields,
            for_current_account=for_current_account,
            ids=ids,
            limit=limit,
            order=order,
            page_token=page_token,
            query=query,
            updated_since=updated_since,
            x_api_version=x_api_version,
        )
    ).parsed
