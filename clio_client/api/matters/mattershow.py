from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.matter_show import MatterShow
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    custom_field_ids: Unset | int = UNSET,
    fields: Unset | str = UNSET,
    if_modified_since: Unset | str = UNSET,
    if_none_match: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_modified_since, Unset):
        headers["IF-MODIFIED-SINCE"] = if_modified_since

    if not isinstance(if_none_match, Unset):
        headers["IF-NONE-MATCH"] = if_none_match

    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["custom_field_ids[]"] = custom_field_ids

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/matters/{id}.json",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | MatterShow | None:
    if response.status_code == 200:
        response_200 = MatterShow.from_dict(response.json())

        return response_200
    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error | MatterShow]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    custom_field_ids: Unset | int = UNSET,
    fields: Unset | str = UNSET,
    if_modified_since: Unset | str = UNSET,
    if_none_match: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Any | Error | MatterShow]:
    """Return the data for a single Matter

     Outlines the parameters, optional and required, used when requesting the data for a single Matter

    Args:
        id (int):
        custom_field_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        if_modified_since (Union[Unset, str]):
        if_none_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, MatterShow]]
    """

    kwargs = _get_kwargs(
        id=id,
        custom_field_ids=custom_field_ids,
        fields=fields,
        if_modified_since=if_modified_since,
        if_none_match=if_none_match,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    custom_field_ids: Unset | int = UNSET,
    fields: Unset | str = UNSET,
    if_modified_since: Unset | str = UNSET,
    if_none_match: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Any | Error | MatterShow | None:
    """Return the data for a single Matter

     Outlines the parameters, optional and required, used when requesting the data for a single Matter

    Args:
        id (int):
        custom_field_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        if_modified_since (Union[Unset, str]):
        if_none_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, MatterShow]
    """

    return sync_detailed(
        id=id,
        client=client,
        custom_field_ids=custom_field_ids,
        fields=fields,
        if_modified_since=if_modified_since,
        if_none_match=if_none_match,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    custom_field_ids: Unset | int = UNSET,
    fields: Unset | str = UNSET,
    if_modified_since: Unset | str = UNSET,
    if_none_match: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[Any | Error | MatterShow]:
    """Return the data for a single Matter

     Outlines the parameters, optional and required, used when requesting the data for a single Matter

    Args:
        id (int):
        custom_field_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        if_modified_since (Union[Unset, str]):
        if_none_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, MatterShow]]
    """

    kwargs = _get_kwargs(
        id=id,
        custom_field_ids=custom_field_ids,
        fields=fields,
        if_modified_since=if_modified_since,
        if_none_match=if_none_match,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    custom_field_ids: Unset | int = UNSET,
    fields: Unset | str = UNSET,
    if_modified_since: Unset | str = UNSET,
    if_none_match: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Any | Error | MatterShow | None:
    """Return the data for a single Matter

     Outlines the parameters, optional and required, used when requesting the data for a single Matter

    Args:
        id (int):
        custom_field_ids (Union[Unset, int]):
        fields (Union[Unset, str]):
        if_modified_since (Union[Unset, str]):
        if_none_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, MatterShow]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            custom_field_ids=custom_field_ids,
            fields=fields,
            if_modified_since=if_modified_since,
            if_none_match=if_none_match,
            x_api_version=x_api_version,
        )
    ).parsed
