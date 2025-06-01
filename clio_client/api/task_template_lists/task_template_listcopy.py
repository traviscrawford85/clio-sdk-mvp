from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.task_template_list_show import TaskTemplateListShow
from ...models.task_template_listcopy_data_body import TaskTemplateListcopyDataBody
from ...models.task_template_listcopy_files_body import TaskTemplateListcopyFilesBody
from ...models.task_template_listcopy_json_body import TaskTemplateListcopyJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: TaskTemplateListcopyJsonBody
    | TaskTemplateListcopyDataBody
    | TaskTemplateListcopyFilesBody,
    fields: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/task_template_lists/{id}/copy.json",
        "params": params,
    }

    if isinstance(body, TaskTemplateListcopyJsonBody):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, TaskTemplateListcopyDataBody):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, TaskTemplateListcopyFilesBody):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | TaskTemplateListShow | None:
    if response.status_code == 201:
        response_201 = TaskTemplateListShow.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | TaskTemplateListShow]:
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
    body: TaskTemplateListcopyJsonBody
    | TaskTemplateListcopyDataBody
    | TaskTemplateListcopyFilesBody,
    fields: Unset | str = UNSET,
) -> Response[Error | TaskTemplateListShow]:
    """Copy a TaskTemplateList

     Creates a copy of the TaskTemplateList identified by the `id` path parameter.

    Args:
        id (int):
        fields (Union[Unset, str]):
        body (TaskTemplateListcopyJsonBody):
        body (TaskTemplateListcopyDataBody):
        body (TaskTemplateListcopyFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, TaskTemplateListShow]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: TaskTemplateListcopyJsonBody
    | TaskTemplateListcopyDataBody
    | TaskTemplateListcopyFilesBody,
    fields: Unset | str = UNSET,
) -> Error | TaskTemplateListShow | None:
    """Copy a TaskTemplateList

     Creates a copy of the TaskTemplateList identified by the `id` path parameter.

    Args:
        id (int):
        fields (Union[Unset, str]):
        body (TaskTemplateListcopyJsonBody):
        body (TaskTemplateListcopyDataBody):
        body (TaskTemplateListcopyFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, TaskTemplateListShow]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: TaskTemplateListcopyJsonBody
    | TaskTemplateListcopyDataBody
    | TaskTemplateListcopyFilesBody,
    fields: Unset | str = UNSET,
) -> Response[Error | TaskTemplateListShow]:
    """Copy a TaskTemplateList

     Creates a copy of the TaskTemplateList identified by the `id` path parameter.

    Args:
        id (int):
        fields (Union[Unset, str]):
        body (TaskTemplateListcopyJsonBody):
        body (TaskTemplateListcopyDataBody):
        body (TaskTemplateListcopyFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, TaskTemplateListShow]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: TaskTemplateListcopyJsonBody
    | TaskTemplateListcopyDataBody
    | TaskTemplateListcopyFilesBody,
    fields: Unset | str = UNSET,
) -> Error | TaskTemplateListShow | None:
    """Copy a TaskTemplateList

     Creates a copy of the TaskTemplateList identified by the `id` path parameter.

    Args:
        id (int):
        fields (Union[Unset, str]):
        body (TaskTemplateListcopyJsonBody):
        body (TaskTemplateListcopyDataBody):
        body (TaskTemplateListcopyFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, TaskTemplateListShow]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            fields=fields,
        )
    ).parsed
