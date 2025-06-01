from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_value import CustomFieldValue
from ...types import Response


def _get_kwargs(
    *,
    body: CustomFieldValue,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/custom-field-values",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomFieldValue | None:
    if response.status_code == 201:
        response_201 = CustomFieldValue.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CustomFieldValue]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CustomFieldValue,
) -> Response[CustomFieldValue]:
    """Create a CustomFieldValue

     Outlines the parameters and data fields used when creating a new CustomFieldValue.
    The `custom_field_id` is required, and the `value` field must match the type
    of the CustomField.

    Args:
        body (CustomFieldValue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldValue]
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
    client: AuthenticatedClient | Client,
    body: CustomFieldValue,
) -> CustomFieldValue | None:
    """Create a CustomFieldValue

     Outlines the parameters and data fields used when creating a new CustomFieldValue.
    The `custom_field_id` is required, and the `value` field must match the type
    of the CustomField.

    Args:
        body (CustomFieldValue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldValue
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CustomFieldValue,
) -> Response[CustomFieldValue]:
    """Create a CustomFieldValue

     Outlines the parameters and data fields used when creating a new CustomFieldValue.
    The `custom_field_id` is required, and the `value` field must match the type
    of the CustomField.

    Args:
        body (CustomFieldValue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomFieldValue]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CustomFieldValue,
) -> CustomFieldValue | None:
    """Create a CustomFieldValue

     Outlines the parameters and data fields used when creating a new CustomFieldValue.
    The `custom_field_id` is required, and the `value` field must match the type
    of the CustomField.

    Args:
        body (CustomFieldValue):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomFieldValue
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
