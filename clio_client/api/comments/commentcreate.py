from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.comment_show import CommentShow
from ...models.commentcreate_data_body import CommentcreateDataBody
from ...models.commentcreate_files_body import CommentcreateFilesBody
from ...models.commentcreate_json_body import CommentcreateJsonBody
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CommentcreateJsonBody | CommentcreateDataBody | CommentcreateFilesBody,
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
        "method": "post",
        "url": "/comments.json",
        "params": params,
    }

    if isinstance(body, CommentcreateJsonBody):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, CommentcreateDataBody):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CommentcreateFilesBody):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CommentShow | Error | None:
    if response.status_code == 201:
        response_201 = CommentShow.from_dict(response.json())

        return response_201
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CommentShow | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CommentcreateJsonBody | CommentcreateDataBody | CommentcreateFilesBody,
    fields: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[CommentShow | Error]:
    """Create a new Comment

     Outlines the parameters and data fields used when creating a new Comment

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (CommentcreateJsonBody):
        body (CommentcreateDataBody):
        body (CommentcreateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommentShow, Error]]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: CommentcreateJsonBody | CommentcreateDataBody | CommentcreateFilesBody,
    fields: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> CommentShow | Error | None:
    """Create a new Comment

     Outlines the parameters and data fields used when creating a new Comment

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (CommentcreateJsonBody):
        body (CommentcreateDataBody):
        body (CommentcreateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommentShow, Error]
    """

    return sync_detailed(
        client=client,
        body=body,
        fields=fields,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CommentcreateJsonBody | CommentcreateDataBody | CommentcreateFilesBody,
    fields: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[CommentShow | Error]:
    """Create a new Comment

     Outlines the parameters and data fields used when creating a new Comment

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (CommentcreateJsonBody):
        body (CommentcreateDataBody):
        body (CommentcreateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommentShow, Error]]
    """

    kwargs = _get_kwargs(
        body=body,
        fields=fields,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CommentcreateJsonBody | CommentcreateDataBody | CommentcreateFilesBody,
    fields: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> CommentShow | Error | None:
    """Create a new Comment

     Outlines the parameters and data fields used when creating a new Comment

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (CommentcreateJsonBody):
        body (CommentcreateDataBody):
        body (CommentcreateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommentShow, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            fields=fields,
            x_api_version=x_api_version,
        )
    ).parsed
