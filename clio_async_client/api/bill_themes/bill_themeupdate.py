from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bill_theme_show import BillThemeShow
from ...models.bill_themeupdate_data_body import BillThemeupdateDataBody
from ...models.bill_themeupdate_files_body import BillThemeupdateFilesBody
from ...models.bill_themeupdate_json_body import BillThemeupdateJsonBody
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: Union[
        BillThemeupdateJsonBody,
        BillThemeupdateDataBody,
        BillThemeupdateFilesBody,
    ],
    fields: Union[Unset, str] = UNSET,
    if_match: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["IF-MATCH"] = if_match

    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/bill_themes/{id}.json",
        "params": params,
    }

    if isinstance(body, BillThemeupdateJsonBody):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, BillThemeupdateDataBody):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, BillThemeupdateFilesBody):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BillThemeShow, Error]]:
    if response.status_code == 200:
        response_200 = BillThemeShow.from_dict(response.json())

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
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 412:
        response_412 = Error.from_dict(response.json())

        return response_412
    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422
    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BillThemeShow, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        BillThemeupdateJsonBody,
        BillThemeupdateDataBody,
        BillThemeupdateFilesBody,
    ],
    fields: Union[Unset, str] = UNSET,
    if_match: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[BillThemeShow, Error]]:
    """Update a single BillTheme

     Outlines the parameters and data fields used when updating a single BillTheme

    Args:
        id (int):
        fields (Union[Unset, str]):
        if_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (BillThemeupdateJsonBody):
        body (BillThemeupdateDataBody):
        body (BillThemeupdateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillThemeShow, Error]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        fields=fields,
        if_match=if_match,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        BillThemeupdateJsonBody,
        BillThemeupdateDataBody,
        BillThemeupdateFilesBody,
    ],
    fields: Union[Unset, str] = UNSET,
    if_match: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[BillThemeShow, Error]]:
    """Update a single BillTheme

     Outlines the parameters and data fields used when updating a single BillTheme

    Args:
        id (int):
        fields (Union[Unset, str]):
        if_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (BillThemeupdateJsonBody):
        body (BillThemeupdateDataBody):
        body (BillThemeupdateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BillThemeShow, Error]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        fields=fields,
        if_match=if_match,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        BillThemeupdateJsonBody,
        BillThemeupdateDataBody,
        BillThemeupdateFilesBody,
    ],
    fields: Union[Unset, str] = UNSET,
    if_match: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[BillThemeShow, Error]]:
    """Update a single BillTheme

     Outlines the parameters and data fields used when updating a single BillTheme

    Args:
        id (int):
        fields (Union[Unset, str]):
        if_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (BillThemeupdateJsonBody):
        body (BillThemeupdateDataBody):
        body (BillThemeupdateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillThemeShow, Error]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        fields=fields,
        if_match=if_match,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        BillThemeupdateJsonBody,
        BillThemeupdateDataBody,
        BillThemeupdateFilesBody,
    ],
    fields: Union[Unset, str] = UNSET,
    if_match: Union[Unset, str] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[BillThemeShow, Error]]:
    """Update a single BillTheme

     Outlines the parameters and data fields used when updating a single BillTheme

    Args:
        id (int):
        fields (Union[Unset, str]):
        if_match (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (BillThemeupdateJsonBody):
        body (BillThemeupdateDataBody):
        body (BillThemeupdateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BillThemeShow, Error]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            fields=fields,
            if_match=if_match,
            x_api_version=x_api_version,
        )
    ).parsed
