from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.lauk_civil_controlled_rate_list import LaukCivilControlledRateList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    activity: Unset | str = UNSET,
    category_of_law: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    key: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    page_token: Unset | str = UNSET,
    rate_type: Unset | str = UNSET,
    region: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["activity"] = activity

    params["category_of_law"] = category_of_law

    params["fields"] = fields

    params["key"] = key

    params["limit"] = limit

    params["page_token"] = page_token

    params["rate_type"] = rate_type

    params["region"] = region

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/lauk_civil_controlled_rates.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | LaukCivilControlledRateList | None:
    if response.status_code == 200:
        response_200 = LaukCivilControlledRateList.from_dict(response.json())

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
) -> Response[Error | LaukCivilControlledRateList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    activity: Unset | str = UNSET,
    category_of_law: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    key: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    page_token: Unset | str = UNSET,
    rate_type: Unset | str = UNSET,
    region: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | LaukCivilControlledRateList]:
    """List Civil Controlled Rates

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukCivilControlledRates

    Args:
        activity (Union[Unset, str]):
        category_of_law (Union[Unset, str]):
        fields (Union[Unset, str]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        rate_type (Union[Unset, str]):
        region (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LaukCivilControlledRateList]]
    """

    kwargs = _get_kwargs(
        activity=activity,
        category_of_law=category_of_law,
        fields=fields,
        key=key,
        limit=limit,
        page_token=page_token,
        rate_type=rate_type,
        region=region,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    activity: Unset | str = UNSET,
    category_of_law: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    key: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    page_token: Unset | str = UNSET,
    rate_type: Unset | str = UNSET,
    region: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | LaukCivilControlledRateList | None:
    """List Civil Controlled Rates

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukCivilControlledRates

    Args:
        activity (Union[Unset, str]):
        category_of_law (Union[Unset, str]):
        fields (Union[Unset, str]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        rate_type (Union[Unset, str]):
        region (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LaukCivilControlledRateList]
    """

    return sync_detailed(
        client=client,
        activity=activity,
        category_of_law=category_of_law,
        fields=fields,
        key=key,
        limit=limit,
        page_token=page_token,
        rate_type=rate_type,
        region=region,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    activity: Unset | str = UNSET,
    category_of_law: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    key: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    page_token: Unset | str = UNSET,
    rate_type: Unset | str = UNSET,
    region: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | LaukCivilControlledRateList]:
    """List Civil Controlled Rates

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukCivilControlledRates

    Args:
        activity (Union[Unset, str]):
        category_of_law (Union[Unset, str]):
        fields (Union[Unset, str]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        rate_type (Union[Unset, str]):
        region (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LaukCivilControlledRateList]]
    """

    kwargs = _get_kwargs(
        activity=activity,
        category_of_law=category_of_law,
        fields=fields,
        key=key,
        limit=limit,
        page_token=page_token,
        rate_type=rate_type,
        region=region,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    activity: Unset | str = UNSET,
    category_of_law: Unset | str = UNSET,
    fields: Unset | str = UNSET,
    key: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    page_token: Unset | str = UNSET,
    rate_type: Unset | str = UNSET,
    region: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | LaukCivilControlledRateList | None:
    """List Civil Controlled Rates

     Outlines the parameters, optional and required, used when requesting the data for all
    LaukCivilControlledRates

    Args:
        activity (Union[Unset, str]):
        category_of_law (Union[Unset, str]):
        fields (Union[Unset, str]):
        key (Union[Unset, str]):
        limit (Union[Unset, int]):
        page_token (Union[Unset, str]):
        rate_type (Union[Unset, str]):
        region (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LaukCivilControlledRateList]
    """

    return (
        await asyncio_detailed(
            client=client,
            activity=activity,
            category_of_law=category_of_law,
            fields=fields,
            key=key,
            limit=limit,
            page_token=page_token,
            rate_type=rate_type,
            region=region,
            x_api_version=x_api_version,
        )
    ).parsed
