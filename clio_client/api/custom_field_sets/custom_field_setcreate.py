from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_set_show import CustomFieldSetShow
from ...models.custom_field_setcreate_data_body import CustomFieldSetcreateDataBody
from ...models.custom_field_setcreate_files_body import CustomFieldSetcreateFilesBody
from ...models.custom_field_setcreate_json_body import CustomFieldSetcreateJsonBody
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CustomFieldSetcreateJsonBody
    | CustomFieldSetcreateDataBody
    | CustomFieldSetcreateFilesBody,
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
        "url": "/custom_field_sets.json",
        "params": params,
    }

    if isinstance(body, CustomFieldSetcreateJsonBody):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, CustomFieldSetcreateDataBody):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, CustomFieldSetcreateFilesBody):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomFieldSetShow | Error | None:
    if response.status_code == 201:
        response_201 = CustomFieldSetShow.from_dict(response.json())

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
) -> Response[CustomFieldSetShow | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CustomFieldSetcreateJsonBody
    | CustomFieldSetcreateDataBody
    | CustomFieldSetcreateFilesBody,
    fields: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[CustomFieldSetShow | Error]:
    """Create a new CustomFieldSet

     Outlines the parameters and data fields used when creating a new CustomFieldSet

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (CustomFieldSetcreateJsonBody):
        body (CustomFieldSetcreateDataBody):
        body (CustomFieldSetcreateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomFieldSetShow, Error]]
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
    body: CustomFieldSetcreateJsonBody
    | CustomFieldSetcreateDataBody
    | CustomFieldSetcreateFilesBody,
    fields: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> CustomFieldSetShow | Error | None:
    """Create a new CustomFieldSet

     Outlines the parameters and data fields used when creating a new CustomFieldSet

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (CustomFieldSetcreateJsonBody):
        body (CustomFieldSetcreateDataBody):
        body (CustomFieldSetcreateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomFieldSetShow, Error]
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
    body: CustomFieldSetcreateJsonBody
    | CustomFieldSetcreateDataBody
    | CustomFieldSetcreateFilesBody,
    fields: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> Response[CustomFieldSetShow | Error]:
    """Create a new CustomFieldSet

     Outlines the parameters and data fields used when creating a new CustomFieldSet

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (CustomFieldSetcreateJsonBody):
        body (CustomFieldSetcreateDataBody):
        body (CustomFieldSetcreateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CustomFieldSetShow, Error]]
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
    body: CustomFieldSetcreateJsonBody
    | CustomFieldSetcreateDataBody
    | CustomFieldSetcreateFilesBody,
    fields: Unset | str = UNSET,
    x_api_version: Unset | str = UNSET,
) -> CustomFieldSetShow | Error | None:
    """Create a new CustomFieldSet

     Outlines the parameters and data fields used when creating a new CustomFieldSet

    Args:
        fields (Union[Unset, str]):
        x_api_version (Union[Unset, str]):
        body (CustomFieldSetcreateJsonBody):
        body (CustomFieldSetcreateDataBody):
        body (CustomFieldSetcreateFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CustomFieldSetShow, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            fields=fields,
            x_api_version=x_api_version,
        )
    ).parsed
