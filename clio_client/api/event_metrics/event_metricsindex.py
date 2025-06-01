from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.event_metrics_show import EventMetricsShow
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fields: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/internal_notifications/event_metrics.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | EventMetricsShow | None:
    if response.status_code == 200:
        response_200 = EventMetricsShow.from_dict(response.json())

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
) -> Response[Error | EventMetricsShow]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    fields: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | EventMetricsShow]:
    """Unread in-app notification events

     Outlines the parameters, optional and required, used when requesting Event Metrics

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, EventMetricsShow]]
    """

    kwargs = _get_kwargs(
        fields=fields,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    fields: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | EventMetricsShow | None:
    """Unread in-app notification events

     Outlines the parameters, optional and required, used when requesting Event Metrics

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, EventMetricsShow]
    """

    return sync_detailed(
        client=client,
        fields=fields,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    fields: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Error | EventMetricsShow]:
    """Unread in-app notification events

     Outlines the parameters, optional and required, used when requesting Event Metrics

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, EventMetricsShow]]
    """

    kwargs = _get_kwargs(
        fields=fields,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    fields: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Error | EventMetricsShow | None:
    """Unread in-app notification events

     Outlines the parameters, optional and required, used when requesting Event Metrics

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, EventMetricsShow]
    """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
            x_api_version=x_api_version,
        )
    ).parsed
