from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.statute_of_limitations_compute_request import (
    StatuteOfLimitationsComputeRequest,
)
from ...models.statute_of_limitations_compute_response import (
    StatuteOfLimitationsComputeResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    body: StatuteOfLimitationsComputeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/statutes-of-limitations/compute",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[StatuteOfLimitationsComputeResponse]:
    if response.status_code == 200:
        response_200 = StatuteOfLimitationsComputeResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[StatuteOfLimitationsComputeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: StatuteOfLimitationsComputeRequest,
) -> Response[StatuteOfLimitationsComputeResponse]:
    """Compute the statute of limitations due date

     Computes the due date based on a provided incident date (e.g., for Auto Accident matters).

    Args:
        body (StatuteOfLimitationsComputeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StatuteOfLimitationsComputeResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: StatuteOfLimitationsComputeRequest,
) -> Optional[StatuteOfLimitationsComputeResponse]:
    """Compute the statute of limitations due date

     Computes the due date based on a provided incident date (e.g., for Auto Accident matters).

    Args:
        body (StatuteOfLimitationsComputeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StatuteOfLimitationsComputeResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: StatuteOfLimitationsComputeRequest,
) -> Response[StatuteOfLimitationsComputeResponse]:
    """Compute the statute of limitations due date

     Computes the due date based on a provided incident date (e.g., for Auto Accident matters).

    Args:
        body (StatuteOfLimitationsComputeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StatuteOfLimitationsComputeResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: StatuteOfLimitationsComputeRequest,
) -> Optional[StatuteOfLimitationsComputeResponse]:
    """Compute the statute of limitations due date

     Computes the due date based on a provided incident date (e.g., for Auto Accident matters).

    Args:
        body (StatuteOfLimitationsComputeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StatuteOfLimitationsComputeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
